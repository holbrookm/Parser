#!/usr/bin/python

import class_latencytimes


time_format = "%Y-%m-%d %H:%M"

"""
    real_Time = real_Time.strftime (app_time_format)

"""

filename = 'statistics.log'

def parsefile(log_file):
    """ The function will parse the file and loads info into the class.
    """
    c1 = class_latencytimes.LatencyTimes()
    while True:
        newline = log_file.next()

        if newline.endswith('Dumping counters:\n'):
            entryDate = newline.split(' ')[0]
            entryTime = newline.split(' ')[1].split(',')[0][0:-3] #Last [0:-3] removes seconds

            date = (str(entryDate +' ' + entryTime))
            #date1 = datetime.strptime(date, time_format)

            c1.date = date

            c1.checkInDatabase() # If in Database, self.inDB flag is set to True.

            
            # Continue loop parsing here without going back to main loop
            HaveDate = True
            while (HaveDate):
                newline = log_file.next()
                if newline.startswith('"TcapProviderManager" TCAP.System Latency:'):
                    newline = log_file.next()
                    count = int(newline.split(',')[-1].split('=')[-1])

                    c1.TotalCalls = (count)
                    newline = log_file.next()
                    newline = log_file.next()
                    max50 = int(newline.split(' ')[5])

                    c1.sub50 = (max50)
                    newline = log_file.next()
                    max100 = int(newline.split(' ')[4])

                    c1.sub100 = (max100)
                    newline = log_file.next()
                    max200 = int(newline.split(' ')[4])

                    c1.sub200 = (max200)
                    newline = log_file.next()
                    max300 = int(newline.split(' ')[4])

                    c1.sub300 = (max300)
                    newline = log_file.next()
                    max400 = int(newline.split(' ')[4])

                    c1.sub400 = (max400)
                    newline = log_file.next()
                    max2000 = int(newline.split(' ')[4])

                    c1.sub2000 = (max2000)
                    newline = log_file.next()
                    max5000 = int(newline.split(' ')[4])

                    c1.sub5000 = (max5000)
                    newline = log_file.next()
                    max8000 = int(newline.split(' ')[4])

                    c1.sub8000 = (max8000)
                    newline = log_file.next()
                    min8000 = int(newline.split(' ')[3])

                    c1.plus8000 = (min8000)
                    HaveDate = False

                    break
            break
    return c1
    
def startparse():
    """
    This function called from Main will run the parsing activities.
    :return:
    """

    with open(filename, 'rU') as log_file:
        firstminute =  parsefile(log_file)
        while True:
            try:
                secondminute = parsefile(log_file)
                result = class_latencytimes.LatencyTimes()
                result.date = secondminute.date
                result.TotalCalls = secondminute.TotalCalls - firstminute.TotalCalls
                result.sub50 = secondminute.sub50 - firstminute.sub50
                result.sub100 = secondminute.sub100 - firstminute.sub100
                result.sub200 = secondminute.sub200 - firstminute.sub200
                result.sub300 = secondminute.sub300 - firstminute.sub300
                result.sub400 = secondminute.sub400 - firstminute.sub400
                result.sub2000 = secondminute.sub2000 - firstminute.sub2000
                result.sub5000 = secondminute.sub5000 - firstminute.sub5000
                result.sub8000 = secondminute.sub8000 - firstminute.sub8000
                result.plus8000 = secondminute.plus8000 - firstminute.plus8000

                if not (secondminute.inDB):
                    result.commitToDatabase()
                firstminute = secondminute


            except:
                break
        del firstminute
        log_file.close()


