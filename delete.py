import mysql.connector

class delete:
    def __init__ (self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Ilovemyself@29",
                database = "bank"
                )
        
    def specific_del(self,table_name,cusid):
        cur=self.conn.cursor()
        cur.execute(f"delete from {table_name} where customerid={cusid}")
        self.conn.commit()
        print('---------------------data has been deleted sucessfully---------------------')