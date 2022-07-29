import mysql.connector

try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="CRIT",
      password="password",
    )
except:
    print("There was an error connecting to MySQL Sever")

def DatabaseQuery(Command):
    mycursor = mydb.cursor()
    return mycursor.execute(Command)

#print(DatabaseQuery("CREATE DATABASE CRIT"))

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
