class Item:
      
      def __init__(self, product:str, price:float):
            self.product = product
            self.price = price

      def getProduct(self):
            return self.product 
      
      def setProduct(self, new_product):
            self.product = new_product

      def getPrice(self):
            return self.price
      
      def setPrice(self, new_price):
            self.price = new_price

      