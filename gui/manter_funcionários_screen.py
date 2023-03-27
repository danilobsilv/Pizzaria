from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from controllers.controller_manter_funcionarios_screen import ManterFuncionariosController
import json

class Ui_ManterFuncionariosScreen(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(533, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(254, 254, 221);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(350, 0, 171, 421))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 101, 20))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(50, 50, 91, 271))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 340, 111, 23))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.excluirFuncionario)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.label_usuario_excluido.setGeometry(QRect(16, 380, 151, 20))
        self.label_usuario_excluido.setFont(font)
        self.label_usuario_excluido.setAlignment(Qt.AlignCenter)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 390, 181, 21))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
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
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 340, 75, 23))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.clicked.connect(self.cadastrarFuncionario)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
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
        self.label_usuario_cadastrado.setObjectName(u"label_usuario_cadastrado")
        self.label_usuario_cadastrado.setGeometry(QRect(56, 380, 201, 20))
        self.label_usuario_cadastrado.setFont(font)
        self.label_usuario_cadastrado.setAlignment(Qt.AlignCenter)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(311, 0, 16, 411))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-20, 389, 331, 31))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 480, 75, 23))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.clicked.connect(self.voltarScreenGerente)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
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
         
        with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
            data = json.load(outfile)
            for elem in data:
                self.listWidget.addItem(elem)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rios", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Excluir funcion\u00e1rio", None))
        self.label_usuario_excluido.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar funcion\u00e1rio", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome completo", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sal\u00e1rio", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.label_usuario_cadastrado.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi


    def cadastrarFuncionario(self): 
        from serializer.serializer import Serializer
        from models.funcionario import Funcionario
        
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

    def excluirFuncionario(self):  # último método faltando
        listItems = self.listWidget.selectedItems()
        if not listItems: return
        
        for item in listItems:
            self.listWidget.takeItem(self.listWidget.row(item))


        with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
            data = json.load(outfile)

        if listItems in data:
            del data[listItems]

        with open("mps_pizzaria\jsons\_funcionary.json", "w") as outfile:
            json.dump(data, outfile)





    # def showListWidgetFuncionarios(self):
    #     try:
    #         with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
    #             data = json.load(outfile)
    #             for elem in data.get():
    #                 self.listWidget.addItem(elem)

    #     except:
    #         raise Exception("ERROR")



    def voltarScreenGerente(self):
        from gui.gerente_screen import UI_GerenteScreen
        self.janela = QMainWindow()
        self.window = UI_GerenteScreen()
        self.window.setupUi(self.janela)
        self.janela.show()

