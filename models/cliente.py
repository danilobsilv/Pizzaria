from models.usuario import Usuario
from random import randint

class Cliente(Usuario):  #phone number, gender
    
    def __init__(self, name: str, password: str, rg: str, phone_number:str, gender:str):
        super().__init__(name, password, rg)
        self.id = randint(100,999)
        self.phone_number = phone_number
        self.gender = gender

    def getId(self):
        return self.id
    
    def setId(self, new_id):
        self.id = new_id

    def getPhoneNumber(self):
        return self.phone_number
    
    def setPhoneNumber(self, new_phone_number):
        self.phone_number = new_phone_number

    def getGender(self):
        return self.gender
    
    def setGender(self, new_gender):
        self.gender = new_gender

