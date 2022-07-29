import mysql.connector
import sys

## Get the Config Settings
sys.path.insert(1, '../Config/')
from Config.config import *


try:
    mydb = mysql.connector.connect(
      host=GetFromConfiguration("HostName"),
      user=GetFromConfiguration("DB_User_Name"),
      password=GetFromConfiguration("DB_Password"),
    )
except:
    print("There was an error connecting to MySQL Sever")

def DatabaseQuery(Command):
    mycursor = mydb.cursor(buffered=True)
    return mycursor.execute(Command)

## Check if Databases exist:

def CreateDB():
    print("Database CRIT Didn't Exist,Creating DB ")
    try:
        print(DatabaseQuery("CREATE DATABASE CRIT"))
    except:
        print("database Already Existed Creating table")

    print(DatabaseQuery("USE crit"))
    Index_Table = '''CREATE TABLE CRIT (
        SwitchID VARCHAR(10),
        SwitchName VARCHAR(16),
        Created  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        DeviceIP VARCHAR(20),
        RouterIP VARCHAR(20),
        primary key(SwitchName)
    );

    '''
    print(DatabaseQuery(Index_Table))

existing =DatabaseQuery("SHOW DATABASES")
if existing == None or "CRIT" not in existing:
    CreateDB()
else:
    print(DatabaseQuery("USE crit"))
