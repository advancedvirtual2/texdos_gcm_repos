class extcmd_handler_main:
    td=None
    def hello_message(payload_):
        td=payload_.get('system')
        payload=payload_.get('payload')
        
        print("\nWelcome back!")
    def __init__(self, __td__):
        self.td=__td__
        self.td.Events.AfterInit.append(self.hello_message)
    commands=[]