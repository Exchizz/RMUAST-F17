// Generated by gencpp from file mavros_msgs/FileMakeDirRequest.msg
// DO NOT EDIT!


#ifndef MAVROS_MSGS_MESSAGE_FILEMAKEDIRREQUEST_H
#define MAVROS_MSGS_MESSAGE_FILEMAKEDIRREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mavros_msgs
{
template <class ContainerAllocator>
struct FileMakeDirRequest_
{
  typedef FileMakeDirRequest_<ContainerAllocator> Type;

  FileMakeDirRequest_()
    : dir_path()  {
    }
  FileMakeDirRequest_(const ContainerAllocator& _alloc)
    : dir_path(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _dir_path_type;
  _dir_path_type dir_path;




  typedef boost::shared_ptr< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> const> ConstPtr;

}; // struct FileMakeDirRequest_

typedef ::mavros_msgs::FileMakeDirRequest_<std::allocator<void> > FileMakeDirRequest;

typedef boost::shared_ptr< ::mavros_msgs::FileMakeDirRequest > FileMakeDirRequestPtr;
typedef boost::shared_ptr< ::mavros_msgs::FileMakeDirRequest const> FileMakeDirRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mavros_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'mavros_msgs': ['/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/mavros/mavros_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "401d5cf5f836aaa9ebdc0897f75da874";
  }

  static const char* value(const ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x401d5cf5f836aaa9ULL;
  static const uint64_t static_value2 = 0xebdc0897f75da874ULL;
};

template<class ContainerAllocator>
struct DataType< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mavros_msgs/FileMakeDirRequest";
  }

  static const char* value(const ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
\n\
\n\
\n\
\n\
string dir_path\n\
";
  }

  static const char* value(const ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.dir_path);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct FileMakeDirRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mavros_msgs::FileMakeDirRequest_<ContainerAllocator>& v)
  {
    s << indent << "dir_path: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.dir_path);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MAVROS_MSGS_MESSAGE_FILEMAKEDIRREQUEST_H
