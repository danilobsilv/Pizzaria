import json

class LoginController:
    
      def __init__(self):
            # self.screen = screen
            self.functionary_path = "mps_pizzaria\jsons\_funcionary.json"


      def validateFunctionary(self, functionary):
            with open(self.functionary_path, "r") as outfile:
                  data  = json.load(outfile)
                  idf = functionary.getName()
            if idf in data:
                  print("está no json")
            else:
                  print("n está no json")
                  
