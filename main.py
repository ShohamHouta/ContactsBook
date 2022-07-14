import sqlite3
import pandas as pd
import os
from time import sleep

from contact import *

con = sqlite3.connect('contacts.db')
cur = con.cursor()

def Insert(contact: Contact):
    """
    Create new entry in DB for new contact
    """
    cur.execute(
        f"INSERT INTO Contacts VALUES('{contact.firstname}','{contact.lastname}','{contact.address}','{contact.phone}','{contact.email}')")
    con.commit()


def Update():
    data = [row for row in cur.execute("SELECT * FROM contacts")]
    print(len(data))
    while True:
        for index,row in enumerate(data):
            print(f"{index}:{row}")
        choice = input("chose contact to modify:")
        try:
            choice =int(choice)
            if choice >= 0 and choice<= len(data):
                name,last,addr,phone,email = data[choice]
                uquery = """UPDATE Contacts
                            SET name='',last='',address='', phone='',email='' 
                            where name=''"""
            break
        except ValueError:
            print("Invalid choice.")
            break
        except IndexError:
            print("Invalid choice.")
            break
    input("Press any key to continue....")
    


def Delete():
    data = [row for row in cur.execute("SELECT * FROM contacts")]
    deleted = False
    while True:
        if len(data) >=1:
            for index, row in enumerate(data):
                print(f"{index} : {row}")
            choice = input("Which Contact do you wish to delete(press c to cancel):")
            try:
                choice = int(choice)
                if choice in range(0, len(data)):
                    cur.execute(
                        f"DELETE FROM Contacts WHERE name='{row[0]}' AND last='{row[1]}' and address='{row[2]}' AND phone='{row[3]}'")
                    con.commit()
                    deleted = True
                break
            except ValueError:
                if choice == 'c':
                    break
                else:
                    print("Contact not exists!")
                    sleep(2)
        else:
            print("Contacts book is empty!")
            sleep(2)
            break
    return deleted


def Search():
    quary = input("Search a contact:").title()
    data = [row for row in cur.execute("SELECT * FROM contacts")]
    if ' ' in quary:
        contact_name = quary.split(" ")
        for row in data:
            name,last,_,_,_ = row
            if name == contact_name[0] and last == contact_name[1]:
                print(row)
            else:
                print("Contact not found!")    

    elif ' ' not in quary:
        for row in data:
            name,last,_,_,_ = row
            if name == quary or last == quary:
                print(row)
            else:
                print("Contact not found!")    
    input("Press any key to continue....")

def Menu():
    while True:
        os.system("clear")
        print("""================================================================
                        : CLI CONTACT BOOK :
================================================================

    [1] Add New Contact.
    [2] Remove Contact.
    [3] Search Contact.
    [4] Edit Contact.
    [0] Quit
    """)
        choice = input("1-4,0>")
        try:
            choice = int(choice)
            break
        except ValueError:
            print("Option not found!")
            sleep(1)
    return choice


def create_contact():
    """
    Create new instence of Contact
    """
    Country_Codes = pd.read_csv("PhonesCountryCodes.csv")
    Codex = Country_Codes["COUNTRY CODE"].to_list()
    Countries = Country_Codes["COUNTRY"].to_list()
    region_list = list(zip(Countries, Codex))

    print("New Entry:")

    name = input("Enter a name:")
    lname = input("Enter last name:")
    address = input("Enter an address:")

    while True:
        try:
            for index, (c, code) in enumerate(region_list):
                print(f"({index}) {c}:{code}")

            choice = int(input("Chose Your country Code:"))
            country_code = '+'+Codex[choice]
            phone = country_code + input("Enter phone number:")

            InfoChecks.phone_check(phone)

            email = input("Enter email address:")

            InfoChecks.email_check(email)
            break

        except InvalidPhone:
            print("Invalid phone number!")
        except InvalidEmail:
            print("Invalid email address!")

    contact = Contact(name, lname, address, phone, email)
    return contact


def main():
    while True:
        match Menu():
            case 1:
                c = create_contact()
                Insert(c)
            case 2:
                if Delete():
                    print("Action was successfull!")
                    sleep(1)
            case 3:
                Search()
            case 4:
                Update()
            case 0:
                break


if __name__ == '__main__':
    main()
