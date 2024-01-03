import os
path_prefixes = ".\\".replace("\\", os.sep)

import sys
import time

import importlib

def str_to_class(classname):
    return getattr(sys.modules['__main__'], classname)

if __name__ == "__main__":
    from main import *
    from commands import *
else:
    from system.main import *   
    from system.commands import *
    path_prefixes = ".\\system\\".replace("\\", os.sep)
for command in commands:
    td.addCommand(command)



noregister = []


if os.path.exists(f"{path_prefixes}"):
    cmds = os.listdir(f"{path_prefixes}")
    for cmd in cmds:
        if cmd.endswith(".py") and cmd.startswith("extcmd_"):
            td.toProtect_external_commands.append(f"{path_prefixes[2:]}{cmd}")
            ospathbasename = os.path.basename(cmd)
            lines = ""
            if not os.path.exists(path_prefixes+"safe_extcmds.txt"):
                 with open(path_prefixes+"safe_extcmds.txt", 'w'): pass
            time.sleep(0.950)     
            with open(path_prefixes+"safe_extcmds.txt", 'r') as f:
                lines = f.read()
            if ospathbasename in lines:
                pass
            else:
                addtochecked = ""
                if platform.system() == "Windows":
                    if float(platform.release()) >= float(10):
                        addtochecked = input(Fore.YELLOW+Style.BRIGHT+f"Warning! Found new external command \"{ospathbasename}\". Mark it as safe and register in system? [Y/N/EXIT/ONCE]: "+Style.RESET_ALL)
                    else:
                        print(Fore.YELLOW+Style.BRIGHT+f"Warning! Found new external command \"{ospathbasename}\". Mark it as safe and register in system? [Y/N/EXIT/ONCE]: "+Style.RESET_ALL, end="")    
                        addtochecked = input()
                else:
                    addtochecked = input(Fore.YELLOW+Style.BRIGHT+f"Warning! Found new external command \"{ospathbasename}\". Mark it as safe and register in system? [Y/N/EXIT/ONCE]: "+Style.RESET_ALL)        
                if addtochecked.lower() == "n":
                    noregister.append(ospathbasename)
                elif addtochecked.lower() == "y":
                    with open(path_prefixes+"safe_extcmds.txt", 'a') as f:
                       f.write(ospathbasename+"\n")
                elif addtochecked.lower() == "exit": 
                    print(Fore.CYAN+"cancelling..."+Style.RESET_ALL)
                    sys.exit()
                elif addtochecked.lower() == "once":   
                    print(Fore.CYAN+f"\"{cmd}\" will be loaded once now..."+Style.RESET_ALL)
                else:
                    print(Fore.RED+"Unknown answer!"+Style.RESET_ALL)    
                    print(Fore.CYAN+"cancelling..."+Style.RESET_ALL)
                    
                    sys.exit()
            time.sleep(0.950)     
                



def import_by_path(path:str):
    requests_import_failed = False
    try:
        mod = importlib.import_module(path.replace(os.sep, ".").replace("\\", os.sep)[2:-3])
        return mod
    except ImportError as iee:
        return iee
    except Exception as eei:
        return eei



external_commands_classes = [] 

if os.path.exists(f"{path_prefixes}"):
    cmds = os.listdir(f"{path_prefixes}")
    for cmd in cmds:
        if cmd.endswith(".py") and cmd.startswith("extcmd_"):
            
            qq11 = os.path.basename(cmd) 
            if qq11 in noregister:
                continue
            importname = f"{path_prefixes}{qq11}"
            cls_ = import_by_path(importname)
            if isinstance(cls_, ImportError):
                noregister.append(qq11)
                print(Fore.RED+f"imports failed in \"{qq11}\", this will not be registred!\n    {cls_}"+Style.RESET_ALL)
                continue
            elif isinstance(cls_, Exception):
                noregister.append(qq11)
                print(Fore.RED+f"\"{qq11}\" is failed, this will not be registred!\n    {cls_}"+Style.RESET_ALL)
                continue
            ____cls____ = cls_.extcmd_handler_main(td)
            external_commands_classes.append (____cls____)
            for command in ____cls____.commands:
                td.addCommand(command, silent=False)
                if command.get('neededSelf') == True: td.addCommandClass(command.get("name"), ____cls____)
            

if __name__ == "__main__":
   
        td.run()   
