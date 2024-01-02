from colorama import Style as S
from colorama import Fore as F ###FR###
_FR__=F.RED
_SRA_=S.RESET_ALL
_SB__=S.BRIGHT

import os
###

class extcmd_handler_main():
    td = None    
           
    def __init__(self, ____td____):
        self.td = ____td____
    def cat(cwd:str=".", args:list=[]):
      if len(args)==0:
          print(_FR__+_SB__+"Usage: \"cat <file_name> ...\"."+_SRA_)
          return
      for i in args:
        path=None
        if not i.startswith("/"):#os.path.join(".",i) self, #+i
          path=os.path.join(cwd,i)
        else:
          path=os.path.join(".",i)
        with open(path, 'r') as fr:
          print(fr.read())
      print("\n") ###".")    
        #if not i.startswith("/"):
        #  path=cwd+args
      
    commands = [
        {"name": "cat", 'function': cat, 'neededArgs': True, 'description': 'Like a Linux "cat" command, print all contents of all files in arguments...'} ###"} ###) ###commandsfor\"linux
         ]
