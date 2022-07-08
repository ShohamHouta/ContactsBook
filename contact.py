import phonenumbers
import pandas as pd
import re


class InvalidEmail(Exception):
    def __init__(self, email) -> None:
        self.email = email
        self.message = f"{self.email} Is not a valid Email!"
        super().__init__(self.message)


class InvalidPhone(Exception):
    def __init__(self, phone) -> None:
        self.phone = phone
        self.message = f"{self.phone} Is Not a valid phone!"
        super().__init__(self.message)


class InfoChecks():


    def email_check(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        tmp = re.search(regex, email)
        if tmp:
            return True
        else:
            raise InvalidEmail(email)

    def phone_check(phone):
        Country_Codes = pd.read_csv("PhonesCountryCodes.csv")
        Codex = Country_Codes["COUNTRY CODE"].to_list()
        for code in Codex:
            if code in phone: 
                number = phonenumbers.parse(phone)
        if not phonenumbers.is_possible_number(number):
            raise InvalidPhone(number)


class Contact:
    def __init__(self, name, last, address, phone, email) -> None:
        self.Name = name
        self.Last = last
        self.Address = address
        self.Phone = phone
        self.Email = email

    @property
    def email(self):
        return self.Email

    @property
    def address(self):
        return self.Address

    @property
    def phone(self):
        return self.Phone

    @property
    def fullname(self):
        return f"{self.Name} {self.Last}"

    def __repr__(self) -> str:
        return f"({self.Name} {self.Last},{self.Address},{self.Phone},{self.Email})"
                       