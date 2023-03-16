from invalid import Invalid
import re


class Usuario:
    
    def __init__(self, name:str, surname:str,  password:str, rg:str):
        self.name = name
        self.surname = surname
        self.password = password
        self.rg = rg

    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname
    
    def getPassword(self):
        return self.password
    
    def setPassword(self, newPassword):
        self.password = newPassword

    def getRg(self):
        return self.rg

    def checkRg(self):
        check = re.match("^\d{1,8}([A-Z]|[a-z]{1})?-?\d{1,6}$", self.rg)

        try:
            if check: 
                return True
            else: 
                return False
        except Exception:             
            raise Invalid(f"ERROR --> {Exception}")
            
        