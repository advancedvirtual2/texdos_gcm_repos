import os
import shutil
import time
from colorama import Fore, Back, Style

from distutils.dir_util import copy_tree

from datetime import datetime

def mkdir(cwd:str=".", args:list=[]):
    for arg in args:
        if os.path.exists(cwd.replace("/","\\").replace("\\", os.sep)+os.sep+arg):
            print(Fore.RED,Style.BRIGHT,"Path already exists!",Style.RESET_ALL)
        else:           
            os.makedirs(cwd.replace("/","\\").replace("\\", os.sep)+os.sep+arg) 



def move(cwd:str=".", args:list=[]):
    if len(args) >= 2:
        source_file =  cwd+args[0]
        target_file =  cwd+args[1]
        if os.path.exists(source_file):
            if not os.path.exists(target_file):
                time_start = time.time()
                os.rename(source_file, target_file)
                print(f"Moved 1 object successfully.\n   Elapsed time: {round(time.time()-time_start, 2)} seconds.")
            else:
                print(Fore.RED+Style.BRIGHT+f"Target path is already exists!"+Style.RESET_ALL)
        else:
            print(Fore.RED+Style.BRIGHT+f"Source file not found!"+Style.RESET_ALL)    
    
    else:
        print(Fore.YELLOW+Style.BRIGHT+"Usage: \"move {source_file} {target_file}\"."+Style.RESET_ALL)
        



def copy(cwd:str=".", args:list=[]):
    if len(args) >= 2:
        source_file =  cwd+args[0]
        target_file =  cwd+args[1]
        if os.path.exists(source_file):
            if not os.path.exists(target_file):
                totalDir = 0
                totalFiles = 0
                total = 0
                if os.path.isdir(source_file):
                    for base, dirs, files in os.walk(source_file):
                        print(f"\"{base}\"")
                        for directories in dirs:
                            totalDir += 1
                        for Files in files:
                            totalFiles += 1
                    total = totalDir + totalFiles        
                else:
                    total = 1          
                time_start = time.time()
                if os.path.isdir(source_file):
                    copy_tree(source_file, target_file)
                    
                else:    
                    shutil.copy(source_file, target_file)
                print(f"Copied {total} objects successfully.\n   Elapsed time: {round(time.time()-time_start, 2*2)} seconds.")
            else:
                print(Fore.RED+Style.BRIGHT+f"Target path is already exists!"+Style.RESET_ALL)
        else:
            print(Fore.RED+Style.BRIGHT+f"Source file not found!"+Style.RESET_ALL)    
    
    else:
        print(Fore.YELLOW+Style.BRIGHT+"Usage: \"move {source_file} {target_file}\"."+Style.RESET_ALL)
        



def ____dir____(cwd:str=".", args:list=[]):
    if len(args) == 0:
        args = [""] 
    for arg in args:
        dinfo = cwd.replace("/","\\").replace("\\", os.sep)+arg
        
        
        dirinfo = f"""
Contents of directory \"{dinfo}\" :
        """
        for file in os.listdir(dinfo):
            mtime = str(datetime.fromtimestamp(os.path.getmtime(dinfo+os.sep+file))).ljust(8)
            isdir = os.path.isdir(dinfo+os.sep+file)
            if isdir:
                isdir = "<DIR>".ljust(8)
            else:
                isdir = "     "  .ljust(8)
            size = str(os.path.getsize(dinfo+os.sep+file))  .ljust(8)    
            dirinfo += f"\n{mtime} {isdir} {size} {     file.ljust(8)     }"
                        ##
         
        print(dirinfo)    
            



def echo(cwd:str=".", args:list=[]):
    print(" ".join(args))

def datetime_cmd(cwd:str=".", args:list=[]):
    print(datetime.now())


def dellocker_cancle_command_handler(cwd:str="."):
    print(Fore.RED+Style.BRIGHT+f"Command is disabled due an incedent!"+Style.RESET_ALL)
                                                                     # with previous version of \"***OS\"#               # #


def pause_cmd(cwd:str=".", args:list=[]):
    if len(args) == 0:
        input("Press any key to continue...")
    else:
        delay_seconds = 0 
        delay_seconds = int(args[0])
        remaining = delay_seconds
        for i in range(delay_seconds): 
            pre  = ""
            if i != delay_seconds:
                pre =  "\r"
            else:
                pre =    ""    
                #print("\r")\r, end=""
            print(f"{pre}Waiting for {remaining} seconds.", end="")
            time.sleep(1)
            remaining -= 1
        print(f"\rWaiting for 0 seconds.")    
        print("\n") # 
    

commands:list = [
    {'name': 'mkdir', 'function': mkdir, 'neededArgs': True, 'description': 'Creates directory.'},
    {'name': 'dir', 'function': ____dir____, 'neededArgs': True, 'description': 'Shows directory contents.'},
    {'name': 'echo', 'function': echo, 'neededArgs': True, 'description': 'Echo input arguments.'},
    {'name': 'datetime', 'function': datetime_cmd, 'neededArgs': True, 'description': 'Displays current date and time.'},
    {'name': 'move', 'function': move, 'neededArgs': True, 'description': 'Move files or directories.'},
    {'name': 'copy', 'function': copy, 'neededArgs': True, 'description': 'Copy files or directories.'},
    {'name': 'del', 'function': dellocker_cancle_command_handler, 'neededArgs': False, 'description': 'Delete command placeholder.'},
    {'name': 'pause', 'function': pause_cmd, 'neededArgs': True, 'description': 'Pause main loop.'}
    #{'name': '', 'function': , 'neededArgs': True}#
    ]
  