#!/bin/bash
# Akshay Srivatsan
# Removes the custom icons of all .app files in the current directory.
#   Requires root privileges to modify system apps.

for app in *.app
do
  python icon_remover.py "$app"
done
