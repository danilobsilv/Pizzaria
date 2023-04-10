from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from gui.fazer_pedido_screen import Ui_FazerPedido
from gui.gerente_screen import UI_GerenteScreen


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
                  
      def AbrirProxJan(self):
        user = self.txt_usuario.text()
        cargo = self.combo_cargo.currentText()

        try:
            with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
                json.load(outfile)
        except:
            raise Exception("Failed to load the JSON file")
        
        
        if cargo == "funcionário":
            if self.validateFunctionary(user):
                self.janela = QMainWindow()
                self.wind = Ui_FazerPedido()
                self.wind.setupUi(self.janela)
                self.janela.show()
        elif cargo == "gerente": 
            if self.validateGerente(user):
                self.janela = QMainWindow()
                self.wind = UI_GerenteScreen()
                self.wind.setupUi(self.janela)
                self.janela.show()
            else:
                self.txt_aviso.setText("Usuário Inválido!")