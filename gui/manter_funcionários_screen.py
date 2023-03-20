from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from models.funcionario import Funcionario
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(533, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(254, 254, 221);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(350, 0, 151, 421))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 101, 20))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 40, 91, 271))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_excluir_funcionario = QPushButton(self.frame)
        self.btn_excluir_funcionario.setObjectName(u"btn_excluir_funcionario")
        self.btn_excluir_funcionario.setGeometry(QRect(20, 340, 111, 23))
        self.btn_excluir_funcionario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_funcionario.setStyleSheet(u"QPushButton{\n"
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
        self.label_usuario_excluido = QLabel(self.frame)
        self.label_usuario_excluido.setObjectName(u"label_usuario_excluido")
        self.label_usuario_excluido.setGeometry(QRect(16,380,151,20))
        self.label_usuario_excluido.setFont(font)
        self.label_usuario_excluido.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 0, 321, 411))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 10, 131, 20))
        self.label_2.setCursor(QCursor(Qt.SplitVCursor))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 50, 271, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 100, 271, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(32, 150, 271, 20))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 230, 271, 20))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setEchoMode(QLineEdit.Normal)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(100, 290, 121, 22))
        self.dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(130, 340, 75, 23))
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.clicked.connect(self.cadastrarFuncionario)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
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
        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 190, 271, 20))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)
        self.label_usuario_cadastrado = QLabel(self.frame_2)
        self.label_usuario_cadastrado.setObjectName("label_usuario_cadastrado")
        self.label_usuario_cadastrado.setGeometry(QRect(56,380,201,20))
        self.label_usuario_cadastrado.setFont(font)
        self.label_usuario_cadastrado.setAlignment(Qt.AlignCenter)
        self.btn_ok = QPushButton(self.centralwidget)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(220, 480, 75, 23))
        self.btn_ok.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ok.clicked.connect(self.voltarScreenGerente) #----------------------------------
        self.btn_ok.setStyleSheet(u"QPushButton{\n"
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 533, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        try:
            with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
                data = json.load(outfile)
                for elem in data:
                    self.listWidget.addItem(elem)

        except:
            raise Exception("ERROR")
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rios", None))
        self.btn_excluir_funcionario.setText(QCoreApplication.translate("MainWindow", u"Excluir funcion\u00e1rio", None))
        self.label_usuario_excluido.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar funcion\u00e1rio", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome completo", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sal\u00e1rio", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.label_usuario_cadastrado.setText("")
        self.btn_ok.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

    def cadastrarFuncionario(self):
        from serializer.serializer import Serializer
        
        nome = self.lineEdit.text()
        password = self.lineEdit_2.text()
        rg = self.lineEdit_3.text()
        cargo = self.lineEdit_5.text()
        salary = self.lineEdit_4.text()
        hiring_date = self.dateEdit.text()

        
        serializer = Serializer()
        new_funcionario = Funcionario(nome, password, rg, cargo, salary, hiring_date)
        serializer.serializeFunctionary(new_funcionario)
        
        self.label_usuario_cadastrado.setText("funcionário cadastrado")

    def excluirFuncionarios(self):  # último método faltando
        pass

    # def showListWidgetFuncionarios(self):
        # try:
        #     with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
        #         data = json.load(outfile)
        #         for elem in data:
        #             self.listWidget.addItem(elem)

        # except:
        #     raise Exception("ERROR")


    def voltarScreenGerente(self):
        from gui.gerente_screen import Ui_MainWindow
        self.janela = QMainWindow()
        self.window = Ui_MainWindow()
        self.window.setupUi(self.janela)
        self.janela.show()

    