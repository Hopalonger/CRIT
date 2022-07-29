## Dictonary of configuration items

Configuration = {
"DB_User_Name": "CRIT",
"DB_Password": "password",
"HostName": "localhost"
}

def GetFromConfiguration(V):
    return Configuration[V]
