#This python script is used to backup VirtualBox VMS
#This script only works on windows (Right Now)

import subprocess
import os
from datetime import date

#Gets the current date to use for the creation of the backup folder.
#Format is Day,Month(Abrev.)Year
def get_date():
    global today
    today = date.today()
    global d4
    d4 = today.strftime("%d%b%Y")

get_date()

#Sets all the needed variables to global and collects the needed values
def get_values():
    print("")
    subprocess.run(["VBoxManage.exe", "list", "vms"])
    global VMName
    print("")
    VMName = input("Which VM do you want to backup? ")
    print("")
    subprocess.run(["wmic", "LOGICALDISK", "LIST", "BRIEF"])
    global DriveDest
    DriveDest = input("Letter of drive you want to store backup on: ")
    global VM_BAK_NAME
    VM_BAK_NAME = input("Enter VM backup name: ")
    global VMDest
    VMDest = str(DriveDest) + ":\VM Backup\\" + str(d4) + str("\\") + str(VM_BAK_NAME)

#Is called to backup VM after values are collected
def VM_BAK():
    subprocess.run(["VBoxManage.exe", "export", str(VMName), "--options", "iso", "--ovf10", "--output", str(VMDest)])

#Makes a backup Directory if one does not exist
def make_directory():
    print("Directory does not exist, creating now")
    os.mkdir(str(DriveDest) + ":\VM Backup\\" + str(d4))

#Changes directory to the VirtualBox directory so VBoxManage can be called
os.chdir("C:\Program Files\Oracle\VirtualBox")

get_values()

#Tests to see if the folder needed for the backup exists
path_test = str(DriveDest) + ":\VM Backup\\" + str(d4)
ispath = os.path.isdir(path_test)

if ispath == True:
    print("Directory already exists, starting backup")
    VM_BAK()
elif ispath == False:
    make_directory()
    VM_BAK()
else: end
