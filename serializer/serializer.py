import json


class Serializer:
      def __init__(self, file_name):
            self.file_name = file_name
            self.counter = 1
            

      def right_into_json(self, person:object):
            data = {}
            with open(self.file_name, "r") as outfile:
                  try:
                        data = json.load(outfile)
                  except:
                        raise Exception 

                  dictionary = {"Name":person.name, "RG":person.rg,  "ID":person.id, "Counter": self.counter}
                  data[person.rg] = dictionary
                  
                  with open(self.file_name, "w") as outfile:
                        json.dump(data, outfile, indent=4)                        
