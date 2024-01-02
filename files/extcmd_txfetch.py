from art import *
from colorama import Style as S
from colorama import Fore  as F
import platform

class extcmd_handler_main():
    def safe_list_get (self, l, idx, default):
      try:
        return l[idx]
      except IndexError:
        return default
    td = None    
           
    def __init__(self, ____td____):
        self.td = ____td____
    def txfetch(self, cwd:str=".", args:list=[]):
        system = self.td.sname
        host_system = platform.system() ##y##
        version = self.td.sversion
        release = platform.release()
        #len#False
        # Display ASCII art logo
        logo = text2art(system)
        if "--nocolor" in args or "-n" in args:
            print(logo)
        else:    
            print(S.BRIGHT+F.CYAN+logo+S.RESET_ALL)

        # Display system information
        print(f"System: {system}")
        print(f"Version: {version}")
        print(f"Host System: {host_system} {release}")

        if "--help" in args or "-h" in args: #iiher
            print(f"\n\n---------------\nHelp for \"{self.safe_list_get(self.commands, 0, {}).get('name', 'txfetch')}\":\n--help / -h : show this help message.\n--nocolor / -n : disable colors.\n---------------") 
       
    commands = [
        {"name": "txfetch", 'function': txfetch, 'neededArgs': True, 'description': 'Like a neofetch program.' , 'neededSelf': True}
        ]
