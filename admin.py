print("**********welcome to abc hospital******")

import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%A--%d/%b/%Y,%H:%M:%S")
# y=datetime.datetime.now()
# day=y.strftime("%A")
# date=y.strftime("%d")
# month=y.strftime("%b")
# year=y.strftime("%Y")
# hour=y.strftime("%H")
# minit=y.strftime("%M")
# sec=y.strftime("%S")
# print(f"{day}--{date}/{month}/{year},{hour}:{minit}:{sec}")


import mysql.connector

mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database="hospital_db"
)

mycursor=mydb.cursor()


def main():
    print("enter -- 1 for register for docter")
    print("enter -- 2 for register for patient")
    print("enter -- 3 for exit ")

    user=int(input("enter your choice:--"))
# if try is not worked in condition or contains a error it shows a except concept

    try:
        if user==1:
            docter()
        elif user==2:
            patient()
        elif user==3:
            exit()
        else:
            print("invalid number")

    except:
        print("invalid number please print correct value")

def docter():
    a="insert into docter_dt(id,name,gender,password,email) values (%s,%s,%s,%s,%s)"
    print("welcome to docter registration portal")


    id=int(input("enter your id :--"))
    name=input("enter account user name:--")
    gender=input("enter male or female:--")
    password=input("enter your password :--")
    email=input("enter your mail id:--")
    
    data=(id,name,gender,password,email)
    mycursor.execute(a,data)
    mydb.commit()
    print(f"haii {name} your registration for docter was successfully registered ")

def patient():
    a="insert into patient_dt(id,name,gender,reason,email) values (%s,%s,%s,%s,%s)"
    print("welcome to patient registration portal")

    id=int(input("enter your id :--"))
    name=input("enter your name:--")
    gender=input("enter male or female:--")
    reason=input("enter your reason :--")
    email=input("enter your mail id:--")
    
    data=(id,name,gender,reason,email)
    mycursor.execute(a,data)
    mydb.commit()
    print(f"haii {name} your registration for patient was successfully registered ")

def exit():
    print("thanks for visiting ABC Hospital")

main()
