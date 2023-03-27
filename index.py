import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from gui.login_screen    import UI_LoginScreen


# from serializer.serializer import  Serializer
# from models.item import Item

# serial = Serializer()
# item = Item("calabresa",22.50, 10)
# item1 = Item("coca-cola",10,15)
# serial.serializeItem(item)
# serial.serializeItem(item1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = UI_LoginScreen()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())   

