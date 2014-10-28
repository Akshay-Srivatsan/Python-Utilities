# Author: Akshay Srivatsan
# Description: Checks the Info.plist of a Mac Application to see if it is hidden from the dock.
import sys
import plistlib
key = 'LSUIElement'

if len(sys.argv) == 1:
    print 'Usage: python is_hidden.py filename'
    sys.exit(1)

path = sys.argv[1]

fp = open(path + "/Contents/Info.plist", "rwb")
pl = plistlib.readPlist(fp)
print path, "is",
if not key in pl:
    print "not hidden."
elif pl[key]:
    print "hidden."
else:
    print "not hidden."
