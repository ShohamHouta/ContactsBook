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


def Delete():
    data = [row for row in cur.execute("SELECT * FROM contacts")]
    deleted = False
    while True:
        if len(data) >=1:
            for index, row in enumerate(data):
                print(f"{index} : {row}")
            choice = input("Which Contact do you wish to delete:")
            try:
                choice = int(choice)
                if choice in range(0, len(data)):
                    cur.execute(
                        f"DELETE FROM Contacts WHERE name='{row[0]}' AND last='{row[1]}' and address='{row[2]}' AND phone='{row[3]}'")
                    con.commit()
                    deleted = True
                break
            except ValueError:
                print("Contact not exists!")
        else:
            print("Contacts book is empty!")
            break
    return deleted

def Update():
    pass


def Search(contact: Contact):
    pass


def Menu():
    while True:
        os.system("clear")
        print("""================================================================
                        : CLI CONTACT BOOK :
================================================================

    [1] Add New Contact.
    [2] Remove Contact.
    [3] Edit Contact.
    [4] Search Contact.
    [0] Quit
    """)
        choice = input("1-4,0>")
        try:
            choice = int(choice)
            break
        except ValueError:
            print("Option not found!")
            sleep(2)
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
                    break
            case 3:
                Update()
            case 0:
                break


if __name__ == '__main__':
    main()
