# Akshay Srivatsan
# Removes custom icons from a folder or application. Requires Developer Tools to be installed.

import os
import sys

def deicon(target):

    os.system('rm $\'' + target + '/Icon\\r\'')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python icon_remover.py file_or_folder_to_change'
        sys.exit(1)

    target = sys.argv[1].split('/')[0]
    deicon(target)
