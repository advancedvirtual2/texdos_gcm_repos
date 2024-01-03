import os
from colorama import Fore, Style ###, Back, Style ###n

class extcmd_handler_main:
    td=None
    def beforeinit(self, payload):
        td=payload.get("system")        
        self.protect()
        payload_=payload.get("payload")
        if payload_: print(payload_)
        self.protect(td.toProtect_external_commands)
    def __init__(self, __td__): ###d__);_): $$$d)))t)
        self.td=__td__
        self.td.Events.BeforeInit.append(self.beforeinit) ###After
        #protect()
        #
        #protect(td.toProtect_external_commands)
     
    def getProtectedFiles(self, cwd:str="."):
        print(self.protected_files)    
    protected_files = []
    #advancedFiles=[self.]self.
    def protect(self, advancedFiles:list=[]):
        if advancedFiles == []:  
            #print(Fore.YELLOW+Style.BRIGHT+f"Opening protectors for \"main_app.py\" ..."+Style.RESET_ALL)
            #self.protected_files.append(open("main_app.py", 'r'))
            print(Fore.YELLOW+Style.BRIGHT+f"Opening protectors for \"system\\__init__.py\" ..."+Style.RESET_ALL)
            self.protected_files.append(open("system\\__init__.py".replace("\\", os.sep), 'r'))
            print(Fore.YELLOW+Style.BRIGHT+f"Opening protectors for \"system\\main.py\" ..."+Style.RESET_ALL)
            self.protected_files.append(open("system\\main.py".replace("\\", os.sep), 'r'))
            print(Fore.YELLOW+Style.BRIGHT+f"Opening protectors for \"system\\commands.py\" ..."+Style.RESET_ALL)
            self.protected_files.append(open("system\\commands.py".replace("\\", os.sep), 'r'))
            #print(Fore.YELLOW+Style.BRIGHT+f"Opening protectors for \"dependchecker.py\" ..."+Style.RESET_ALL)
            #self.protected_files.append(open("dependchecker.py", 'r'))
        else:  
            for avfile in advancedFiles:
                print(Fore.YELLOW+Style.BRIGHT+f"Opening protectors for \"{avfile}\" ..."+Style.RESET_ALL)
                self.protected_files.append(open(avfile.replace("\\", os.sep), 'r'))
                #


    def reprotect(self, cwd:str=".",force:bool=False):
        """Restars system files protections.

        Args:
            cwd (str, optional): For TexDOS custom command system. recieves current selected system directory. Defaults to ".".
            force (bool, optional): if True, dont check for root access. Defaults to False.
        """
        if self.td.am == "root" or force: 
            if self.td.isPCFSok:
                print(Fore.YELLOW+Style.BRIGHT+f"Protectors is already ok!\n"+Style.RESET_ALL)
                return
            
            count = 4
            count += len(self.td.toProtect_external_commands)
            
            print(Fore.YELLOW+Style.BRIGHT+f"Reopening protectors for {count} files..."+Style.RESET_ALL)
            self.protect()
            self.protect(self.td.toProtect_external_commands)
            print(Fore.GREEN+Style.BRIGHT+f"Done!"+Style.RESET_ALL)
        else:
            print(Fore.RED+Style.BRIGHT+f"\nYou don't have permission to perform this command! Please get root access!")

    def unprotect(self, cwd:str=".", args:list=[], force:bool=False):
        global protected_files
        if self.td.am == "root" or force:
            for protection_ in self.protected_files:
                print(Fore.YELLOW+Style.BRIGHT+f"Closing protector for \"{protection_.name}\"..."+Style.RESET_ALL)
                protection_.close()
            self.protected_files = []    
            if len(args) > 0:
                if args[0] == "nowarn":   
                    pass
                else:
                        
                    print(Fore.RED+Style.BRIGHT+"\nWarning! All files protections is disabled! System vulnerable for files deletion! Run \"reprotect\" from root!")    
            else:        
                print(Fore.RED+Style.BRIGHT+"\nWarning! All files protections is disabled! System vulnerable for files deletion! Run \"reprotect\" from root!")    
        else:
            print(Fore.RED+Style.BRIGHT+f"\nYou don't have permission to perform this command! Please get root access!")   
        #    

    commands = [
        {'name': 'getProtectedFiles', 'function': getProtectedFiles, 'neededArgs': False, "neededSelf": True},{'name': 'reprotect', 'function': reprotect, 'neededArgs': False , 'description': "Restarts protectors for system files.", "neededSelf": True},{'name': 'unprotect', 'function': unprotect, 'neededArgs': False , 'description': "Shutdowns protectors for system files.", "neededSelf": True}
        #td.makeCommand('reprotect', reprotect, False, "Restarts protectors for system files."),
        #td.makeCommand("unprotect", unprotect, description="Shutdowns protectors for system files.")
    ]
    
#/self./*
#td.addCommand({'name': 'getProtectedFiles', 'function': getProtectedFiles, 'neededArgs': False})
#td.addCommand(td.makeCommand('reprotect', reprotect, False, "Restarts protectors for system files."))
#td.addCommand(td.makeCommand("unprotect", unprotect, description="Shutdowns protectors for system files."))*//