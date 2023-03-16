import json
from models.cliente import Cliente
from models.invalid import Invalid
import jsons

class Serializer:
      def __init__(self):
            # self.file_name_client = "mps_pizzaria\jsons\clients.json"
            # self.file_name_functionary = "mps_pizzaria\jsons\osfuncionarios.json"
            # self.counter = 1
            pass
            

      def serializeClient(self, client:object):
            
            data = {}
            with open("mps_pizzaria\jsons\clients.json", "r") as outfile:
                  try:
                        data = json.load(outfile)
                  except:
                        raise Invalid("ERRO")
                         

                  dictionary = {"name":client.name, "password":client.password, "rg":client.rg, "phone number":client.phone_number, "gender":client.gender}
                  data[client.id] = dictionary
                  
                  with open("mps_pizzaria\jsons\clients.json", "w") as outfile:
                        json.dump(data, outfile, indent=4)             

      def serializeFunctionary(self, functionary:object):
            data = {}
            with open("mps_pizzaria\jsons\osfuncionarios.json", "r") as outfile:
                  try:
                        data = json.load(outfile)
                  except:
                        raise Invalid("ERRO")
                  
                  dictionary = {"name": functionary.name, "password":functionary.password, "rg":functionary.rg, "salary":functionary.salary, "hiring date": functionary.hiring_date}
                  data[functionary.id] = dictionary

                  with open("mps_pizzaria\jsons\osfuncionarios.json", "w") as outfile:
                        json.dump(data, outfile, indent=4)
                        