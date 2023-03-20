from serializer.serializer import Serializer

class Item:
      
      def __init__(self, product:str, price:float, amount:int):
            self.product = product
            self.price = price
            self.amount = amount

      def getProduct(self):
            return self.product 
      
      def setProduct(self, new_product):
            self.product = new_product

      def getPrice(self):
            return self.price
      
      def setPrice(self, new_price):
            self.price = new_price

      def getAmount(self):
            return self.amount
      
      def setAmount(self, new_amount):
            self.amount = new_amount
      
      def creatItem(self, product, price, amount):
            new_item = Item(product, price, amount)
            serializer = Serializer()
            serializer.serializeItem(new_item)

