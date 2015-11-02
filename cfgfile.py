from ConfigParser import SafeConfigParser


def importcfgfile():
        global db_url
        global db_username
        global db_password
        global stat_failure_rate
	global stat_timer

        parser = SafeConfigParser()
        parser.read('nginsnmp.ini')
        db_url = parser.get('database', 'url')
        db_username = parser.get('database', 'username')
        db_password = parser.get('database', 'password')
        stat_failure_rate =  parser.getint('stat', 'failure_rate')
        stat_timer =  parser.getint('stat', 'timer')
#        print parser.getint('stat', 'failure_rate')


