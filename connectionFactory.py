import sqlite3  as sql 

class ConnectionFactory():         
    database  = "PasswordDB.db"  
    conn  = None
    cur   = None    
    connected = False

    def connect(self):
        ConnectionFactory.conn = sql.connect(ConnectionFactory.database) 
        ConnectionFactory.cur  = ConnectionFactory.conn.cursor()        
        ConnectionFactory.connected = True                           
    def disconnect(self):
        ConnectionFactory.conn.close()   
        ConnectionFactory.connected = False   


    def execute(self, sql, parms = None):
        if ConnectionFactory.connected:
            if parms == None: 
                ConnectionFactory.cur.execute(sql) 
            else:                         
                ConnectionFactory.cur.execute(sql,parms)   
            return True           
        return False 

    def persist(self):
        if ConnectionFactory.connected:       
                ConnectionFactory.conn.commit()  
                return True                         
        return False      
    
    def fetchall(self):
        return ConnectionFactory.cur.fetchall()      


def initDB():
    trans = ConnectionFactory()        
    trans.connect()
    trans.execute("""CREATE TABLE IF NOT EXISTS Passwords(
                    ID INTEGER PRIMARY KEY, 
                    Senha TEXT, 
                    Onde TEXT,
                    Data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    Hash BOOL)""")
    trans.persist() 
    trans.disconnect()
initDB()
