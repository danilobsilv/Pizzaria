from models.item import Item
from models.cliente import Cliente
from random import randint

class Pedido:
      def __init__(self, client:object, data):
            self.id = randint(1001,9999)
            self.items_list = []
            self.client = client
            self.data = data
            self.status = "não confirmado"
            self.value = 0

      def setValue(self):
            for elem in self.items_list:
                  self.value += elem.price

      def getValue(self):
            print(self.value)
            return self.value

      def pushItemInList(self, item):
            self.items_list.append(item)

      def setStatus(self, new_status):
            self.status = new_status

      def getStatus(self):
            return self.status

      
