import os
import sys

if os.getuid() != 0:
    print("[!]You should execute as root, say the magic word ")
    sys.exit()
os.system("chmod +x magician.py")
os.system("cp magician.py /usr/local/bin/magician")
os.system("cp magician_banner.py /usr/local/bin/")
os.system("cp magi.py /usr/local/bin/")
os.system("cp armoury.py /usr/local/bin/")

os.system("clear")
print("Done.........")
