#istalled library mysql-connector-pythyon
import mysql.connector

#creating connection
class insert:   #create class
    def __init__(self):     #init constructor
        self.conn = mysql.connector.connect(    #connection code
                host="localhost",
                user="root",
                password="Ilovemyself@29",
                database="bank"
                )
    def personal_details(self,cid,fname,lname,addr,pn,an,pan):     #function for inserting data in personal details table
        cur=self.conn.cursor()    #creating cursor
        cur.execute(f"insert into personal_details values({cid},'{fname}','{lname}','{addr}',{pn},{an},'{pan}')") #executing the cursor
        self.conn.commit()
        print("--------------------------------personal details has been saved sucessfully!!!---------------------------------")

    def bank_details(self,an,cid,at):
        cur=self.conn.cursor()
        cur.execute(f"insert into bank_details values({an},{cid},'{at}')")
        self.conn.commit()
        print("---------------------------------bank details has been saved sucessfully!!!------------------------------------")
    
    def transaction_details(self,tid,sa,ra,amt,met):
        cur=self.conn.cursor()
        cur.execute(f"insert into transaction_details values({tid},{sa},{ra},{amt},'{met}')")
        self.conn.commit()
        print("---------------------------------transaction details has been saved sucessfully!!!------------------------------")

    def account_details(self,an,tid,amt,closingbal,transtype):
        cur=self.conn.cursor()
        cur.execute(f"insert into account_details values({an},{tid},{amt},{closingbal},'{transtype}')")
        self.conn.commit()
        print("-----------------------------------account details has been saved sucessfully!!!--------------------------------")



