import admin
import smtplib

def choice():
    print(" Enter 1. for login docter ")
    print("Enter 2. for login paitent ")

    choose=int(input("enter your catagiery:"))

    if choose==1:
        login_docter()
    elif choose==2:
        login_patient()
    else:
        print("enter right choice")


def login_docter():
# viewing a current account detail

    d=input("Enter column name(id)only:")  #getting column name to idenfy a column
    e = input(f"Enter value in your {d}: ")

    query = f"SELECT * FROM docter_dt WHERE {d} = %s"      #used to perform the datas in data set

    admin.mycursor.execute(query, (e,))           #used to execute particular function
    data = admin.mycursor.fetchall()          # fetchall is used to take every data from a data set

    passcode=input("enter your password : ")

    for row in data: #used to get the pin number
      

        if passcode==row[3]:   #using if condition to check the pin number
            print(f"your password is :{row[3]}")

            admin.mycursor.execute(query, (e,))
            data = admin.mycursor.fetchall()

            for row in data:
                print(f"Your id is {row[0]} and your name is {row[1]}")
                print(f"welcome to abc hospital dr:{row[1]}")

                    # try block is check the code if any error accer except block will work

            try:
                for row in data:
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login("gardennature48@gmail.com", "scpgljwuqfamlrns")  # Replace with your actual password

                    message = "Login successfully"
                    s.sendmail("gardennature48@gmail.com", row[4], message)
                    s.quit()

                print("Emails sent successfully!")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print("Please check your network to receive the email.")


def login_patient():
# patient data

    d=input("Enter column name(id)only:")  #getting column name to idenfy a column
    e = input(f"Enter value in your {d}: ")

    query = f"SELECT * FROM patient_dt WHERE {d} = %s"      #used to perform the datas in data set

    admin.mycursor.execute(query, (e,))           #used to execute particular function
    data = admin.mycursor.fetchall()          # fetchall is used to take every data from a data set

    admin.mycursor.execute(query, (e,))
    data = admin.mycursor.fetchall()


    for row in data:
        s = row[3].split(",")  # Split the symptoms into a list
        
        if "fever" in s and "cough" in s:
            print("You may have COVID-19. Please consult a doctor and isolate yourself.")
        elif "fever" in s and "cough" in s and "cold" in s:
            print("You may have COVID-19. Please consult a doctor.")
        elif "fever" in s or "cold" in s or "cough" in s or "bodypain" in s:
            print(f"It is normal, but please be cautious. Your symptom are: {', '.join(s)}")
        else:
            print(f"Something else. Please wait for a few minutes.")
        
        print(f"Your ID is {row[0]} and your symptoms are: {', '.join(s)}")

choice()
