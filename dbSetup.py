#!/usr/bin/python
""" This script will hold the MySQL Database setup for the Ngin Statistics Logs DB.
    #Marc Holbrook
    # 0851742253
    # <mholbrook@eircom.ie>
"""
"""
This file is only used to initialise the Database. The class_latency times file will perform the day 
to day database activities.
"""
import os
import logging_config 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DATETIME, Boolean



#engine = create_engine('sqlite:///:memory:', echo=True)  # In memory DB

Base = declarative_base()
logger = logging_config.logger

class StatLogSCP1(Base):
    __tablename__ = 'StatLogSCP1'
    #__table_args__ = {'autoload':True}
    id = Column(Integer, primary_key=True)
    date = Column(DATETIME)
    TotalCalls = Column(Integer)
    sub50 = Column(Integer)
    sub100 = Column(Integer)
    sub200 = Column(Integer)
    sub300 = Column(Integer)
    sub400 = Column(Integer)
    sub2000 = Column(Integer)
    sub5000 = Column(Integer)
    sub8000 = Column(Integer)
    plus8000 = Column(Integer)
    inDB = Column(Boolean)

    def __init__(self, user, password):
        logger.debug('FUNC: dbSetup.StatLogSCP1.__init__()   :')

        logger.debug('**Leaving :: FUNC: ema_db.EmaAccess.__init__()   :')
        return

    def __repr__(self):
        return ("<StatLogSCP1(id='%d', Date='%s', TotalCalls='%d', sub50='%d', sub100='%d', sub200='%d',sub300='%d', sub400='%d', sub2000='%d', sub5000='%d', sub8000='%d', plus8000='%d', inDB='%s')>" % \
        (self.id, self.date, self.TotalCalls,  self.sub50, self.sub100, self.sub200,self.sub300, self.sub400, self.sub2000, self.sub5000, self.sub8000, self.plus8000, self.inDB))

        
def initdb():
    """"""
    logger.debug('FUNC: dbSetup.initdb()   :')

    if os.path.isfile('nginLatency.db'):
        engine = create_engine('sqlite:///DBLatency.db', echo=True)
    else:
        engine = create_engine('sqlite:///DBLatency.db', echo=True)
        db = Base.metadata.create_all(engine)

    Base.metadata.bind = engine
    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    DBSession = sessionmaker()   #Same as Session = sessionmaker(bind=engine)
    DBSession.bind = engine
    session = DBSession()
    logger.debug('**Leaving:: FUNC: dbSetup.initdb()   :')
    return session

        
def main():
    session = initdb()
    return
    
    
if __name__ == '__main__':
    main()
    


    


