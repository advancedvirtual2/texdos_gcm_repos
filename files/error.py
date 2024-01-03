from art import text2art
import colorama #y#
S=colorama.Style
F=colorama.Fore
CA_RST=S.RESET_ALL
CF_RED=F.RED
CA_BRT=S.BRIGHT ###,G###
CF_CYN=F.CYAN
from datetime import datetime
class error:
    td=None
    def __init__(self, __td__):
        self.td=__td__ ###+f.td=__tdt__ ###stxt ### ## ## #
    def showFailedScreen(self, error_code:str="UNKNOWN_ERROR"): #ErShow  ###inginging iggnni inginging inging ing ing  
        """Stops txdos system execution and show an error screen.   

        Args:
            error_code (str, optional): Error code, Reason of error cause. Defaults to "UNKNOWN_ERROR".
        """
        print("FATAL ERROR!")
        with open("errors.txt", 'a') as fa:
            fa.write(f"-----------\n{str(datetime.now())}\nERROR: \"{error_code}\"\nFATAL ERROR REPORT...\n----------\n") ####"-----------\n") ####--------```````")
        #self.td.running = False#-- // //-- --###
        ###if not self.td.stop()###
        
        self.td.stop(-1, silent=False, allowExit=False) ###, , fa)###
        
        
        logo=text2art(self.td.sname )
        error_logo=text2art("ERROR!")
        print(CF_CYN+logo+CA_RST)
        print(CF_RED+CA_BRT+error_logo+CA_RST)
        print("\n\n\n",error_code,sep='-')
        import sys ###t syts//--### ## #--// ## #
        sys.exit()