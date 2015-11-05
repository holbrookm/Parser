#/usr/bin/python/
""" This file should contain functions need to send SNMP alarms via the trapgen binary program.
This should also contain all the file names of the input files needed for the different applications that may 
send traps.

22/09/2015 : Modified to deal with Latency trap only.

email: marc.holbrook@eir.ie mob: 0851742253
"""

import commands
import debug
import logging_config

applog = logging_config.logger()

def trapgensend ():
    
    debug.p("Func: trapgensend in trapgen.py")
    f_set_fault = 5
    com_path = ". ./send_trap.sh " + str(f_set_fault) + " " + str('A1:latency')
    debug.p(str(com_path))
    p = commands.getoutput (com_path)
    applog.critical('A1:The system Call Latency has failed according to the criteria' ) 
    
    return
    
           

	
def trapgenclear ():
    debug.p("Func: trapgenclear in trapgen.py")
    f_clear_fault = 1
    com_path = ". ./send_trap.sh " + str(f_clear_fault) + " " + str('A1:latency')
    debug.p(str(com_path))
    applog.info('A1:The system Call Latency has returned to accepted service levels' )		
    p = commands.getoutput (com_path)
                   		
    return

def trapgensendapp():
    
    debug.p("Func: trapgensend in trapgen.py")
    f_set_fault = 5
    com_path = ". ./send_trap.sh " + str(f_set_fault) + " " + str('A2:latency')
    debug.p(str(com_path))
    p = commands.getoutput (com_path)
    applog.critical('A2:The system Call Latency SNMP Application has failed according to the criteria.' ) 
    
    return
	
def trapgenclearapp ():
    debug.p("Func: trapgenclear in trapgen.py")
    f_clear_fault = 1
    com_path = ". ./send_trap.sh " + str(f_clear_fault) + " " + str('A2:latency')
    debug.p(str(com_path))
    applog.info('A2:The system Call Latency SNMP Application has returned to accepted service levels' )		
    p = commands.getoutput (com_path)
                   		
    return	
		
