from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from controllers.controller_login_screen import LoginScreenController
from gui.fazer_pedido_screen import Ui_FazerPedido
from gui.gerente_screen import UI_GerenteScreen
import json


class UI_LoginScreen(object):
    def __init__(self) -> None:
        self.txt_usuario = ""
        self.txt_combo_cargo = ""

    def setupUi(self, MainWindow):
        login_controller = LoginScreenController
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(621, 575)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 222);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 230, 451, 281))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 222);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_usuario = QLineEdit(self.frame)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(60, 60, 311, 20))
        font = QFont()
        font.setPointSize(11)
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet(u"color: rgb(37, 34, 51)")
        self.txt_usuario.setAlignment(Qt.AlignCenter)
        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(62, 150, 301, 20))
        self.txt_senha.setFont(font)
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        self.btn_entrar = QPushButton(self.frame)
        self.btn_entrar.clicked.connect(self.AbrirJanelaFazerPedido)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(170, 220, 75, 23))
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0)\n"
"\n"
"}\n"
"	")
        self.txt_aviso = QLabel(self.frame)
        self.txt_aviso.setObjectName(u"txt_aviso")
        self.txt_aviso.setGeometry(QRect(60,100,311,20))
        font1 = QFont()
        font1.setPointSize(12)
        self.txt_aviso.setFont(font1)
        self.txt_aviso.setAlignment(Qt.AlignCenter)
        self.combo_cargo = QComboBox(self.frame)
        self.combo_cargo.addItem("Funcionário")
        self.combo_cargo.addItem("Gerente")
        self.combo_cargo.setObjectName(u"combo_cargo")
        self.combo_cargo.setGeometry(QRect(150,20,121,22))
        self.combo_cargo.setFont(font1)
        self.combo_cargo.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 431, 211))
        self.label.setPixmap(QPixmap(u"mps_pizzaria\images\logo_2.png"))
        self.label.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SENHA", None))
        self.btn_entrar.setText(QCoreApplication.translate("MainWindow", u"ENTRAR", None))
        self.txt_aviso.setText("")
        self.combo_cargo.setItemText(0, QCoreApplication.translate("MainWindow", u"funcion\u00e1rio", None))
        self.combo_cargo.setItemText(1, QCoreApplication.translate("MainWindow", u"gerente", None))
        self.combo_cargo.setPlaceholderText("Cargo")
        self.label.setText("")
    # retranslateUi  
            
    def AbrirJanelaFazerPedido(self):
        user = self.txt_usuario.text()
        cargo = self.combo_cargo.currentText()

        try:
            with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
                json.load(outfile)
        except:
            raise Exception("Failed to load the JSON file")
        
        
        controller = LoginScreenController()
        if cargo == "funcionário":
            if controller.validateFunctionary(user):
                self.janela = QMainWindow()
                self.wind = Ui_FazerPedido()
                self.wind.setupUi(self.janela)
                self.janela.show()
        elif cargo == "gerente": 
            if controller.validateGerente(user):
                self.janela = QMainWindow()
                self.wind = UI_GerenteScreen()
                self.wind.setupUi(self.janela)
                self.janela.show()
            else:
                self.txt_aviso.setText("Usuário Inválido!")