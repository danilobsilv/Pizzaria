import json
from models.cliente import Cliente
from models.invalid import Invalid

class Serializer:
      def __init__(self):
            self.file_name_client = "mps_pizzaria\jsons\_client.json"
            self.file_name_functionary = "mps_pizzaria\jsons\_funcionary.json"
            self.file_name_item_menu = "mps_pizzaria\jsons\_itemMenu.json"
            self.file_name_stock = "mps_pizzaria\jsons\_stock.json"
            self.file_name_gerente = "mps_pizzaria\jsons\gerente.json"
            

      def serializeClient(self, client:object):
            
            data = {}
            with open(self.file_name_client, "r") as outfile:
                  try:
                        data = json.load(outfile)
                  except:
                        raise Invalid("ERRO")
                         

                  dictionary = {"name":client.name, "password":client.password, "rg":client.rg, "phone number":client.phone_number, "gender":client.gender}
                  data[client.name] = dictionary
                  
                  with open(self.file_name_client, "w") as outfile:
                        json.dump(data, outfile, indent=4)             

      
      def serializeFunctionary(self, functionary:object):
            data = {}
            with open(self.file_name_functionary, "r") as outfile:
                  try:
                        data = json.load(outfile)
                  except:
                        raise Invalid("ERRO")
                  
                  dictionary = {"name": functionary.name, "password":functionary.password,"cargo":functionary.cargo, "rg":functionary.rg, "salary":functionary.salary, "hiring date": functionary.hiring_date}
                  data[functionary.name] = dictionary

                  with open(self.file_name_functionary, "w") as outfile:
                        json.dump(data, outfile, indent=4)
      
      def serializerGerente(self, gerente):
            data = {}
            with open(self.file_name_gerente, "r") as outfile:
                  try:
                        data = json.load(outfile)
                  except:
                        raise Invalid("ERRO")
                  
                  dictionary = {"name": gerente.name, "password":gerente.password,"cargo":gerente.cargo, "rg":gerente.rg, "salary":gerente.salary, "hiring date": gerente.hiring_date}
                  data[gerente.name] = dictionary

                  with open(self.file_name_gerente, "w") as outfile:
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
            