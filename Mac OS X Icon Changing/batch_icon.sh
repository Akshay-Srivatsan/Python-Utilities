#!/bin/bash
# Akshay Srivatsan
# Changes the icons of all .app files in the current directory.
#   Requires root privileges to modify system apps.

for app in *.app
do
  python icon_changer.py "$app" "$1" "$2"
done
