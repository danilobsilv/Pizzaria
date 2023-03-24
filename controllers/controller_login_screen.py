import json

class LoginScreenController():
         
      def validateFunctionary(self, user_input):
            with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
                  try:
                        data = json.load(outfile)
                        if user_input in data:
                              return True
                        else:
                              return False
                  except:
                        raise Exception("ERROR")
                  

      def validateGerente(self, user_input):
            with open("mps_pizzaria\jsons\gerente.json", "r") as outfile:
                  try:
                        data = json.load(outfile)
                        if user_input in data:
                              return True
                        else:
                              return False
                  except:
                        raise Exception("ERROR")      