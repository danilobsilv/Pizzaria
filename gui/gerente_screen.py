from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from controllers.controller_gerente_screen import gerenteScreenController

class UI_GerenteScreen(object):
    def setupUi(self, MainWindow):
        controller = gerenteScreenController()
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(637, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 621, 551))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 222);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(129, 50, 301, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btn_abrir_fazer_pedido = QPushButton(self.frame_2)
        self.btn_abrir_fazer_pedido.setObjectName(u"btn_abrir_fazer_pedido")
        self.btn_abrir_fazer_pedido.setGeometry(QRect(100, 30, 111, 23))
        self.btn_abrir_fazer_pedido.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_abrir_fazer_pedido.clicked.connect(controller.abrirFazerPedidoScreen)
        self.btn_abrir_fazer_pedido.setStyleSheet(u"QPushButton{\n"
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
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(130, 150, 301, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_abri_manter_funcionarios = QPushButton(self.frame_3)
        self.btn_abri_manter_funcionarios.setObjectName(u"btn_abri_manter_funcionarios")
        self.btn_abri_manter_funcionarios.setGeometry(QRect(100, 30, 111, 23))
        self.btn_abri_manter_funcionarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_abri_manter_funcionarios.clicked.connect(controller.abrirManterFuncionariosScreen)
        self.btn_abri_manter_funcionarios.setStyleSheet(u"QPushButton{\n"
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
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(130, 270, 301, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btn_abrir_manter_itens = QPushButton(self.frame_4)
        self.btn_abrir_manter_itens.setObjectName(u"btn_abrir_manter_itens")
        self.btn_abrir_manter_itens.setGeometry(QRect(100, 30, 111, 23))
        self.btn_abrir_manter_itens.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_abrir_manter_itens.clicked.connect(controller.abrirManterItensScreen)
        self.btn_abrir_manter_itens.setStyleSheet(u"QPushButton{\n"
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
        self.menubar.setGeometry(QRect(0, 0, 637, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_abrir_fazer_pedido.setText(QCoreApplication.translate("MainWindow", u"Fazer Pedido", None))
        self.btn_abri_manter_funcionarios.setText(QCoreApplication.translate("MainWindow", u"Manter funcion\u00e1ros", None))
        self.btn_abrir_manter_itens.setText(QCoreApplication.translate("MainWindow", u"Manter Itens", None))
    # retranslateUi
