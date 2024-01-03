class extcmd_handler_main():    
    
    td = None 
    def __init__(self, ____td____):
        self.td = ____td____    
        
    def renameos(self, cwd:str='.', args:list=[]) :
        if len(args) == 0:
            print('Usage: "renameos <name>"')
            return
        if len(args) >= 1:
            print("Setting name...")    
            self.td.renameOS(args[0], self.td.ctitle) ###setParameter()###
            print("OK!")
            
            print("Searching for \"txfetch\"...") #|")
            txfetch=None
            txfetch_ns=None ###False
            for i in self.td.externalCommands: ###.get("")###
                if i.get("name") == 'txfetch':
                    txfetch=i.get("function")
                    txfetch_ns=i.get("neededSelf", False) ###N")c
                    break
            if txfetch != None:
                print("\"txfetch\" is found, running directly...")
                if txfetch_ns: txfetch(self.td.customCommandsClasses.get("txfetch"), cwd, [])
                else: txfetch(cwd, [])
            else:
                print("\"txfetch\" is not found, ignoring it.")    
            print("OK!")    
            
            ###      R")###
        
    commands = [
        {
            'name': 'renameos',
            'function': renameos,
            'neededArgs': True,
            'description': 'Change system name.',
            'neededSelf': True
        }
    ]       
    
    
    """
    commands = [
        {
            'name': '',
            'function': ,
            'neededArgs': 
            'description': '',
            'neededSelf': True
        }
    ]      """
        