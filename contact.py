import phonenumbers
import re

class InvalidEmail(Exception):
    def __init__(self,email) -> None:
        self.email = email
        self.message = f"{self.email} Is not a valid Email!"
        super().__init__(self.message)

class InvalidPhone(Exception):
    def __init__(self,phone) -> None:
        self.phone = phone
        self.message = f"{self.phone} Is Not a valid phone!"
        super().__init__(self.message)

class InfoChecks():

    def email_check(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
        tmp = re.search(regex,email)
        if tmp:
            return True
        else:
            raise InvalidEmail(email)

    def phone_check(phone):
        number = phonenumbers.parse(phone)    
        if ~phonenumbers.is_possible_number(number):
            raise InvalidPhone(number)
class Contact:
    def __init__(self,name,last,address,phone,email) -> None:
        self.name = name
        self.last = last
        self.address = address
        self.phone = phone
        self.email = email
    
    @property
    def email(self):
        return self.email

    @property
    def address(self):
        return self.address
    
    @property
    def phone(self):
        return self.phone

    @property
    def fullname(self):
        return f"{self.name} {self.last}"

    def __repr__(self) -> str:
        return f"""Full Name:{self.name} {self.last})
        Address:{self.address}
        Phone:{self.phone}
        E-mail:{self.email}"""