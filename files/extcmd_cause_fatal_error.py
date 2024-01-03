
class extcmd_handler_main():    
    
    td = None    
    def __init__(self, __td__): ###id__)#extcmd_handler_main## ## ## # # ### ## #
        self.td=__td__
    def cause_fatal_error(self, cwd:str=".")    :
        if self.td.error != None:
            self.td.error.showFailedScreen()
        else:
            self.td.stop(-1)    
            
    commands = [
        {
            'name': 'cause_fatal_error',
            'function': cause_fatal_error,
            'neededArgs': False,
            'description': 'Make system exit with non-zero exit code.',
            'neededSelf': True
        }
    ]