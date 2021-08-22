#This python script is used to backup VirtualBox VMS
#This script only works on windows (Right Now)

import subprocess
import os
from datetime import date

def file_creation():
    pass

def show_menu():
    print ("\nExample menu")
    print ("-----------------")
    print ("1) Backup VMS")
    print ("2) Restore VMS")
    print ("3) Delete VMS")
    print ("Q) Exit\n")

def menu(today_date):
    # while True:
        show_menu()
        choice = input('Enter your choice: ').lower()
        if choice == '1':
            get_values(today_date)
        elif choice == '2':
            file_creation()
        elif choice == 'q':
            exit()

#Sets all the needed variables to global and collects the needed values
def get_values(today_date):
    print("")
    vm_list = subprocess.run(["VBoxManage.exe", "list", "vms"], capture_output=True, text=True)
    vm_output = vm_list.stdout
    vms = []
    for line in vm_output.split("\n"):
        if '"' in line:
            vms.append(line.split('"')[1])

    for i, VM in enumerate(vms):
      print(f"{i}) {VM}")
    print(f"{len(vms) + 1}) All VMs")

    user_input = input("Which VM to back up? ")
    if user_input == len(vms) + 1:
        for VM in vms:
            VM_BAK(VM, today_date)
        else:
            VM_BAK(vms[VM-1])

def test_the_path(DriveDest, today_date):
    path_test = DriveDest + ":\VM Backup\\" + today_date
    if os.path.isdir(path_test):
        print("Directory already exists, starting backup")
    else:
        make_directory(DriveDest, today_date)

#Is called to backup VM after values are collected
def VM_BAK(vm, today_date):
    DriveDest = input("Letter of drive you want to store backup on: ")
    VM_BAK_NAME = input("Enter VM backup name: ")
    VMDest = DriveDest + ":\\VM Backup\\" + today_date + "\\" + VM_BAK_NAME
    test_the_path(VMDest, today_date)
    subprocess.run(["VBoxManage.exe", "export", vm, "--options", "iso", "--ovf10", "--output", VMDest])

#Makes a backup Directory if one does not exist
def make_directory(DriveDest, today_date):
    print("Directory does not exist, creating now")
    os.mkdir(DriveDest + ":\VM Backup\\" + today_date)

#Changes directory to the VirtualBox directory so VBoxManage can be called
os.chdir("C:\Program Files\Oracle\VirtualBox")
#Get the current date to use for the creation of the backup folder.
d4 = date.today().strftime("%d%b%Y")

while True:
    menu(d4)
