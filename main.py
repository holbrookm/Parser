#!/usr/bin/python
""" This script will hold the MySQL Database setup for the Ngin Statistics Logs DB.
    #Marc Holbrook
    # 0851742253
    # <marc.holbrook@eir.ie>
    
    Modified: 23/9/15 : To include SFTP connect to update statistics.log file.
"""

__author__ = 'holbrookm'

import parselog, check_db_alarm
from time import sleep
from datetime import datetime
import trapgen as trap
import sftp_connect as sftp

def main():
    s50 = float(0)
    s100 = float(0)
    s200 = float(0)
    alarm_sent = False
    app_alarm = False
    while True:
        sftp.sftpconnect(host = '172.30.1.1')
        parselog.startparse()
        print datetime.now()
        s50, s100, s200 = check_db_alarm.check_latency_stats()
        if (s50):
            if (app_alarm): # Check to see if App A2 Alarm has been sent and not cleared
                trap.trapgenclearapp() # Clear
                app_alarm = False # reset App Alarm Flag

            #Test for Alarm Criteria and send trap if True
            if (((s100 > 2) or (s200 > 0.5)) and alarm_sent == False):
                print('send_alarm()')
                trap.trapgensend()
                alarm_sent = True
            #Test for Alarm Criteria and Clear if True
            elif (((s100 < 2) and (s200 < 0.5)) and alarm_sent == True):
                print ('cancel_alarm()')
                trap.trapgenclear()
                alarm_sent = False
            # Test for Alarm Criteria and re-send trap if True
            elif (((s100 > 2) or (s200 > 0.5)) and alarm_sent == True):
                print ('Alarm still active')
                trap.trapgensend()
            else:
                pass
        else:
            if app_alarm == False:
                trap.trapgensendapp()
                app_alarm = True

        sleep(10)

if __name__ == '__main__':
    main()
