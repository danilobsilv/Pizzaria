# from serializer.serializer import Serializer
# from models.cliente import Cliente
# from models.funcionario import Funcionario
# from models.item import Item
# from controllers.controller_login import LoginController

# from PyQt5 import uic, QtWidgets, QtGui
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from gui.screen_save import Login_Screen
# from 

lista = []
# serial = Serializer()
# # # cliente = Cliente("danilo bruno da silva","12345","89328","1283891231231","male")
# # # lista.append(cliente)
# # # cliente2 = Cliente("miguel","123182371939871","18237917","12739182379817","male")
# # # lista.append(cliente2)

# # # for client in lista:
# # #     serial.serializeClient(client)

# func1 = Funcionario("gerente","123456789","819273","gerente",100.21, "10/05/2050")
# serial.serializerGerente(func1)
# lista.append(func1)
# func2 = Funcionario("funcionario ", "098080","09808098123","funcionário", 109.90,"17/04/2025")
# serial.serializeFunctionary(func2)
# func2.deleteFuncionario(func2)
# lista.append(func2)
# func3 = Funcionario("funcionario 3", "123123", "13123","funcionario", 120.12, "1230913")
# serial.serializeFunctionary(func3)

# for func in lista:
#     serial.serializeFunctionary(func)

# # # item1 = Item("Coca-cola",5.50, 20)
# # # lista.append(item1)
# # # item2 = Item("Pizza calabresa", 22.50, 50)
# # # lista.append(item2)

# # # for elem in lista:
# # #     serial.serializeItem(elem)
    
# # cont = LoginController()
# # cont.validateFunctionary(func1)
# # cont.validateFunctionary(func2)




import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from gui.login_screen    import UI_LoginScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = UI_LoginScreen()
    ui.setupUi(mainWindow)
    mainWindow.show()
    # ui.showCombo()
    sys.exit(app.exec_())

    # app = QApplication([])
    # main_window = QMainWindow()
    # ui = UI_LoginScreen()
    # ui.setupUi(main_window)
    # main_window.show()
    # app.exec_()