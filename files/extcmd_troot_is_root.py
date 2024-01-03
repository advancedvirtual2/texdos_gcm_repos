class extcmd_handler_main:
    td=None
    def rename_troot(self, payload_):
            td=payload_.get('system')
            root=None
            troot=None
            for i in td.externalCommands :
                if i.get('name') == 'root':
                    print("\"root\" command is already exists")
                    return
                if i.get('name') == 'troot':
                    troot=i
            if troot == None: print("\"troot\" command is not found!"); return 
            else:
                troot['name']='root'
                troot['neededSelf']=True ###f']=TY ## #
    def __init__(self, __td__):
        self.td=__td__
        self.td.Events.AfterInit.append(self.rename_troot)
    commands=[]