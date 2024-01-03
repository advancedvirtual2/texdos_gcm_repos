import webbrowser
from colorama import Fore, Style
import requests

class extcmd_handler_main():    
    
    td = None    
        
    def __init__(self, ____td____):
        self.td = ____td____
        
    
    def openurl(cwd:str=".", args:list=[]):    
        if len(args) == 0:
            print('Usage: "openurl <url>"')
            return
        ###print("Opening \"{}\"")###
        webbrowser.open(" ".join(args))
      
    def getHeaders(cwd:str=".", args:list=[]):     
        url_se:str = " ".join(args)
        if not url_se.startswith("http") and len(url_se) > 0:
            url_se = "http://"+url_se
        r = requests.head(url_se)
        
        colored_status_code_r = str(r.status_code)
        if colored_status_code_r.startswith("2"):
            colored_status_code_r = Fore.GREEN+Style.BRIGHT+colored_status_code_r+Style.RESET_ALL
        elif colored_status_code_r.startswith("3"):
            colored_status_code_r = Fore.YELLOW+Style.BRIGHT+colored_status_code_r+Style.RESET_ALL
        elif colored_status_code_r.startswith("4") or  colored_status_code_r.startswith("5"):
            colored_status_code_r = Fore.RED+Style.BRIGHT+colored_status_code_r+Style.RESET_ALL    
        print(Fore.CYAN+Style.BRIGHT+"Response status code: "+colored_status_code_r+"\n\n"+str(r.headers )+Style.RESET_ALL)
        return str(r.status_code)+"\n\n"+str(r.headers )
        
    commands = [
        {'name': 'openurl', 'function': openurl, 'neededArgs': True, 'description': 'Opens a website in web browser.'},
        {'name': 'getHeaders', 'function': getHeaders, 'neededArgs': True, 'description': 'Gets website status code and headers.'}
    ]    