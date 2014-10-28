# Akshay Srivatsan
# Adds custom icons to a file from a source directory. Requires Developer Tools to be installed.


import os
import sys



def reicon(target, folder, ext):
    name = os.path.splitext(os.path.basename(target))[0]
    tf = os.path.normpath(folder + '/' + name + '.' + ext)

    if not os.path.exists(tf):
        print "Error:", tf, "does not exist!"
        sys.exit(100)

    os.system('sips -i "' + tf + '"')
    os.system('DeRez -only icns "' + tf + '" > /tmp/com.appspot.akshay-srivatsan.icon_changer.tmp')
    os.system('Rez -o $\'' + target + '/' + 'Icon\\r\' -append /tmp/com.appspot.akshay-srivatsan.icon_changer.tmp')
    os.system('SetFile -a C "' + target + '"')
    os.system('SetFile -a V $\'' + target + '/Icon\\r\'')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'Usage: python icon_changer.py file_or_folder_to_change folder_containing_icons extension'
        sys.exit(1)

    target = sys.argv[1].split('/')[0]
    folder = sys.argv[2]
    ext = sys.argv[3]
    reicon(target, folder, ext)
