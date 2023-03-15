from usuario import Usuario

class Cliente(Usuario):
    def __init__(self, name, surname, password, rg, id:str, phone_number:str, gender:str):
        super().__init__(name, surname, password, rg)
        self.id = id
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

