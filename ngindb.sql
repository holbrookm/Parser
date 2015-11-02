# Use this script to create the databse setup for the NGIN Statistics Database
# Marc Holbrook 0851742253
# 14/9/15

CREATE DATABASE nginStatLog;

CREATE USER 'admin'@'localhost' identified by 'admin';

USE nginStatLog;

GRANT ALL ON nginStatLog.* TO 'admin'@'localhost';

CREATE TABLE StatLogSCP1  
id INT PRIMARY KEY AUTO_INCREMENT, date DATETIME , TotalCalls INT NOT NULL,  sub50 INT NOT NULL, sub100 INT NOT NULL, sub200 INT NOT NULL 
, sub300 INT NOT NULL, sub400 INT NOT NULL, sub2000 INT NOT NULL, sub5000 INT NOT NULL, sub8000 INT NOT NULL, plus8000 INT NOT NULL;

CREATE PROCEDURE drop_old_rows ()
BEGIN
    DELETE FROM StatLogSCP! WHERE DATEDIFF(CURDATE(), date) > 90;
END

quit;
