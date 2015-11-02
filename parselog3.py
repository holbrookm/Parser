#!/usr/bin/python
import os

filename = 'statistics.log'

i = 0
with open(filename,'rw') as log_file:
    for line in log_file:
        print line
        i += 1
        print i
        if line.endswith('Dumping counters:'):
            entryDate = line.split(' ')[0]
            entryTime = line.split(' ')[1]
            print entryDate, entryTime
            i = 0
        if i == 2000:
            break


    """
            if line.startswith('"TcapProviderManager" TCAP.System Latency:'):
                print line
                #newline = log_file.next()
                print newline
                #break
        #newline = log_file.next()
        #print newline
    """