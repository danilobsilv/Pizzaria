import json
from models.cliente import Cliente
from models.invalid import Invalid
import jsons

class Serializer:
      def __init__(self):
            self.file_name_client = "mps_pizzaria\jsons\_client.json"
            self.file_name_functionary = "mps_pizzaria\jsons\_funcionary.json"
            self.file_name_item_menu = "mps_pizzaria\jsons\_itemMenu.json"
            self.file_name_stock = "mps_pizzaria\jsons\_stock.json"
            

      def serializeClient(self, client:object):
            
            data = {}
            with open(self.file_name_client, "r") as outfile:
                  try:
                        data = json.load(outfile)
                  except:
                        raise Invalid("ERRO")
                         

                  dictionary = {"name":client.name, "password":client.password, "rg":client.rg, "phone number":client.phone_number, "gender":client.gender}
                  data[client.id] = dictionary
                  
                  with open(self.file_name_client, "w") as outfile:
                        json.dump(data, outfile, indent=4)             

      
      def serializeFunctionary(self, functionary:object):
            data = {}
            with open(self.file_name_functionary, "r") as outfile:
                  try:
                        data = json.load(outfile)
                  except:
                        raise Invalid("ERRO")
                  
                  dictionary = {"name": functionary.name, "password":functionary.password, "rg":functionary.rg, "salary":functionary.salary, "hiring date": functionary.hiring_date}
                  data[functionary.id] = dictionary

                  with open(self.file_name_functionary, "w") as outfile:
                        json.dump(data, outfile, indent=4)
                        

      def serializeItem(self, item):
            data = {}
            with open(self.file_name_stock, "r") as outfile:
                  try:
                        data = json.load(outfile)
                  except:
                        raise Invalid("ERRO")
                  
                  dictionary = {"price": item.price, "amount": item.amount}
                  data[item.product] = dictionary

                  with open(self.file_name_stock, "w") as outfile:
                        json.dump(data, outfile, indent=4)
            