import json
from utils.cliente import Cliente


class Serializer:
      def __init__(self):
            # self.file_name = file_name
            # self.counter = 1
            pass
            

      def serializeClient(self, client:object):
            file = "clients.json"
            data = {}
            with open(file, "r") as outfile:
                  # try:
                  data = json.load(outfile)
                  # except:
                        
                        # raise f"error --> {Exception}" 

                  dictionary = {"first name":client.first_name, "surname":client.surname,  "password":client.password}
                  data[client.id] = dictionary
                  
                  with open(self.file_name, "w") as outfile:
                        json.dump(data, outfile, indent=4)             


if __name__ == "__main__":
      serial = Serializer()
      cliente = Cliente("danilo","bruno", "1234","423879","123","1233213","male")
      serial.serializeClient(cliente)

      # print(type(cliente))