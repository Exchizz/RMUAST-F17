/*
 *  Originally from: https://dev.px4.io/ros-mavros-offboard.html
 */

#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/State.h>
#include "../headers/image_converter.hpp"
#define COLOR       0

using namespace std;
using namespace cv;

mavros_msgs::State current_state;
geometry_msgs::PoseStamped localposemsg;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}

void localpose_cb(const geometry_msgs::PoseStamped::ConstPtr& msg){
  localposemsg = *msg;
}


void onmouse(int event, int x, int y, int flags, void* param){
    cv::Mat _img = *((cv::Mat*)(param));
    cv::Mat img = _img.clone();

    // Left click
    if (event == CV_EVENT_LBUTTONDOWN) {
        cv::Vec3b intensity = img.at<cv::Vec3b>(y, x);
        std::cout << "RGB = (" << int(intensity.val[2]) << ", " <<
            int(intensity.val[1]) << ", " << int(intensity.val[0]) << ")" << std::endl;
    }
}
bool find_center(Mat &image, Point2f &result){
    Mat segmented;

    inRange(image ,Scalar(0,0,200), Scalar(10,10,255), segmented);

    vector<vector<Point> > contours;
    vector<Vec4i> hierarchy;

    // Find contours
    findContours( segmented, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );

    /// Get the moments
    vector<Moments> mu(contours.size() );
    for( int i = 0; i < contours.size(); i++ )
     { mu[i] = moments( contours[i], false ); }

    ///  Get the mass centers:
    vector<Point2f> mc( contours.size() );
    for( int i = 0; i < contours.size(); i++ )
     { mc[i] = Point2f( mu[i].m10/mu[i].m00 , mu[i].m01/mu[i].m00 ); }

    /// Draw contours
    // for( int i = 0; i< contours.size(); i++ )
    //  {
    //    Scalar color = Scalar( rng.uniform(0, 255), rng.uniform(0,255), rng.uniform(0,255) );
    //    drawContours( drawing, contours, i, color, 2, 8, hierarchy, 0, Point() );
    //    circle( drawing, mc[i], 4, color, -1, 8, 0 );
    //  }

    if(mc.empty()){
        return false;
      }
    result = mc[0];
    return true;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "offb_node");
    ros::NodeHandle nh;

    ros::Subscriber state_sub = nh.subscribe<mavros_msgs::State>("mavros/state", 10, state_cb);
    ros::Publisher local_pos_pub = nh.advertise<geometry_msgs::PoseStamped>("mavros/setpoint_position/local", 10);
    ros::ServiceClient arming_client = nh.serviceClient<mavros_msgs::CommandBool>("mavros/cmd/arming");
    ros::ServiceClient set_mode_client = nh.serviceClient<mavros_msgs::SetMode>("mavros/set_mode");
    ros::Subscriber localpose_sub = nh.subscribe<geometry_msgs::PoseStamped>("/mavros/local_position/pose", 1, localpose_cb);
    ImageConverter image_conv("/iris/camera/image_raw", COLOR);
    //the setpoint publishing rate MUST be faster than 2Hz
    ros::Rate rate(20.0);

    //namedWindow("Image", 1);
    //setMouseCallback("Image", onmouse, NULL);
    // wait for FCU connection
    while(ros::ok() && current_state.connected){
        ros::spinOnce();
        rate.sleep();
    }

    geometry_msgs::PoseStamped pose;
    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = 2;

    //send a few setpoints before starting, or else you won't be able to switch to offboard mode
    for(int i = 100; ros::ok() && i > 0; --i){
        std::cout << "Starting " << 100-i << "%\r" << std::endl;
        local_pos_pub.publish(pose);
        ros::spinOnce();
        rate.sleep();
    }

    mavros_msgs::SetMode offb_set_mode;
    offb_set_mode.request.custom_mode = "OFFBOARD";

    mavros_msgs::CommandBool arm_cmd;
    arm_cmd.request.value = true;

    ros::Time last_request = ros::Time::now();

    while(ros::ok()){
        if( current_state.mode != "OFFBOARD" &&
            (ros::Time::now() - last_request > ros::Duration(5.0))){
            if( set_mode_client.call(offb_set_mode) &&
                offb_set_mode.response.success){
                ROS_INFO("Offboard enabled");
            }
            last_request = ros::Time::now();
        } else {
            if( !current_state.armed &&
                (ros::Time::now() - last_request > ros::Duration(5.0))){
                if( arming_client.call(arm_cmd) &&
                    arm_cmd.response.success){
                    ROS_INFO("Vehicle armed");
                }
                last_request = ros::Time::now();
            }
        }
        cv::Mat image = image_conv.get_image();

        if(!image.empty()){
          Point2f center;

          float X_pre_error = 0.0;
          float Y_pre_error = 0.0;

          if(find_center(image, center)){
              int camx = center.x; // px
              int camy = center.y; // px

              int imgwidth = image.cols;
              int imgheight = image.rows;
              circle(image, center, 10, Scalar(255,255,255));
              circle(image, Point2f(imgwidth/2, imgheight/2), 40, Scalar(255,0,255));

              int d = 2; // meters

              float Y = localposemsg.pose.position.y;
              float X = localposemsg.pose.position.x;

              std::cout << "image width: " << imgwidth << std::endl;
              std::cout << "relative posy: " << camy-imgheight/2 << " posx: " << camx-imgwidth/2 << std::endl;
              /*
              if((camy-imgheight/2) > 0){
                std::cout << "Go back" << std::endl;
                X-=0.1;
              } else {
                std::cout << "Go forward" << std::endl;
                X+=0.1;
              }

              if(camx-imgwidth/2 > 0){
                Y-=0.1;
              } else {
                Y+=0.1;
              }
              */

              /////////////////////////////////////////////////////////////////
              /////////////////////////////////////////////////////////////////
              float K_p = 0.001;

              float K_i = 0.06;
              float dt = 0.1;
              float X_integral = 0.0;
              float Y_integral = 0.0;

              float K_d = 0.0001;
              float X_derivative = 0.0;
              float Y_derivative = 0.0;

              float X_p = 0.0;
              float Y_p = 0.0;
              float X_i = 0.0;
              float Y_i = 0.0;
              float X_d = 0.0;
              float Y_d = 0.0;

              //Proportional term, error * K_p
              X_p = (camy-imgheight/2)*K_p;
              Y_p = (camx-imgwidth/2)*K_p;
              // Integrational term
              X_integral += (camy-imgheight/2) * dt;
              X_i = K_i * X_integral;

              Y_integral += (camx-imgwidth/2) * dt;
              Y_i = K_i * Y_integral;

              // Derivative term
              X_derivative = ((camy-imgheight/2) - X_pre_error) / dt;
              X_d = K_d * X_derivative;

              Y_derivative = ((camx-imgwidth/2) - Y_pre_error) / dt;
              Y_d = K_d * Y_derivative;

              //Total output
              X -= X_p + X_i + X_d;
              Y -= Y_p + Y_i + Y_d;

              X_pre_error = (camy-imgheight/2);
              Y_pre_error = (camx-imgwidth/2);
              /////////////////////////////////////////////////////////////////
              /////////////////////////////////////////////////////////////////
              std::cout << "X: " << X << " Y: " << Y << std::endl;

              pose.pose.position.x = X; // Meters
              pose.pose.position.y = Y; // Meters
              pose.pose.position.z = d; // Meters
            }
            cv::imshow("Image", image);
            waitKey(1);
        }
        local_pos_pub.publish(pose);

        ros::spinOnce();
        rate.sleep();
    }

    return 0;
}

