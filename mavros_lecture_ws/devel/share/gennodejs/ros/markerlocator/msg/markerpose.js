// Auto-generated. Do not edit!

// (in-package markerlocator.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class markerpose {
  constructor() {
    this.header = new std_msgs.msg.Header();
    this.order = 0;
    this.x = 0.0;
    this.y = 0.0;
    this.theta = 0.0;
    this.quality = 0.0;
    this.timestamp = {secs: 0, nsecs: 0};
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type markerpose
    // Serialize message field [header]
    bufferInfo = std_msgs.msg.Header.serialize(obj.header, bufferInfo);
    // Serialize message field [order]
    bufferInfo = _serializer.uint8(obj.order, bufferInfo);
    // Serialize message field [x]
    bufferInfo = _serializer.float64(obj.x, bufferInfo);
    // Serialize message field [y]
    bufferInfo = _serializer.float64(obj.y, bufferInfo);
    // Serialize message field [theta]
    bufferInfo = _serializer.float64(obj.theta, bufferInfo);
    // Serialize message field [quality]
    bufferInfo = _serializer.float64(obj.quality, bufferInfo);
    // Serialize message field [timestamp]
    bufferInfo = _serializer.time(obj.timestamp, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type markerpose
    let tmp;
    let len;
    let data = new markerpose();
    // Deserialize message field [header]
    tmp = std_msgs.msg.Header.deserialize(buffer);
    data.header = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [order]
    tmp = _deserializer.uint8(buffer);
    data.order = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [x]
    tmp = _deserializer.float64(buffer);
    data.x = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [y]
    tmp = _deserializer.float64(buffer);
    data.y = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [theta]
    tmp = _deserializer.float64(buffer);
    data.theta = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [quality]
    tmp = _deserializer.float64(buffer);
    data.quality = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [timestamp]
    tmp = _deserializer.time(buffer);
    data.timestamp = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'markerlocator/markerpose';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5b1f0f0642695a793c93c4a2dcaa8c41';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header 	 header
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
    
    `;
  }

};

module.exports = markerpose;
