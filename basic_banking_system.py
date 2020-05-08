import sys
import random
import os 


def landing_page(): 
    try:
        user_input = int(input("\n Input 1 for Staff Login \n Input 2 for to close app: "))
        if user_input == 2:
            closeapp(user_input)
        else:
            stafflogin()
    except ValueError:
        print("This is not a number. Kindly input a number: ")
        landing_page()

def closeapp(user_input):
    print("Thanks for using our internet banking app!")
    sys.exit()

def stafflogin():
    username = input("Kindly enter your username in lowercase only here: ")
    password = input("Kindly type your password in lowercase only here: ")
    a = 'Username:  '
    b = 'password: '
    credentials = a + username + '' + b + password
    c = open('staff.txt')
    txt = c.read()

    if username and password in txt:
        with open ('user_session.txt', 'w+') as user_session:
            user_session.write(credentials)
        login()
    else:
        print('Error! Incorrect credentials. Kindly enter the correct credentials ')
        stafflogin()
                 
def login():
    try:
        print("\n Welcome Staff! ")
        staff_response = int(input(" \n Press 1 to create a new bank account \n Press 2 to check account details \n press 3 to logout: "))
        
        if staff_response == 1:
            account_name = input("Kindly enter your account name: ")
            opening_balance = input("Kindly enter your opening balance: ")
            account_type = input("Kindly enter account type here: ")
            email = input("Enter your email address here: ")
            account_number = "%0.10d" % random.randint(0, 9999999999)
            print("Here is your account number: ", account_number)
            file = open("customer.txt", "a")
            file.write("Account Name: ")
            file.write(account_name)
            file.write(" ")
            file.write("Opening Balance: ")
            file.write(opening_balance)
            file.write(" ")
            file.write("Account Type: ")
            file.write(account_type)
            file.write(" ")
            file.write("email: ")
            file.write(email)
            file.write(" ")
            file.write("Account Number: ")
            file.write(" ")
            file.write(account_number)
            file.write("\n")
            file.close()
            login()
        if staff_response == 2:
            account_digit = input("Enter your generated account number here: ")
            d = open('customer.txt')
            txts = d.read()
            if account_digit in txts:
                print("Here is your account details: ", txts)
                login()
        if staff_response == 3:
            os.remove('user_session.txt')
            landing_page()
    except ValueError:
        print("This is not a number. Kindly input a number. ")
        login()
        
landing_page()



