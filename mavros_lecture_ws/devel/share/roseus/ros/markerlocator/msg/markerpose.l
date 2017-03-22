;; Auto-generated. Do not edit!


(when (boundp 'markerlocator::markerpose)
  (if (not (find-package "MARKERLOCATOR"))
    (make-package "MARKERLOCATOR"))
  (shadow 'markerpose (find-package "MARKERLOCATOR")))
(unless (find-package "MARKERLOCATOR::MARKERPOSE")
  (make-package "MARKERLOCATOR::MARKERPOSE"))

(in-package "ROS")
;;//! \htmlinclude markerpose.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass markerlocator::markerpose
  :super ros::object
  :slots (_header _order _x _y _theta _quality _timestamp ))

(defmethod markerlocator::markerpose
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:order __order) 0)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:theta __theta) 0.0)
    ((:quality __quality) 0.0)
    ((:timestamp __timestamp) (instance ros::time :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _order (round __order))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _theta (float __theta))
   (setq _quality (float __quality))
   (setq _timestamp __timestamp)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:order
   (&optional __order)
   (if __order (setq _order __order)) _order)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:theta
   (&optional __theta)
   (if __theta (setq _theta __theta)) _theta)
  (:quality
   (&optional __quality)
   (if __quality (setq _quality __quality)) _quality)
  (:timestamp
   (&optional __timestamp)
   (if __timestamp (setq _timestamp __timestamp)) _timestamp)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint8 _order
    1
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _theta
    8
    ;; float64 _quality
    8
    ;; time _timestamp
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint8 _order
       (write-byte _order s)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _theta
       (sys::poke _theta (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _quality
       (sys::poke _quality (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; time _timestamp
       (write-long (send _timestamp :sec) s) (write-long (send _timestamp :nsec) s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint8 _order
     (setq _order (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _theta
     (setq _theta (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _quality
     (setq _quality (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; time _timestamp
     (send _timestamp :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _timestamp :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get markerlocator::markerpose :md5sum-) "5b1f0f0642695a793c93c4a2dcaa8c41")
(setf (get markerlocator::markerpose :datatype-) "markerlocator/markerpose")
(setf (get markerlocator::markerpose :definition-)
      "Header 	 header
uint8    order
float64  x
float64  y
float64  theta
float64  quality
time     timestamp

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :markerlocator/markerpose "5b1f0f0642695a793c93c4a2dcaa8c41")


