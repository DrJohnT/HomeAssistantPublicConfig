# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
import shutil
import glob
import os

def mkdir(dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)

target_dir = "../HomeAssistantPublicConfig/config/"

# top level folder
dst = target_dir
mkdir(dst)
for file in glob.glob("./*.yaml"):
    if (file != ".\\secrets.yaml" and file != ".\\known_devices.yaml" and file != ".\\device_tracker.yaml"):
      shutil.copy(file,  dst)

# packages
dst = target_dir + "/packages"
mkdir(dst)
copytree('./packages', dst)

# lovelace
dst = target_dir + "/.storage"
mkdir(dst)
for file in glob.glob("./.storage/lovelace*"):
    shutil.copy(file,  dst)

# copy soft_ui theme
dst = target_dir + "/themes/soft_ui"
copytree('./themes/soft_ui', dst)

dst = target_dir + "/nas710"
mkdir(dst)
shutil.copy(".\\nas710\\install_ssh_keypair.sh",  dst)



