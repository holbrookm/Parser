#!/usr/bin/python
""" This script will hold the MySQL Database setup for the Ngin Statistics Logs DB.
    #Marc Holbrook
    # 0851742253
    # <mholbrook@eircom.ie>
"""

import mysqlcon


create_table = "CREATE TABLE StatLogSCP1  \
(id INT PRIMARY KEY AUTO_INCREMENT, date DATETIME , TotalCalls INT NOT NULL,  sub50 INT NOT NULL, sub100 INT NOT NULL, sub200 INT NOT NULL \
, sub300 INT NOT NULL, sub400 INT NOT NULL, sub2000 INT NOT NULL, sub5000 INT NOT NULL, sub8000 INT NOT NULL, plus8000 INT NOT NULL)"

show_tables = " SHOW TABLES"


try:
    db, cursor = mysqlcon.connectdb()
    cursor.execute(create_table)
    cursor.execute(show_tables)
    print cursor.fetchone()
    db.commit()
    cursor.close()
    db.close()
    

except mysqlcon.Error as error: 
    print error
    
finally:
    pass
    
def main():
    pass
    
    
if __name__ == '__main__':
    main()
    


