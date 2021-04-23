#!/usr/bin/python3

import os
import sys

if os.getuid() != 0:
  print("[!]You must execute as root...")
  import sys.exit()
  
print("@take off")

os.system("rm /usr/local/bin/magician")
os.system("rm /usr/local/bin/magician_banner.py")
os.system("rm /usr/local/bin/magi.py")
os.system("rm /usr/local/bin/armoury.py")

print("Done...................")
