# This file is generated by objective.metadata
#
# Last update: Mon Sep 24 11:13:32 2012

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$$'''
enums = '''$$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'eventDidFail:withError:', {'arguments': {2: {'type': 'r^{AEDesc=I^^{OpaqueAEDataStorageType}}'}}})
    r(b'SBApplication', b'isRunning', {'retval': {'type': 'Z'}})
    r(b'SBElementArray', b'arrayByApplyingSelector:', {'arguments': {2: {'sel_of_type': b'@@:'}}})
    r(b'SBElementArray', b'arrayByApplyingSelector:withObject:', {'arguments': {2: {'sel_of_type': b'@@:@'}}})
    r(b'SBObject', b'sendEvent:id:parameters:', {'variadic': True})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'eventDidFail:withError:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': 'r^{AEDesc=I^^{OpaqueAEDataStorageType}}'}, 3: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE