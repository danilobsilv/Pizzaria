from models.item import Item
from models.cliente import Cliente

class Pedido:
      def __init__(self, client:object, data):
            self.id = id
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


if __name__ == "__main__":
      danilo = Cliente("dan","brun","12345","098","12324","32189","mas")
      coca = Item("coca-cola", 12.50)
      pizza = Item("pizza", 25)

      pedido1 = Pedido(danilo, "12/03")
      pedido1.pushItemInList(coca)
      pedido1.pushItemInList(pizza)
      pedido1.setValue()
      pedido1.getValue()


