from models.usuario import Usuario
from datetime import date
from random import randint

class Funcionario(Usuario): #id, salary, float, hiring_date
    def __init__(self, name: str, password: str, rg: str, salary:float, hiring_date:date):
        super().__init__(name, password, rg)
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