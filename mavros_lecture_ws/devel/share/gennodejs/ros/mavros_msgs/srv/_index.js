
"use strict";

let FileRemove = require('./FileRemove.js')
let WaypointPush = require('./WaypointPush.js')
let ParamPull = require('./ParamPull.js')
let FileRead = require('./FileRead.js')
let CommandTOL = require('./CommandTOL.js')
let FileWrite = require('./FileWrite.js')
let ParamSet = require('./ParamSet.js')
let ParamPush = require('./ParamPush.js')
let FileChecksum = require('./FileChecksum.js')
let CommandBool = require('./CommandBool.js')
let CommandInt = require('./CommandInt.js')
let FileList = require('./FileList.js')
let FileClose = require('./FileClose.js')
let StreamRate = require('./StreamRate.js')
let CommandHome = require('./CommandHome.js')
let CommandLong = require('./CommandLong.js')
let WaypointClear = require('./WaypointClear.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let SetMode = require('./SetMode.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let FileTruncate = require('./FileTruncate.js')
let WaypointPull = require('./WaypointPull.js')
let FileOpen = require('./FileOpen.js')
let FileMakeDir = require('./FileMakeDir.js')
let FileRename = require('./FileRename.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let ParamGet = require('./ParamGet.js')

module.exports = {
  FileRemove: FileRemove,
  WaypointPush: WaypointPush,
  ParamPull: ParamPull,
  FileRead: FileRead,
  CommandTOL: CommandTOL,
  FileWrite: FileWrite,
  ParamSet: ParamSet,
  ParamPush: ParamPush,
  FileChecksum: FileChecksum,
  CommandBool: CommandBool,
  CommandInt: CommandInt,
  FileList: FileList,
  FileClose: FileClose,
  StreamRate: StreamRate,
  CommandHome: CommandHome,
  CommandLong: CommandLong,
  WaypointClear: WaypointClear,
  FileRemoveDir: FileRemoveDir,
  SetMode: SetMode,
  WaypointSetCurrent: WaypointSetCurrent,
  FileTruncate: FileTruncate,
  WaypointPull: WaypointPull,
  FileOpen: FileOpen,
  FileMakeDir: FileMakeDir,
  FileRename: FileRename,
  CommandTriggerControl: CommandTriggerControl,
  ParamGet: ParamGet,
};
