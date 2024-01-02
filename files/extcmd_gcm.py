import colorama, requests, os, time, shutil
S=colorama.Style
F=colorama.Fore
B=colorama.Back
import tqdm, datetime
import TexnikTextTools as ttt
class extcmd_handler_main():    
    
    td = None    
    gcm_dir = None
    cache_directory = None
           
    def __init__(self, ____td____):
        self.td = ____td____
    
    git_base_url_usercontent = "https://raw.githubusercontent.com/{repos_name}/main/{file}"
    
    def get_repos_filelist(self, repos_name:str, replace_sc:bool=False):
        _repos_name_=repos_name
        if replace_sc: _repos_name_=_repos_name_.replace(';', '/', 1)
        r=requests.get(self.git_base_url_usercontent.format(repos_name=_repos_name_, file="file_list.txt"))
        if r.status_code != 200:
            raise Exception(f"Can not download file list of repository: \"{repos_name}\"")
        return r.text 
    
    def list(self, name:str=""):
        if name == "" or name == None:
            with open(os.path.join(self.gcm_dir, "config", "sources.list"), 'r') as fr:
                 d=fr.read()
                 for i in tqdm.tqdm(d.splitlines()):
                     tqdm.tqdm.write(i)
                     repos_name=i
                     fr=open(os.path.join(self.gcm_dir, "cache", f"{repos_name.replace('/', ';')}.txt"), 'r')
                     dsi=fr.read()
                     fr.close()
                     for ii in dsi.splitlines():
                         data=f"{ii.split('|')[0]}=={ii.split('|')[1]}"
                         
                         tqdm.tqdm.write(data)
        else:
            repos_name=name
            fr=open(os.path.join(self.gcm_dir, "cache", f"{repos_name}.txt"), 'r')
            dsi=fr.read()
            fr.close()
            for ii in dsi.splitlines():
                         data=f"{ii.split('|')[0]}=={ii.split('|')[1]}"
                         print(data)
    
    def update_cache(self, name:str=""):
      if name == "" or name == None:
        with open(os.path.join(self.gcm_dir, "config", "sources.list"), 'r') as fr:
          d=fr.read()
          for i in tqdm.tqdm(d.splitlines()):
            tqdm.tqdm.write(i)
            data=self.get_repos_filelist(i, True)  
            repos_name=i
            if os.path.exists(os.path.join(self.gcm_dir, "cache", f"{repos_name.replace('/', ';')}.txt")): shutil.move(os.path.join(self.gcm_dir, "cache", f"{repos_name.replace('/', ';')}.txt"), os.path.join(self.gcm_dir, "cache", f"{repos_name.replace('/', ';')}_{ttt.shttxt(str(datetime.datetime.now()), '_')}.txt"))
            with open(os.path.join(self.gcm_dir, "cache", f"{repos_name.replace('/', ';')}.txt"), 'a') as fa:
                fa.write(data)
      else:
        data=self.get_repos_filelist(name, True)
        repos_name=name
        with open(os.path.join(self.gcm_dir, "cache", f"{repos_name.replace('/', ';')}.txt"), 'a') as fa: 
            fa.write(data)
    
    def install(self, name:str="", noreboot:bool=False):
        if name == '':
            raise Exception("Package name can not be empty!")
        print(f"Searching \"{name}\"...")    
        repos_name=None
        isFound=False
        with open(os.path.join(self.gcm_dir, "config", "sources.list"), 'r') as fr:
                 d=fr.read()
                 for i in tqdm.tqdm(d.splitlines()):
                     if isFound :
                         break
                     tqdm.tqdm.write(i)
                     repos_name=i
                     fr=open(os.path.join(self.gcm_dir, "cache", f"{repos_name.replace('/', ';')}.txt"), 'r')
                     dsi=fr.read()
                     fr.close()
                     for ii in dsi.splitlines():    
                         if ii.split("|")[0] == name:
                             #print(f"Found \"{name}\" in repository: \"{repos_name}\"!") 
                             tqdm.tqdm.write(f"Found \"{name}\" in repository: \"{repos_name}\"!")
                             isFound=True
                             break
        if not isFound:
            raise FileNotFoundError(f"Failed to search for package \"{name}\". Nothing is found. Check package name or update caches and try again.") ##!!!!un") #xception("")                     
        url=self.git_base_url_usercontent.format(repos_name=repos_name, file=f"files/extcmd_{name}.py")
        print(F.YELLOW+f"Downloading file: \"{url}\"..."+S.RESET_ALL)
        r=requests.get(url)
        if r.status_code != 200:
            r.raise_for_status()
        print(F.GREEN+f"Received {len(r.content)} bytes."+S.RESET_ALL)    
        if os.path.exists(os.path.join("system", f"extcmd_{name}.py")): print("Moving old version...") ; shutil.move(os.path.join("system", f"extcmd_{name}.py"), os.path.join("system", f"no_extcmd_{name}_{ttt.shttxt(str(datetime.datetime.now()), '_')}.py")) #verssssss#{}"#isfile    
        print(F.YELLOW+"Writing file..."+S.RESET_ALL)
        with open(os.path.join("system", f"extcmd_{name}.py"), 'ab') as fab:
            bytecount=fab.write(r.content)
        
            print(F.GREEN+f"Written {bytecount} bytes."+S.RESET_ALL)
        print(F.GREEN+S.BRIGHT+"OK!"+S.RESET_ALL)
        time.sleep(0.135)
        if noreboot:
            print(F.YELLOW+"Auto reboot is diabled!\nTo use installed/updated command, please, reboot your system..."+S.RESET_ALL) ###S>) #,ceserupdated
        else:
            print(F.YELLOW+"Rebooting system..."+S.RESET_ALL) ### and cdn###
            print("Running command: \"reboot\"...")
            self.td.processCommand(command='reboot') 
    def safe_list_get (self, l, idx, default):
      try:
        return l[idx]
      except IndexError:
        return default

    def help(self, name:str=""):
        if name != "": print("----\n! \"name\" parameter will be ignored because this command is not accepts this argument !"); print("----\n\n") ###ppscall###
        print(f"{self.safe_list_get(self.commands, 0, {}).get('name', 'gcm').uppercase()} - v{self.safe_list_get(self.commands, 0, {}).get('version', '0.0')}\n") ###?.?')}")
        print(f"Help for command: {self.safe_list_get(self.commands, 0, {}).get('name', 'gcm')}:")    
        print("arguments:" )
        print("--noreboot / -n : Prevent system from rebooting after update/install is complete.")
        print("commands:" )
        print("install / i : install or update a command.") ### (run \"gcm u\", check  before installing if results as error).")
        print("update  / u : reload all package list caches.") ### :o###
        print("list    / l : lists  all packages from package list caches.")
        print("\n\nTo update a package just run \"gcm i <package_name>\"")
    
    def gcm(self, cwd:str=".", args:list=[]):
      name=""
      command=None
      self.gcm_dir=os.path.join(self.td.uname, ".gcm")
      self.cache_directory=os.path.join(self.gcm_dir, "cache")
      if not os.path.isdir (os.path.join(self.gcm_dir, "config"))                : os.makedirs(os.path.join(self.gcm_dir, "config"))
      print(F.YELLOW+"Checking cache..."+S.RESET_ALL, end='', flush=True)
      time.sleep(0.315)
      if not os.path.isdir(self.cache_directory):
        print("\r"+F.RED+"Checking cache..."+S.RESET_ALL)
        time.sleep(0.315) 
        print("Error during cache verification!")
        print("Recovering...")
        print("-------------")
        print("Cache directory is not found, creating...")
        
        os.makedirs(self.cache_directory)
        if not os.path.isfile(os.path.join(self.gcm_dir, "config", "sources.list")):
          print("Writing default settings...")
          with open(os.path.join(self.gcm_dir, "config", "sources.list"), 'a', encoding='utf8') as fa:
              fa.write("advancedvirtual2/texdos_gcm_repos\n")
          print("Updating caches for \"advancedvirtual2/texdos_gcm_repos\"...")
          self.update_cache("advancedvirtual2/texdos_gcm_repos")
        print("Updating caches...")
        self.update_cache()
        print("OK!")
        print("Please, rerun GCM!")
      else:
        print("\r"+F.GREEN+"Checking cache..."+S.RESET_ALL)  
        time.sleep(0.315) 
        print("OK!")
      if len(args)==0:
          raise Exception("No action is selected. Please select action from this list: [u]pdate, [l]ist, [i]nstall...")
      if len(args)>=1:
          command=args[0]
      if len(args)>=2:
          name = args[1]
      if command == 'i' or command == 'install':
          command= self.install
      elif command == 'l' or command == 'list':
          command= self.list
      elif command == 'u' or command == 'update':
          command= self.update_cache
      elif command == 'h' or command == 'help':
          command= self.help 
      if command == self.install: command(name, "--noreboot" in args or "-n" in args)  
      else: command(name)    
      
    commands = [
        {"name": "gcm", 'function': gcm, 'neededArgs': True, 'description': 'Github command manager. (LIKE "APT" IN LINUX OR "WINGET" IN WINDOWS).', 'neededSelf': True, 'version': '1.2'}
    ]  
