// Auto-generated. Do not edit!

// (in-package mavros_msgs.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class HilActuatorControls {
  constructor() {
    this.header = new std_msgs.msg.Header();
    this.controls = new Array(16).fill(0);
    this.mode = 0;
    this.flags = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type HilActuatorControls
    // Serialize message field [header]
    bufferInfo = std_msgs.msg.Header.serialize(obj.header, bufferInfo);
    // Serialize message field [controls]
    obj.controls.forEach((val) => {
      bufferInfo = _serializer.float32(val, bufferInfo);
    });
    // Serialize message field [mode]
    bufferInfo = _serializer.uint8(obj.mode, bufferInfo);
    // Serialize message field [flags]
    bufferInfo = _serializer.uint64(obj.flags, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type HilActuatorControls
    let tmp;
    let len;
    let data = new HilActuatorControls();
    // Deserialize message field [header]
    tmp = std_msgs.msg.Header.deserialize(buffer);
    data.header = tmp.data;
    buffer = tmp.buffer;
    len = 16;
    // Deserialize message field [controls]
    for (let i = 0; i < len; ++i) {
      tmp = _deserializer.float32(buffer);
      data.controls[i] = tmp.data;
      buffer = tmp.buffer;
    }
    // Deserialize message field [mode]
    tmp = _deserializer.uint8(buffer);
    data.mode = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [flags]
    tmp = _deserializer.uint64(buffer);
    data.flags = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'mavros_msgs/HilActuatorControls';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '18482e8ef0330ac2fc9a0421be1d11c3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # HilActuatorControls.msg
    #
    # ROS representation of MAVLink HIL_ACTUATOR_CONTROLS
    # See mavlink message documentation here:
    # https://pixhawk.ethz.ch/mavlink/#HIL_ACTUATOR_CONTROLS
    
    std_msgs/Header header
    float32[16] controls
    uint8 mode
    uint64 flags
    
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
    
    `;
  }

};

module.exports = HilActuatorControls;
