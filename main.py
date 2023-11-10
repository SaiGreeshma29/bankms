from create import insert
from read import read
from update import update
from delete import delete

obj = insert()
objread = read()
objupdate = update()
objdelete = delete()   

print("------------------------------BANK MANAGEMENT SYSTEM---------------------------------")
print("for inserting the data press 1")
print("for reading the data press 2")
print("for updating the data press 3")
print("for deleting the data press 4")

opr = int(input("please enter your operation: "))

def myopr():
    print("for personal details press 1")
    print("for bank details press 2")
    print("for transaction details press 3")
    print("for account details press 4")
    vr= int(input("please select the table:"))
    if vr==1:
        return 'personal_details'
    elif vr==2:
        return 'bank_details'
    elif vr==3:
        return 'transaction_details'
    elif vr==4:
        return 'account_details'


if opr==1:
    h=myopr()
    if h=='personal_details':
        cid = int(input("enter customer id:"))
        fname=input("enter customer first name:")
        lname=input("enter customer last name:")
        addr=input("enter customer address:")
        pn=int(input("enter customer phnone number:"))
        an=int(input("enter customer aadhar number:"))
        pan=input("enter customer pan number:")
        obj.personal_details(cid,fname,lname,addr,pn,an,pan)

    elif h=='bank_details':
        an=int(input("enter customer account number:"))
        cid=int(input("enter customer id:"))
        at=input("enter account type:")
        obj.bank_details(an,cid,at)
    
    elif h=='transaction_details':
        tid=int(input("enter transaction id:"))
        sa=int(input("enter sender account number:"))
        ra=int(input("enter reciever acccount number:"))
        amt=int(input("enter amount transfered:"))
        met=input("enter method of transaction:")
        obj.transaction_details(tid,sa,ra,amt,met)
    
    elif h=='account_details':
        an=int(input("enter customer account number:"))
        tid=int(input("enter transactionid:"))
        amt=int(input("enter amount:"))
        closingbal=int(input("enter closing balance:"))
        transtype=input("enter transaction type:")
        obj.account_details(an,tid,amt,closingbal,transtype)

if opr==2:
    j = myopr()
    cusid=int(input("please enter customer id for fetching data:"))
    objread.specific_info(cusid,j)

if opr ==3:
    j = myopr()
    cusid = int(input("please enter customer id for fetching data:"))
    colname = input("please enter column name:")
    newval = input("please enter new values:") 
    objupdate.myupdate(j,colname,newval,cusid)

if opr ==4:
    k = myopr()
    cusid = int(input("enter customer id to delete the data:"))
    objdelete.specific_del(k,cusid)