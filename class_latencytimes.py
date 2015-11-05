#!/usr/bin/python

""" This script will access the EMA via http commands with SOAP XML content.
    #Marc Holbrook
    # 0851742253
    # <mholbrook@eircom.ie> 
"""

import dbSetup
from sqlalchemy.exc import SQLAlchemyError

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

        try:
            new_row = dbSetup.StatLogSCP1(my_args)
            session = dbSetup.initdb()
            session.add(new_row)
            session.commit()

            print "Commit"

        except SQLAlchemyError as error:
            print error
        finally:
            return
        
    def checkInDatabase(self):
        """
        This method should commit the calls to the database.
        """
        my_args = (self.date)
        
        try:
            new_row = dbSetup.StatLogSCP1(my_args)
            session = dbSetup.initdb()
            getrow = session.query(dbSetup.StatLogSCP1).filter(dbSetup.StatLogSCP1.date == my_args).one()

            if getrow.date:
            #date = datetime.strftime(getrow[0], time_format)
                date = getrow.date.strftime(time_format)
                if (date == self.date):
                    self.inDB = True

        except SQLAlchemyError as error:
            print error
            
        finally:
            return


