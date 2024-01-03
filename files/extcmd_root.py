import os, time
from colorama import Fore, Style
class extcmd_handler_main():    
    
    td = None #    #
    def __init__(self, ____td____):
        self.td = ____td____    
        self.root_passcodes=self.td.root_passcodes
    root_passcodes=None #[0000]
    def root(self, cwd:str=".", args:list=[]): #, dontSave:bool=False
        if len(args) >= 1:
            if args[0] in self.root_passcodes:
                self.td.setParameter('am', 'root')
                dontSave = False
                if len(args) >= 2:
                    if args[1] == 'dontsavestate':  #r#2# []'']
                        dontSave = True
                if not dontSave:
                    with open(".\\system\\isRootEnabled.txt".replace("\\", os.sep), 'w') as f:
                        f.write(self.td.am)  
            else:
                print(Fore.RED+Style.BRIGHT+f"Wrong passcode!"+Style.RESET_ALL)    
        else:
            if self.td.am == 'root':
                self.td.setParameter('am', 'user')
                #print(td.am)
                dontSave = False
                if len(args) >= 2:
                    if args[1] == 'dontsavestate':  #r#2# []'']"
                        dontSave = True
                if not dontSave:
                    with open(".\\system\\isRootEnabled.txt".replace("\\", os.sep), 'w') as f:
                        f.write(self.td.am)
            else:
                print(Fore.RED+Style.BRIGHT+f"Enter passcode!"+Style.RESET_ALL)    
           
        time.sleep(0.915)   
    commands = [
        {
            'name': 'troot',
            'function': root,
            'neededArgs': True,
            'description': 'Add "troot" command that do same as "root" from extended version.',
            'neededSelf': True
        }
    ]    