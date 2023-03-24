import json

class LoginScreenController():
      def __init__(self):
            self.functionary_file_path = "mps_pizzaria\jsons\_funcionary.json"
            self.gerente_file_path ="mps_pizzaria\jsons\gerente.json"
            
      def validateFunctionary(self, user_input):
            with open(self.functionary_file_path, "r") as outfile:
                  try:
                        data = json.load(outfile)
                        if user_input in data:
                              return True
                        else:
                              return False
                  except:
                        raise Exception("ERROR")
                  

      def validateGerente(self, user_input):
            with open(self.gerente_file_path, "r") as outfile:
                  try:
                        data = json.load(outfile)
                        if user_input in data:
                              return True
                        else:
                              return False
                  except:
                        raise Exception("ERROR")      