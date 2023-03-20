from models.usuario import Usuario
from random import randint
from serializer.serializer import Serializer
import json

class Funcionario(Usuario): #id, salary, float, hiring_date
    def __init__(self, name: str, password: str, rg: str, cargo, salary:float, hiring_date):
        super().__init__(name, password, rg, cargo)
        self.id = randint(100,999)
        self.salary = salary
        self.hiring_date = hiring_date

    def getId(self):
        return self.id
    
    def setId(self, new_id):
        self.id = new_id

    def getSalary(self):
        return self.salary
    
    def setSalary(self, new_salary):
        self.salary = new_salary

    def getHiringDate(self):
        return self.hiring_date
    
    def checkFuncionario(self):  # esse método vai validar se um funcionário existe ou não, irá validá-lo
        pass
    
    def createFuncionario(self, name, password, rg, cargo, salary, hiring_date):
        new_funcionary = Funcionario(name, password, rg, cargo, salary, hiring_date)
        serializer = Serializer()
        serializer.serializeFunctionary(new_funcionary)

    def deleteFuncionario(self, funcionary):
        try:
            with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
                data = json.load(outfile)
        except:
            raise Exception("ERROR: Could not open the file.")
        
        del data[funcionary]

        with open("mps_pizzaria\jsons\_funcionary.json", "w") as outfile:
            json.dump(data, outfile)


    