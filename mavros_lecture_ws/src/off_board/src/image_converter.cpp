#include "../headers/image_converter.hpp"

ImageConverter::ImageConverter(std::string subcription, uint _type) : it_(nh_)
{
    this->type = _type;
    // Subscrive to input video feed
    image_sub_ = it_.subscribe(subcription, 1, &ImageConverter::imageCb, this);
}

ImageConverter::~ImageConverter()
{
}

void ImageConverter::imageCb(const sensor_msgs::ImageConstPtr& msg)
{
    cv_bridge::CvImagePtr cv_ptr;
    try {
        switch(this->type) {
            case 0:
                cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);       // RGB IMAGE
                break;
            case 1:
                // cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::TYPE_8UC1);    // DEPTH IMAGE
                cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::TYPE_32FC1);    // DEPTH IMAGE
                break;
        }
    } catch (cv_bridge::Exception& e) {
        ROS_ERROR("cv_bridge exception: %s", e.what());
        return;
    }

    image = cv_ptr->image.clone();
}

cv::Mat ImageConverter::get_image()
{
    return image.clone();
}
