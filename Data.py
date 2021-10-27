import sqlite3
class ParMaSys:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS ParkingMS(Place INTEGER PRIMARY KEY,name varchar,carno varchar)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Park(uid INTEGER PRIMARY KEY)")
        self.conn.commit()

    def adduser(self,Place,name,carno):
        self.cur.execute("INSERT INTO ParkingMS VALUES(?,?,?)",(Place,name,carno))
        self.cur.execute("delete from Park where uid = ?",(Place,))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM ParkingMS")
        rows = self.cur.fetchall()
        return rows

    def viewemp(self):
        self.cur.execute("SELECT * FROM Park")
        rows = self.cur.fetchall()
        return rows

    def check(self,no):
        self.cur.execute("SELECT *FROM ParkingMS where Place=?",(no,))
        rows=self.cur.fetchall()
        return rows

    def check1(self,no):
        self.cur.execute("SELECT *FROM Park where uid=?",(no,))
        rows=self.cur.fetchall()
        return rows
    
    def delete(self,uid):
        self.cur.execute("delete from ParkingMS where Place =?",(int(uid),))
        self.cur.execute("INSERT INTO Park VALUES(?)",(int(uid),))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()    
