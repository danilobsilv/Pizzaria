from models.invalid import Invalid
import re


class Usuario:
    
    def __init__(self, name:str,  password:str, rg:str, cargo:str):
        self.name = name
        self.password = password
        self.rg = rg
        self.cargo = cargo

    def getName(self):
        return self.name
    
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
    
    def getCargo(self):
        return self.cargo
    
    def setCargo(self, new_cargo):
        self.cargo = new_cargo
            
        