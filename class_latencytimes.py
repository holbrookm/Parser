#!/usr/bin/python

""" This script will access the EMA via http commands with SOAP XML content.
    #Marc Holbrook
    # 0851742253
    # <mholbrook@eircom.ie>
"""


import mysqlcon
from datetime import datetime
time_format = "%Y-%m-%d %H:%M"

class LatencyTimes(object):

    def __init__(self):
        """
        Total calls and latency times of calls per minute
        """
               
        self.date = None
        self.TotalCalls = None
        self.sub50 = None
        self.sub100 = None
        self.sub200 = None
        self.sub300 = None
        self.sub400 = None
        self.sub2000 = None
        self.sub5000 = None
        self.sub8000 = None
        self.plus8000 = None
        self.inDB = False
        
        return
    
    def commitToDatabase(self):
        """ 
        This method should commit the calls to the database.
        """
        my_args = (self.date, self.TotalCalls, self.sub50, self.sub100, self.sub200, self.sub300, self.sub400, self.sub2000, self.sub5000, self.sub8000, self.plus8000)

        insert_row = "INSERT INTO StatLogSCP1 ( date, TotalCalls, sub50, sub100, sub200, sub300, sub400, sub2000, sub5000, sub8000, plus8000) \
                        VALUES ('{0}', '{1}', '{2}','{3}', '{4}', '{5}', '{6}', '{7}','{8}','{9}', '{10}')".format(my_args[0],my_args[1], my_args[2], my_args[3], my_args[4], \
                                                                                              my_args[5], my_args[6], my_args[7], my_args[8], my_args[9], my_args[10])


        try:
            db, cursor = mysqlcon.connectdb()
            cursor.execute(insert_row)
            db.commit()
            print "Commit"
            cursor.close()
            db.close()         
            
        except mysqlcon.Error as error: 
            print error
            
        finally:
            return
        
    def checkInDatabase(self):
        """
        This method should commit the calls to the database.
        """
        my_args = (self.date)

        select_row = "SELECT date from  StatLogSCP1 where date = '{0}:00'".format(my_args)


        try:
            db, cursor = mysqlcon.connectdb()
            cursor.execute(select_row)
            getrow = cursor.fetchone()
            if getrow:
            #date = datetime.strftime(getrow[0], time_format)
                date = getrow[0].strftime(time_format)
                if (date == self.date):
                    self.inDB = True
            cursor.close()
            db.close()

        except mysqlcon.Error as error:
            print error

        finally:
            return


