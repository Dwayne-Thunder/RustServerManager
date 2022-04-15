import ctypes
import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE
import os
from os.path import exists

home = f'"{os.getcwd()}"'
homep = os.getcwd().replace("\\", "/")

steam = 'addons\\steam\\steamcmd.exe'
curl = 'addons\\curl\\curl.exe'
zip = 'addons\\7zip\\7za.exe'
server = 'RustDedicated.exe'

def main():
    work()

def work():
    # Create rust_data directory
    
    if not os.path.isdir(f'{home}/rust_data'):
        os.path.join(home, 'rust_data\RustDedicated_Data\Managed')
        
    # Check for steam server update

    print("Updating Server..")

    subprocess.call(f'{steam} +force_install_dir "{homep}/rust_data" +login anonymous +app_update 258550 +quit', shell=False)

    # Install oxide

    print("Updating Oxide..")

    subprocess.call(f'{curl} -SL -A "Mozilla/5.0" "https://umod.org/games/rust/download" --output "{homep}/rust_data/oxidemod.zip"', shell=False)
    subprocess.call(f'{zip} x "{homep}/rust_data\oxidemod.zip" -o"{homep}/rust_data/" -y', shell=False)
    
    # Windows broken cannot delete file
    #os.remove(f'"{homep}/rust_data/oxidemod.zip"')

    # Install RustEdit

    print("Updating RustEdit..")

    subprocess.call(f'{curl} -SL -A "Mozilla/5.0" "https://github.com/k1lly0u/Oxide.Ext.RustEdit/raw/master/Oxide.Ext.RustEdit.dll" --output "{homep}/rust_data\RustDedicated_Data\Managed\Oxide.Ext.RustEdit.dll"', shell=False)

    # Start Server

    print("Starting server..")

    os.chdir(home.replace('"', "") + '/rust_data')

    generateStartupBatchFile()
    startServer()
    
    # Reboot
    
    #main()

def getConfiguration():
    # Check if config exists / create
    if not exists(f'{homep}/rust_data/config.cfg'):
        print("Generating new configuration file..\n")
        C = ["-server.port 28015\n","-app.port 28016"]
        conf = open(f'{homep}/rust_data/config.cfg', 'w')
        conf.writelines(C)
        conf.close()
    
    conf = ""
    
    confFile = open(f'{homep}/rust_data/config.cfg', 'r')
    Lines = confFile.readlines()
    
    for line in Lines:
        conf += line.replace('\n', ' ')
    
    return conf

def generateStartupBatchFile():
        print("Generating startup.bat file..\n")
        serverConfig = getConfiguration()
        C = ["@echo off\n", ":START\n", f"RustDedicated.exe -batchmode {serverConfig}\n", "echo Restarting..!\n", "clear\n","cd ..\n", "python app.py"]
        conf = open(f'{homep}/rust_data/startup.bat', 'w')
        conf.writelines(C)
        conf.close()

def startServer(): # Start server using startup.bat and wait for it to finish before continuing
    Popen(f'{homep}/rust_data/startup.bat', creationflags=CREATE_NEW_CONSOLE)

main()
