import email
import sqlite3
from contact import *

con = sqlite3.connect('contacts.db')
cur = con.cursor()



def add_contact():
    print("Add New Contact:")
    name = input("Enter a name:")
    lname = input("Enter last name:")
    address = input("Enter an address:")
    while True:
        try:    
            phone = input("Enter phone number:")
            InfoChecks.phone_check(phone)
            email = input("Enter email address:")
            InfoChecks.email_check(email)
            break
        except InvalidPhone:
            print("Invalid phone number!")
        except InvalidEmail:
            print("Invalid email address!")
            
    contact = Contact(name,lname,address,phone,email)
    return contact

def main():
    c = add_contact()
    print(c)
    
if __name__ == '__main__':
    main()