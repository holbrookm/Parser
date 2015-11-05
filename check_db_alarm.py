#!/usr/bin/python

""" This script will access the DB and check for unusual latency patterns.
    #Marc Holbrook
    # 0851742253
    # <marc.holbrook@eir.ie>
    
"""

import debug
from datetime import timedelta
import logging_config

from dbSetup import StatLogSCP1, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

def connectToDB():
    """
    To connect to the Database create a session and bind with the Db.
    """
    Base = declarative_base()
    engine = create_engine('sqlite:///DBLatency.db', echo=True)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


def getDate(delta):
    """ This function returns the real time minus 3 minute in a format required for the program.
"""
    debug.p("FUNC:check_db_alarm.getDate")
    db = connectToDB()
    debug.p('Get Max Date in DB')
    date_entry = db.query(func.max(StatLogSCP1.date))
    debug.p(date_entry)
    #max_Date = c.fetchone() #This return a tuple, 0 item is a datetime.datetime object
    #maxDate = max_Date[0]
    deltaDate = date_entry - timedelta(minutes= delta)
    debug.p("**Leaving FUNC:check_db_alarm.getDate")
    return deltaDate


def check_latency_stats():
    """
        The inputs for this function should be a duration in minutes which is a window for comparison of stats.
        
    """
    debug.p('FUNC:check_db_alarm.check_latency_stats()    ****')
    try:
        db, c = mysql.connectdb()
        check_date = getDate(11)
        query = 'SELECT date, round((sub50/TotalCalls *100),2) as s50, round((sub100/TotalCalls *100),2) as s100, ' \
                'round((sub200/TotalCalls *100),2) as s200 from StatLogSCP1 where date > \'{0}\''.format(check_date)
        c.execute(query)
        s50 = float(0)
        s100 = float(0)
        s200 = float(0)
        while(True):
            row = c.fetchone()
            if row == None:
                break
            else:
                s50 = s50 + float(row[1])
                s100 += float(row[2])
                s200 += float(row[3])

        #return s50, s100, s200
    
    except Exception, e:
        applog = logging_setup.getLog("NGIN LATENCY SNMP")
        applog.critical('An exception has occurred in check_db_alarm.check_latency_stats' )
        s50 = float(0)
        s100 = float(0)
        s200 = float(0)

    finally:
        debug.p('** Leaving FUNC:check_db_alarm.check_latency_stats()    ****')
        return s50/11, s100/11, s200/11

        