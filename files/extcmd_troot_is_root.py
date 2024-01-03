class extcmd_handler_main:
    td=None
    def __init__(self, __td__):
        self.td=__td__
        def rename_troot(payload_):
            td=payload_.get('system')
            #payload=payload_.get('payload')
            #td.externalCommands #
            #isFounded=False#
            root=None
            troot=None
            for i in td.externalCommands :
                if i.get('name') == 'root':
                    print("\"root\" command is already exists") ##self, # 
                    return ###extpresent") ###("Root")###
                if i.get('name') == 'troot':
                    troot=i
            if troot == None: print("\"troot\" command is not found!"); return 
            else:
                troot['name']='root'
            ### //--// --#m
        self.td.Events.AfterInit.append(rename_troot)
    commands=[]