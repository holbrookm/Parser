#!/usr/bin/python

""" This file should contain functions need to SFTP to the NGIN to retieive the statistics.log file.

23/09/2015 :

email: marc.holbrook@eir.ie mob: 0851742253
"""

import pysftp

wan_eirin12 = '10.146.3.11'
wan_eirin12 = '10.146.3.12'
remote_eirin11 = '172.30.1.1'
remote_eirin12 = '172.30.1.2'
iusername = 'ocfs'
ipassword = 'ocfs'
iprivate_key_pass = 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEAv/zHqtRlnDOE0Z1O3R2lV1m+nrND5Wbbrr+9gTsC7VuGhDHr847uksXFpZqBu2GP47lim0Fvy+P5FMOpV0OSeigkLP1OLvzvFWaUlqoIMEOvcjciuH6iycdLFHMfwzUl07wGQIE85j3W4bdo+KQu4jWmNhfwWOwBwT62ed4bCuk= ocfs@eirin11'

def sftpconnectgetlogfile(host):
    with pysftp.Connection(host, username = iusername, password = ipassword, private_key_pass = iprivate_key_pass) as sftp:
        with sftp.cd('/opt/jnetx/ocfs/HA_Node1.SCP1/slee/log'):
            sftp.get('statistics.log', '.') # Get statistics.log and place in current directory
    return
        


