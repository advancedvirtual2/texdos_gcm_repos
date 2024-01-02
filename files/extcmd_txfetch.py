#import art#
from art import *
import platform

class extcmd_handler_main():
    td = None    
           
    def __init__(self, ____td____):
        self.td = ____td____
    def txfetch(self, cwd:str="."):
        system = self.td.sname
        version = self.td.sversion ###ae ## #
        release = platform.release()
        
        # Display ASCII art logo
        logo = text2art(system)
        print(logo)

        # Display system information
        print(f"System: {system}")
        print(f"Release: {release}")
        print(f"Version: {version}")
      
    commands = [
        {"name": "txfetch", 'function': txfetch, 'neededArgs': False, 'description': 'Like a neofetch program.' , 'neededSelf': True}
        ]
