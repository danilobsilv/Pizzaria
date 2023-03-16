from usuario import Usuario
from datetime import date

class Funcionario(Usuario):
    
    def __init__(self, name, surname, password, rg, id:str, salary:float, hiring_date:date):
        super().__init__(name, surname, password, rg)
        self.id = id
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


oi = Funcionario("danilo","bruno","12345","2976346-0", "09821", "100000", "kkk")

print(oi.checkRg())
oi.checkFuncionario()