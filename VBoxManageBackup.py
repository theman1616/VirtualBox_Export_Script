#This python script is used to backup VirtualBox VMS
#This script only works on windows (Right Now)

#Requirements needed to make the script work

import subprocess
import os
from datetime import date

#Gets the current date to use for the creation of the backup folder.
#Format is Day,Month(Abrev.)Year
d4 = date.today().strftime("%d%b%Y")

#function to ask questions and collect the values Needed
def get_values():
    print("")
    subprocess.run(["VBoxManage.exe", "list", "vms"])
    print("")
    get_values.VMName = input("Which VM do you want to backup? ")
    print("")
    subprocess.run(["wmic", "LOGICALDISK", "LIST", "BRIEF"])
    get_values.DriveDest = input("Letter of drive you want to store backup on: ")
    get_values.VM_BAK_NAME = input("Enter VM backup name: ")
    get_values.VMDest = str(get_values.DriveDest) + ":\VM Backup\\" + str(d4) + str("\\") + str(get_values.VM_BAK_NAME)

#Is called to backup VM after values are collected
def VM_BAK():
    subprocess.run(["VBoxManage.exe", "export", str(get_values.VMName), "--options", "iso", "--ovf10", "--output", str(get_values.VMDest)])

#Makes a backup Directory if one does not exist
def make_directory():
    print("Directory does not exist, creating now")
    os.mkdir(str(get_values.DriveDest) + ":\VM Backup\\" + str(d4))

#Changes directory to the VirtualBox directory so VBoxManage can be called
os.chdir("C:\Program Files\Oracle\VirtualBox")

#Invokes the get_values function
get_values()

#Tests to see if the folder needed for the backup exists
path_test = str(get_values.DriveDest) + ":\VM Backup\\" + str(d4)
ispath = os.path.isdir(path_test)

#Deciding if statement
if ispath == True:
    print("Directory already exists, starting backup")
    VM_BAK()
elif ispath == False:
    make_directory()
    VM_BAK()
else: end
