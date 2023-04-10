import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from gui.login_screen    import UI_LoginScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = UI_LoginScreen()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())