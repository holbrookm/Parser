#/usr/bin/python
""" This module is used to set up Logging for the SNMP modules. """

import logging


def getLog(name = 'default log'):
    """ Set up logger functionality"""

    FORMAT = "%(asctime)s %(levelname)s | %(module)s | %(name)s | %(message)s"
    formatter =logging.Formatter(FORMAT)

    handler_s = logging.StreamHandler()
    handler_s.setFormatter(formatter)
    handler_s.setLevel(logging.DEBUG)


    handler_f = logging.FileHandler('nginlatencysnmp.log')
    handler_f.setFormatter (formatter)
    handler_f.setLevel(logging.DEBUG)

    log = logging.getLogger(name)
#    log.addHandler(handler_s)
    log.addHandler(handler_f)
    log.setLevel(logging.DEBUG)

    return log

