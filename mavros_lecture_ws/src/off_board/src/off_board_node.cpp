/*
 *  Originally from: https://dev.px4.io/ros-mavros-offboard.html
 */

#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/State.h>

mavros_msgs::State current_state;
geometry_msgs::PoseStamped localposemsg;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}

void localpose_cb(const geometry_msgs::PoseStamped::ConstPtr& msg){
  localposemsg = *msg;
}

int main(int argc, char **argv){
    ros::init(argc, argv, "offb_node");
    ros::NodeHandle nh;

    ros::Subscriber state_sub = nh.subscribe<mavros_msgs::State>("mavros/state", 10, state_cb);
    ros::Subscriber localpose_sub = nh.subscribe<geometry_msgs::PoseStamped>("/mavros/local_position/pose", 1, localpose_cb);


    ros::Publisher local_pos_pub = nh.advertise<geometry_msgs::PoseStamped>("mavros/setpoint_position/local", 10);
    ros::ServiceClient arming_client = nh.serviceClient<mavros_msgs::CommandBool>("mavros/cmd/arming");
    ros::ServiceClient set_mode_client = nh.serviceClient<mavros_msgs::SetMode>("mavros/set_mode");

    //the setpoint publishing rate MUST be faster than 2Hz
    ros::Rate rate(20.0);

    // wait for FCU connection
    while(ros::ok() && current_state.connected){
        ros::spinOnce();
        rate.sleep();
    }


    int camx = 0; // px
    int camy = 0; // px
    int d = 2; // meters
    float f = 0.01;

    int imgwidth = 0;
    int imgheight = 0;

// topic /mavros/local_position/pose
  // geometry_msgs/PoseStamped
    float X = (camx*d)/f;
    float Y = (camy*d)/f;

    X = localposemsg.pose.position.x + X - imgwidth/2;
    Y = localposemsg.pose.position.y + Y - imgheight/2;

    bool Markerfound = true;

    geometry_msgs::PoseStamped pose;

    if(Markerfound){
      pose.pose.position.x = X; // Meters
      pose.pose.position.y = Y; // Meters
      pose.pose.position.z = d; // Meters
    } else {
      pose.pose.position.x = 0; // Meters
      pose.pose.position.y = 0; // Meters
      pose.pose.position.z = d; // Meters
    }

    //send a few setpoints before starting, or else you won't be able to switch to offboard mode
    for(int i = 100; ros::ok() && i > 0; --i){
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
            if( set_mode_client.call(offb_set_mode) && offb_set_mode.response.success){
                ROS_INFO("Offboard enabled");
            }
            last_request = ros::Time::now();
        } else {
            if( !current_state.armed &&
                (ros::Time::now() - last_request > ros::Duration(5.0))){
                if( arming_client.call(arm_cmd) && arm_cmd.response.success){
                    ROS_INFO("Vehicle armed");
                }
                last_request = ros::Time::now();
            }
        }

        local_pos_pub.publish(pose);

        ros::spinOnce();
        rate.sleep();
    }

    return 0;
}
