# Author: Akshay Srivatsan
# Description: Edits the Info.plist of a Mac Application to prevent it from showing in the dock.
import sys
import plistlib
key = 'LSUIElement'

if len(sys.argv) == 1:
    print 'Usage: python hide_from_dock.py filename'
    sys.exit(1)

path = sys.argv[1]

fp = open(path + "/Contents/Info.plist", "rwb")
pl = plistlib.readPlist(fp)
if not key in pl:
    pl[key] = 1
elif pl[key]:
    pl[key] = 0
else:
    pl[key] = 1

plistlib.writePlist(pl, path + "/Contents/Info.plist")
