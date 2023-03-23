import json

class LoginScreenController():
      def __init__(self) -> None:
            pass
      
      def abrirJanelaFazerPedido(self):
            pass
      
      # def abrirJanelaFazerPedido(self):
      #       from gui.fazer_pedido_screen import Ui_FazerPedido, QMainWindow
      #       from gui.gerente_screen import UI_GerenteScreen, QMainWindow
      #       from gui.login_screen import UI_LoginScreen, QMainWindow
      #       screen = UI_LoginScreen()
      #       # user = screen.txt_usuario.text()
      #       # cargo = screen.combo_cargo.currentText()
      #       # print(screen.txt_usuario)
      #       # try:
      #       #       with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
      #       #             if cargo == "funcionário":
      #       #                   if self.validateFunctionary(user):
      #       #                         self.janela = QMainWindow()
      #       #                         self.wind = Ui_FazerPedido()
      #       #                         self.wind.setupUi(self.janela)
      #       #                         self.janela.show()
      #       #                   else:
      #       #                         self.txt_aviso("Usuário Inválido!")
                  
      #       #             elif cargo == "gerente":
      #       #                   if self.validateGerente:
      #       #                         self.janela = QMainWindow()
      #       #                         self.wind = UI_GerenteScreen()
      #       #                         self.wind.setupUi(self.janela)
      #       #                         self.janela.show()
      #       # except:
      #       #       raise Exception("ERROR")

      #       # if cargo == "funcionário":
      #       #       if self.validateFunctionary(user):
      #       #             self.janela = QMainWindow()
      #       #             self.wind = Ui_FazerPedido()
      #       #             self.wind.setupUi(self.janela)
      #       #             self.janela.show()
      #       #       else:
      #       #             self.txt_aviso("Usuário Inválido!")
                  
      #       # elif cargo == "gerente":
      #       #       if self.validateGerente:
      #       #             self.janela = QMainWindow()
      #       #             self.wind = UI_GerenteScreen()
      #       #             self.wind.setupUi(self.janela)
      #       #             self.janela.show()
         
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