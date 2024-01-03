import os
import sys
import traceback
import colorama
from colorama import init as clmainit
from colorama import Fore, Back, Style
from time import sleep as delay



import platform

class texdos():

        isPCFSok = False
        protected_files = []
        toProtect_external_commands = []

        root_passcodes = ['0000']
        
        error_screen=None
        
        

        customCommandsClasses={} #i
        
        def addCommandClass(self, name, ____class____):
            self.customCommandsClasses[name]=____class____
                
        def setRootPasscodes(self, passcodes:list=['0000']):
            self.root_passcodes = passcodes
        
        externalCommands = []
        def makeCommand(self, name:str, function, neededArgs:bool=True, description:str=None):
            """Returns correct external command dictionary for addCommand()
            
            Args:
                name (str): Command name used for running
                function (function): Command handler, function. Required to set first argument (cwd). Recomended to recieve (cwd:str=".", args:list=[]) in function, this will recieve args if this is enabled, else this be empty.
                neededArgs (bool, optional): If True then list of args will send to function arguments, If False, nothing is send to args. Defaults to True.

            Returns:
                dict: Done generated custom external command dictionary.
            """
            
            returns_value = {'name': name, 'function': function, 'neededArgs': neededArgs}
            
            if description != None:
                returns_value['description'] = description 
            
            return returns_value
            
        def addCommand(self, command:dict, silent:bool=True): 
            """Add external command

            Args:
                command (dict): command dictionary, Example: {'name': "example", 'function': example, 'neededArgs': False} (name: command name used for founding it to run, function: command handler def function without brackets "()", neededArgs: If False Nothing wll be send into your function, If True function will recive args:list) If not defined, True by default

            Returns:
                list: List with all added external commands.
            """
            if not silent:
                print(Fore.YELLOW+Style.BRIGHT+f"Registring command \"{command['name']}\"..."+Style.RESET_ALL)
            self.externalCommands.append(command)
            return self.externalCommands
    
        loop_override = None
        enableDefaultMainLoop = False
    
        cwd = "/"
        cmdlinestart = " >>> "
        def __init__(self, cwd:str="/", cmdlinestart:str=" >>> ", loop_override=None, enableDefaultMainLoop:bool=True):
            self.loop_override
            self.enableDefaultMainLoop
            try:
                import system.error as error 
                self.error_screen=error.error(self)
            except ImportError:    
                print("Module \"error\" is not installed...") ###r") ##'")
                ### ## # ### ## ## # # ### ### # ## ### ## ## # # ###
            except Exception as e:
                print(f"Module \"error\" is failed with message:\n\"{str(e)}\"")    
                #self.error_screen=None
            
            
            self.cwd = cwd
            self.cmdlinestart = cmdlinestart
            
            
            self.regCommands()
            if platform.system() == "Windows":   # r
                if float(platform.release()) >= float(10):

                    clmainit()
                else:

                    clmainit(convert=True)  
            else:
                
                  clmainit()      
            
        running:bool = False 
        sname = ""
        ctitle = ""
        sversion = 1.0
        internal_cwd = "."
        if cwd != "/":
            str_r = cwd
            str_r = "./"+str_r[1:len(str_r)]
            internal_cwd = str_r.replace("/",os.sep)
        else:
                      cwd =  "/"
                      internal_cwd = "."
            

        am = "user"
        uname = "user"
        accessmode = ""
        normalusermode_color = Fore.YELLOW
        rootusermode_color = Fore.BLUE
        if am == "user":
            accessmode = f"{normalusermode_color}[{am}]{Style.RESET_ALL}"
        elif am == "root":
            accessmode = f"{rootusermode_color}[{am}]{Style.RESET_ALL}"    
        else:
            accessmode = f"{Fore.RED}[{am}]{Style.RESET_ALL}"    
        cmdline_structure = f"{accessmode} \"{cwd}\" | @{uname} {cmdlinestart}"


        setCmdTitle  = True
        if platform.system() == "Windows":   #####yopur#"S"DR"RED
            #setCmdTitle  = False 
            pass           
        else:                                                                                                                               #'                  '                          #
            setCmdTitle  = False
            print(Fore.YELLOW+Style.BRIGHT+f"[PLATFORM WARNING] "+ Fore.RED+Style.BRIGHT+f"Setting window title is unavalible on your system ({Fore.CYAN}{platform.system()}{Fore.RED})!"+Style.RESET_ALL)    
                            
        clearOnStart = True
        
        
        runinloop = True
        
            
    
        def setParameter(self, parameter:str,value):
            """Sets selected variable to a selected value, and automaticly reloads required variables if it is exists!

            Args:
                parameter (str): Parameter name to change
                value (str,bool): Value you want to set here

            Returns:
                None or bool: If None then incorrect value or parameter, If True then success!
                
            
            Parameter value variants:
                cwd: changes currently selected directory!
                am: access mode, avalible values "user", "root". If You set something other, then prefix will be changed but permissions is used from normal user ("user") mode!
                normalusermode_color: sets a color for normal user mode prefix (Use colorama "Fore", "Back", or "Style")
                rootusermode_color: like previous, but for root user mode prefix color  (Use colorama "Fore", "Back", or "Style")
                accessmode: forces to fully set user acces mode prefix, IT WILL BE RESETTED AFER "am", "rootusermode_color", "normalusermode_color" CHANGE!
                cmdline_structure: Force sets a command-line prefix, IT WILL BE RESETTED AFER "am", "rootusermode_color", "normalusermode_color", "uname" and "cwd" (directory changing) CHANGE!
                setCmdTitle: USE BEFORE "run()"!!! SELECTS IS COMMAND LINE WINDOW TITLE IS CHANGING! IT IS A BOOL!
                clearOnStart: USE BEFORE "run()"!!! SELECTS IS COMMAND LINE WINDOW CONTENT IS CLEARING! IT IS A BOOL!
                uname: Selects a username!
                running: IF False MAIN LOOP WILL BE INTERRUPTED, IT IS AUTOMATICLY SETS TO True WHEN running "run()" (IF "runinloop" IS False THEN BEHAVOUR IS BE LIKE running IS FALSE, IT MEANS THAT MAIN LOOP WILL BE EXITED ALMOST AFTER START (AFTER FIRST ITERATION))!
                runinloop: IF True MAIN LOOP WILL BE RUNNING IN NORMAL MODE, IF False MAIN LOOP WILL BE EXITED AFTER ONE ITERATION, TO MAKE MAIN LOOP FRAME MANUALLY RUN "loop()" (Running it once for one input iteration)!
                loop_override: Sets addonial main loop processor.
                enableDefaultMainLoop: Controls main loop runner starting, If True, Then, Main Loop will be running normally, If False, Then, Only addonial loop handler will be running (Better to use "loop()" at end of it if default loop handler is disabled) 
                cmdlinestart: Sets splitter beetwen console info and inputted command.
            """
            if parameter == "cwd":
                if not isinstance(value, str):
                    return None
                self.cwd = value
                if self.cwd != "/":
                    str_r = self.cwd
                    str_r = "./"+str_r[1:len(str_r)]
                    self.internal_cwd = str_r.replace("/",os.sep)
                    self.ctitle = f"[SYSTEM] {self.sname} {self.sversion} - {self.cwd}"
                    self.cmdline_structure = f"{self.accessmode} \"{self.cwd}\" | @{self.uname} {self.cmdlinestart}"
                    
                    if self.setCmdTitle:
                        #if platform.system() == "Windows":   #####yopur#"S"DR"RED
                        
                        #else:
                        #    print(Fore.YELLOW+Style.BRIGHT+f"[PLATFORM WARNING] "+ Fore.RED+Style.BRIGHT+f"Setting window title is unavalible on your system ('{platform.system()}')!"+Style.RESET_ALL)    
                            os.system(f"title { self.ctitle }")
                        #    else:
                        #    print(Fore.YELLOW+Style.BRIGHT+f"[PLATFORM WARNING] "+ Fore.RED+Style.BRIGHT+f"Setting window title is unavalible on your system ('{platform.system()}')!"+Style.RESET_ALL)    
                else:
                       self.cwd =  "/"
                       self.internal_cwd = "."
                       
                       
                       self.ctitle = f"[SYSTEM] {self.sname} {self.sversion} | {self.cwd}"
                       self.cmdline_structure = f"{self.accessmode} \"{self.cwd}\" | @{self.uname} {self.cmdlinestart}"
                       
                return self.cwd, self.internal_cwd       
                       
            elif parameter == "am":
                    if not isinstance(value, str):
                        return None
                    self.am = value
                    if self.am == "user":
                        self.accessmode = f"{self.normalusermode_color}[{self.am}]{Style.RESET_ALL}"
                    elif self.am == "root":
                        self.accessmode = f"{self.rootusermode_color}[{self.am}]{Style.RESET_ALL}"    
                    else:
                        self.accessmode = f"{Fore.RED}[{self.am}]{Style.RESET_ALL}"    
                    self.cmdline_structure = f"{self.accessmode} \"{self.cwd}\" | @{self.uname} {self.cmdlinestart}" 
                    return True
               
            elif parameter == "normalusermode_color":
                    if not isinstance(value, str):
                        return None
                
                    self.normalusermode_color = value   
                    if self.am == "user":
                        self.accessmode = f"{self.normalusermode_color}[{self.am}]{Style.RESET_ALL}"
                    elif self.am == "root":
                        self.accessmode = f"{self.rootusermode_color}[{self.am}]{Style.RESET_ALL}"    
                    else:
                        self.accessmode = f"{Fore.RED}[{self.am}]{Style.RESET_ALL}"    
                    self.cmdline_structure = f"{self.accessmode} \"{self.cwd}\" | @{self.uname} {self.cmdlinestart}"  
                    return True
            elif parameter == "rootusermode_color":
                    if not isinstance(value, str):
                        return None
                
                    self.rootusermode_color = value 
                    if self.am == "user":
                        self.accessmode = f"{self.normalusermode_color}[{self.am}]{Style.RESET_ALL}"
                    elif self.am == "root":
                        self.accessmode = f"{self.rootusermode_color}[{self.am}]{Style.RESET_ALL}"    
                    else:
                        self.accessmode = f"{Fore.RED}[{self.am}]{Style.RESET_ALL}"    
                    self.cmdline_structure = f"{self.accessmode} \"{self.cwd}\" | @{self.uname} {self.cmdlinestart}"  
                    return True
            elif parameter == "accessmode":
                if not isinstance(value, str):
                    return None
                
                self.accessmode = value 
                
                self.cmdline_structure = f"{self.accessmode} \"{self.cwd}\" | @{self.uname} {self.cmdlinestart}" 
                return True 
                
            elif parameter == "cmdline_structure"  :
                if not isinstance(value, str):
                    return None
                self.cmdline_structure = value 
                return True 
            elif parameter == "setCmdTitle":
                if not isinstance(value, bool):
                    return None
                
                if platform.system() == "Windows":   ###        #    #yopur#"S"DR"RED
                    self.setCmdTitle = value         
                else:
                    print(Fore.YELLOW+Style.BRIGHT+f"[PLATFORM WARNING] "+ Fore.RED+Style.BRIGHT+f"Setting window title is unavalible on your system ('{platform.system()}')!"+Style.RESET_ALL)    
                            
                
                return True 
            elif parameter == "clearOnStart":
                if not isinstance(value, bool):
                    return None
                self.clearOnStart = value 
                return True 
            elif parameter == "uname":
                if not isinstance(value, str):
                    return None
                self.uname = value
                self.cmdline_structure = f"{self.accessmode} \"{self.cwd}\" | @{self.uname} {self.cmdlinestart}" 
                return True 
            elif parameter == "running":
                if not isinstance(value, bool):
                    return None
                self.running = value 
                return True 
            elif parameter == "runinloop":
                if not isinstance(value, bool):
                    return None
                self.runinloop = value  
                return True 
                
                
                
            elif parameter == "loop_override":
                self.loop_override = value
                return True
            elif parameter == "enableDefaultMainLoop":
                if not isinstance(value, bool):
                    return None
                self.enableDefaultMainLoop = value
                return True
            elif parameter == "cmdlinestart":
                if not isinstance(value, str):
                    return None
                self.cmdlinestart = value
                self.cmdline_structure = f"{self.accessmode} \"{self.cwd}\" | @{self.uname} {self.cmdlinestart}" 
                return True
            else:
                return None  
                
        def renameOS(self, sys_name:str = sname, cmd_title:str=None, sys_version:float=sversion):
            """Changes system name, version. Or force change cmd title.

            Args:
                sys_name (str, optional): System name shown in command line title, if it is enabled. (if ignored, then, it will be keep old value). Defaults to sname.
                cmd_title (str, optional): Forcing to set command line title, if it is enabled. (if ignored, then, it will be automaticly constructed from name and version. IT RESETS WHEN "cwd" IS CHANGED. TO KEEP PREVIOUS set it to "ctitle"). Defaults to None.
                sys_version (float, optional): System version shown in command line title, if it is enabled. (if ignored, then, it will be keep old value). Defaults to sversion.
            """
            self.sname = sys_name
            if cmd_title == None:
                self.ctitle = f"[SYSTEM] {sys_name} {sys_version} - \"{self.cwd}\""
            else:
                self.ctitle = cmd_title
            self.sversion = sys_version
            if self.setCmdTitle:
                self.ctitle = self.ctitle.replace("/", "\\")
                os.system(f"title { self.ctitle }")        
         
        def runMainLoop(self):
            """
            
            
            Running main loop without performing required settings.
            
            
            """
            
            
            if self.runinloop:
                
                while self.running:
                   
                    if self.enableDefaultMainLoop:    
                        self.loop()
                    if self.loop_override != None:
                        self.loop_override()    
                    
            else:
                if self.enableDefaultMainLoop:    
                        self.loop()  
                if self.loop_override != None:
                    self.loop_override()        
            return True
                
        def init(self):
            """Performs default settings but don't start main loop.

            Returns:
                bool: if command passed to 100% it will return True
            """
            
            self.enableDefaultMainLoop = True
            
            sys_name:str = "TXDOS"
            cmd_title:str=None
            sys_version:float=1.0
            
            self.sname = sys_name
            
            if cmd_title == None:
                self.ctitle = f"[SYSTEM] {sys_name} {sys_version} - \"{self.cwd}\""
            else:
                self.ctitle = cmd_title
            self.sversion = sys_version
            
            if platform.system() == "Windows":  
                if float(platform.release()) >= float(10):

                    clmainit()
                else:

                    clmainit(convert=True)
            else:
                clmainit()            
            self.running = True
            if self.setCmdTitle:
                os.system(f"title { self.ctitle }")
            if self.clearOnStart:
                if platform.system() == "Windows":
                    os.system(f"CLS")
                else:
                    os.system(f"clear")    
                  
            
            return True        
                
        def run(self, sys_name:str = "TXDOS", cmd_title:str=None, sys_version:float=1.0):
            """Starts main loop and performs default settings."""
            
            
            self.enableDefaultMainLoop = True
            
            self.sname = sys_name
            if cmd_title == None:
                self.ctitle = f"[SYSTEM] {sys_name} {sys_version} - \"{self.cwd}\""
            else:
                self.ctitle = cmd_title
            self.sversion = sys_version
            
            if platform.system() == "Windows":
                if float(platform.release()) >= float(10):

                    clmainit()
                else:

                    clmainit(convert=True)  
            else:    
                clmainit()      
                
            self.running = True
            if self.setCmdTitle:
                os.system(f"title { self.ctitle }")
            if self.clearOnStart:
                if platform.system() == "Windows":
                    os.system(f"CLS")
                else:
                    os.system(f"clear") 
             
            if self.runinloop:
                
                while self.running:
                    if self.enableDefaultMainLoop:    
                        self.loop()
                    if self.loop_override != None:
                        self.loop_override()    
            else:
                if self.enableDefaultMainLoop:    
                        self.loop()  
                if self.loop_override != None:
                    self.loop_override()        
            return True

        running_instance:run = None

        def get(self, variable_name:str="running"):
            if variable_name == "running":
                return self.running
            else:
                return None
        def parseCmdArgs(self, command:str):
            """Splits command base and arguments.

            Args:
                command (str): raw command string combined with args

            Returns:
                tuple[str, list]: multiple variables, command base and argument list (Usage example: "command, args = parseCmdArgs(...)")
                    first value: command base
                    second value: arguments list
            """
            splits_i = []
            splits_o = []
            isBracket = False
            temp_str = ""
            bcix = []
            chrqi = 0
            i = 0
            ii = 0
            
            q = " ".join(command.split(" ")[1:len(command.split(" "))])
            
            for chr_ in q:

                if chr_ == "\"":
                    chrqi = i
                    isBracket = not isBracket
                    if not isBracket:
                        splits_i.append(temp_str)
                        temp_str = ""
                else:
                    if not isBracket:
                        if chr_ != " ":
                            temp_str += chr_
                        else:
                            splits_i.append(temp_str)
                            temp_str = ""
                                
                    else:    
                        temp_str += chr_ 
                
                if i == len(q)-1:
                            splits_i.append(temp_str)
                            temp_str = ""
                    
                        
                i +=1   
                
            return command.split(" ")[0], splits_i

        cmdenable = {'testargs': True}

        def setUname(self, cwd:str=".", args:list=[]):
            """SetName Command Handler.

            Args:
                cwd (str, optional): recieves current selected directory. Defaults to ".".
                args (list, optional): recieves arguments. Defaults to [].
            """
            if len(args) > 0:
                self.setParameter('uname', args[0])    
                with open(".\\system\\username.txt".replace("\\", os.sep), "w") as f:
                    f.write (self.uname)
            else:
                print(f"\n@{self.uname}")

        
            
        def runPython(cwd:str=".", args:list=[]):
            if len(args) == 0:
                os.system("python")
            else:
                exec(" ".join(args))    

        def regCommands(self):
            self.addCommand(self.makeCommand('setName', self.setUname, True, "Sets username.")) 
            self.addCommand(self.makeCommand('toggleDebug', self.setDebug, False, "Toggle Debug Mode."))
        
        def loop(self):
            """Main Loop runner

            Returns:
                (str | tuple[str, str] | bool | Any | None): text command response or other command method response
            """
            command = ""
            if platform.system() == "Windows":
                if float(platform.release()) >= float(10):
                    command = input(self.cmdline_structure)
                else:
                    print(self.cmdline_structure, end="")
                    command = input()
            else:
                command = input(self.cmdline_structure)        
            command, args = self.parseCmdArgs(command)
            try:
                return self.processCommand(command, args) 
            except Exception as eei:
                                print(Fore.RED+f"Failed in \"{command}\" command.\n    {eei}"+Style.RESET_ALL)    
                                if self.debug: 
                                    print(Fore.RED+f"\nDebug mode is enabled!\nPrinting traceback...\n\n{traceback.format_exc()}"+Style.RESET_ALL)
                    
                
            
        debug = False
        
        def getFileNameFromUrl(self, url:str):
            url_ = url
            url__ = ""
            for chr_ in url_:
                if chr_ == "?":
                    break
                url__ += chr_
            print(url__)    
            
        
        def setDebug(self,cwd:str="."):
            if self.am == 'root':
               self.debug = not self.debug
               print(f"Debug mode is now: {self.debug}")  
            else:
                 print(Fore.RED+Style.BRIGHT+f"\nYou don't have permission to perform this command! Please get root access!")      
            
        def processCommand(self, command:str="help", args:list=[]):  #, addonial=None
            """Process internal command or found and run external command.

            Args:
                command (str, optional): Command base name. Defaults to "help".
                args (list, optional): Command arguments. Defaults to [].

            Returns:
                (str | tuple[str, str] | bool | Any | None): text command response or other command method response
            """
            
            if command == "testargs":
                if self.cmdenable['testargs']:
                    print("\n",command,args,"\n")
                    return "\n"+command+str(args)+"\n" 
                else:
                    print(Style.BRIGHT,Fore.RED,"\n",command,": command is disabled!","\n",Style.RESET_ALL)    
                    return "\n"+command+": command is disabled!"+"\n"
            elif command == "exit":
                return self.stop() 
            elif command == "reboot":
                return self.reboot()
            elif command == "cd":
                return self.cd(" ".join(args))
            elif command == "help":
                return self.help()
            elif command == "runpython":
                return self.runPython(args) 
            else:
                
                    isExistsInExternalCommands = False
                    externalCommand = None
                    neededArgs = True
                    command_name=None
                    
                    neededSelf=False
                    
                    for a, b in enumerate(self.externalCommands):
                        if b['name'] == command:
                            isExistsInExternalCommands = True
                            externalCommand = b['function']
                            if b['neededArgs'] != None:
                                neededArgs = b['neededArgs']
                            command_name=b['name']    
                            if b.get('neededSelf') == True and self.customCommandsClasses.get(command_name) != None:    
                                neededSelf=True
                            ###command_name=b['name']    ### ## ## # # ### ## # 111
                            break
                    
                    if isExistsInExternalCommands:
                            try:
                                if neededArgs:    
                                    if neededSelf: return externalCommand (self.customCommandsClasses.get(command_name, self), cwd=self.internal_cwd, args=args)
                                    else: return externalCommand (cwd=self.internal_cwd, args=args) #, #self.customCommandsClasses.get(command_name
                                else:
                                    if neededSelf: return externalCommand (self.customCommandsClasses.get(command_name, self), cwd=self.internal_cwd)
                                    else: return externalCommand (cwd=self.internal_cwd)
                            except Exception as eei: 
                               
                                print(Fore.RED+f"Failed in \"{command}\" command.\n    {eei}"+Style.RESET_ALL)    
                                if self.debug: 
                                    print(Fore.RED+f"\nDebug mode is enabled!\nPrinting traceback...\n\n{traceback.format_exc()}"+Style.RESET_ALL)
                    else:    
                        print(Style.BRIGHT,Fore.RED,"\n",command,": command is not found, type \"help\"!","\n",Style.RESET_ALL)
                        return "\n"+command+": is not found, type \"help\"!"+"\n"

        
        
        
        def cd(self, cwd:str="/"):
            """Changes current selected directory.

            Args:
                cwd (str, optional): Path to select. Defaults to "/".

            Returns:
                (tuple[str, str] | bool | None): "setParameter(...)" response or False if directory is not Found.
            """
            
            
            
            if len(cwd) <= 0:
                print(self.cwd)
                return True 
            
            cwd_ = ""
            i = 0
            cwd1 = f"{cwd}"
            if cwd1[0] == "/" or cwd1[0] == "\\":
                pass
            else:
               cwd1 = "/"+cwd1
            rr = 1   
            
            
            if cwd1[len(cwd1)-1] == "/" or cwd1[len(cwd1)-1] == "\\":
                pass
            else:
               cwd1 = cwd1+"/"
               rr+=1
            
            for chr_ in cwd1:
                if i == len(cwd1)-1-rr:
                    cwd_ += chr_.replace(" ", "") 
                else:
                    cwd_ += chr_    
                i += 1
            
            cwd_1 = cwd_.replace("/","\\").replace("\\", os.sep)   ###"   ###
            
            if os.path.exists(f".{cwd_1}"):
                
                return self.setParameter("cwd", cwd_.replace("\\", os.sep))
            
            else:
                
                print(Style.BRIGHT, Fore.RED, "Системе не удается найти указанный путь.", Style.RESET_ALL)
                return False
        ###///#***/*#/*"*/###
        
        def help(self):
            
            """
                Displays help message and commands list.
            """
            external_commands_helps = ""
            for cmd in self.externalCommands:
                if 'description' in cmd:
                    external_commands_helps += f"    \"{cmd['name']}\" - {cmd['description']}\n"
            help_string = f"""
{Style.BRIGHT}{Fore.BLUE}Help for \"{self.sname} {self.sversion}\":
    \"exit\"   - Shut down the system.
    \"reboot\" - Shut down the system and restarts it again.
    \"cd\"     - Change current cwd direcory. (Better to use with quotes)
    \"help\"   - Shows this message.
    \"runpython\" starts a python interpretter or run a code in current environment, early, exists in extended version, now added to basic version. (2024.01.01 03:25)
{external_commands_helps}
{Style.RESET_ALL}"""
            print(help_string)                        
            return help_string

        def reboot(self, exit_code:int=0):
                """Stop and restart code. !!! THIS WILL UNSETUP ALL VARIABLES AND DATAS, THIS IS FULL RESTART OF ENTIRE FILE !!!

                Args:
                    exit_code (int, optional): Exit codes, if 0 then just exits, if other then message about it will be set into the console. Defaults to 0.
                """
                print("Rebooting...")
                sysargv = [f"\"{sysargvs}\"" for sysargvs in sys.argv]
                self.stop(exit_code, silent=True, allowExits=False)
                sa = ""
                for sysrgva in sysargv:
                    sa += f"{sysrgva} "
                os.system(f"{sys.executable} {sa}")
                sys.exit()

        def stop(self, exit_code:int=0, silent:bool=False, allowExits:bool=True):
            """Stops the code. !!! THIS WILL SHUTDOWN YOUR APPLICATION !!!

            Args:
                exit_code (int, optional): Exit codes, if 0 then just exits, if other then message about it will be set into the console. Defaults to 0.
                silent (bool, optional): If TRUE all output will be disabled. Defaults to False.

            Returns:
                bool: Returns "running" parameter after processing this commands, USALLY EQUALS False. (DISABLED DUE PROCESS EXITING)
            """
            if not self.running:
                return False
            if exit_code != 0:
                if not silent:
                    print(Style.BRIGHT + Fore.RED + f"Exited with non-zero exit code!\n Error exit code {exit_code}" + Style.RESET_ALL)
            else:
                if not silent:
                    print("Goodbye!\n")
            self.running = False
            delay(1.895/2) 
            if self.am != 'root':
                if len(self.root_passcodes) > 0:
                    self.processCommand('root', [self.root_passcodes[0], "dontsavestate"])   #, True
            if self.am == 'root':
                self.processCommand('unprotect', ['nowarn'])
            delay(1.895/2) 
            if allowExits:
                sys.exit()
            return self.running
            
#def runPython(cwd:str=".", args:list=[]):
    #if len(args) == 0:
        #os.system("python")
    #else:
        #exec(" ".join(args))                

td = texdos()
                
                
                
            
                
