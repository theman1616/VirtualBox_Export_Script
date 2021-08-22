### Explanation for the VBoxManage python script
This also includes a version that once completed, would allow you to make a number selection along with being able to select all the vms and loop through the backup script until all the vms have completed a backup. That version is [TestCode.](/Drafts/TestCode.py) I do not have the knowledge to make this work, so I have to use this. Also includes the previous version of this, which sets the variables in the fuctions as global. The [VBoxManage](VBoxManageBackup.py) version has fixed this.

[Previous_Version](https://github.com/theman1616/VirtualBox_Export_Script/tree/main/Drafts/VBoxManage_Backup_Script.py)

[VBoxManage](VBoxManageBackup.py)

[TestCode](https://github.com/theman1616/VirtualBox_Export_Script/blob/main/Drafts/Testcode.py)

### Requirements

* Needed to run commands from cmd
  - `import subprocess`
  - `import os`
* Needed to get the date for later folder creation
  - `from datetime import date`
* Get the current date in DDMonth(Abrev)YYYY
  - `d4 = date.today().strftime("%d%b%Y")`
  - d4 stores the current date for later

### Gettting the values

* Define the function
  - `def get_values():`
* Add tasks to the function
  - Call VBoxManage and list the vms
    - `subprocess.run(["VBoxManage.exe", "list", "vms"])`
  - Ask which vm to Backup
    - `get_values.VMName = input("Which VM do you want to backup? ")`
  - List the drives and ask which one to use
    - `subprocess.run(["wmic", "LOGICALDISK", "LIST", "BRIEF"])`
    - `get_values.DriveDest = input("Letter of drive you want to store backup on: ")`
  - Bring it al together to make the VM destination string
    - `get_values.VMDest = str(get_values.DriveDest) + ":\VM Backup\\" + str(d4) + str("\\") + str(get_values.VM_BAK_NAME)`

### Define the backup function
* Define the function
  - `def VM_BAK():`
* Add tasks to the function
    - `subprocess.run(["VBoxManage.exe", "export", str(get_values.VMName), "--options", "iso", "--ovf10", "--output", str(get_values.VMDest)])`

### Define the make directory function
* Define the function
  - def make_directory():
* Add tasks to the function
  - Print a message saying the directory does not exist
    - `print("Directory does not exist, creating now")`
  - Create the directory
    - `os.mkdir(str(get_values.DriveDest) + ":\VM Backup\\" + str(d4))`

### Change to the correct directory
* VBoxManage directory
  - Change to the VirtualBox directory
    - `os.chdir("C:\Program Files\Oracle\VirtualBox")`

### Invoke the get_values function
* Invoke the get_values function
  - `get_values`

### Test if the backup directory exists or not
* Define the path to check
  - `path_test = str(get_values.DriveDest) + ":\VM Backup\\" + str(d4)`
* Return a true or false value based on if the directory exists or not
  - `ispath = os.path.isdir(path_test)`

### Invoke the deciding IF statement
* This statement decides what to do based on if the directory exists
  - If directory exists, starts backup
    - `if ispath == True:
        print("Directory already exists, starting backup")
        VM_BAK()`
  - If directory does not exist, creates it and starts backup
    - `elif ispath == False:
        make_directory()
        VM_BAK()
    else: end`
