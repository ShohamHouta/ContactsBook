import sqlite3,pandas as pd
from contact import *

con = sqlite3.connect('contacts.db')
cur = con.cursor()



def create_contact():
    """
    Create new instence of Contact
    """
    Country_Codes = pd.read_csv("PhonesCountryCodes.csv")
    Codex = Country_Codes["COUNTRY CODE"].to_list()
    Countries = Country_Codes["COUNTRY"].to_list()
    region_list = list(zip(Countries,Codex))
    
    print("New Entry:")
    
    name = input("Enter a name:")
    lname = input("Enter last name:")
    address = input("Enter an address:")
    
    while True:
        try:    
            for index,(c, code) in enumerate(region_list):
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
            
    contact = Contact(name,lname,address,phone,email)
    return contact

def main():
    c = create_contact()
    print(c)
    
if __name__ == '__main__':
    main()