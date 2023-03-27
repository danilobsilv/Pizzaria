# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fazer_pedido_screenRqAXMW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FazerPedido(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(485, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(253, 253, 220);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 70, 451, 481))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 191, 291))
        self.layout_vertical_listapizzas = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_vertical_listapizzas.setObjectName(u"layout_vertical_listapizzas")
        self.layout_vertical_listapizzas.setContentsMargins(0, 0, 0, 0)
        self.lista_pizzas = QListWidget(self.verticalLayoutWidget)
        self.lista_pizzas.setObjectName(u"lista_pizzas")
        self.lista_pizzas.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.layout_vertical_listapizzas.addWidget(self.lista_pizzas)

        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(239, 10, 181, 291))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listaBebidas = QListWidget(self.horizontalLayoutWidget)
        self.listaBebidas.setObjectName(u"listaBebidas")
        self.listaBebidas.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.listaBebidas)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 310, 441, 171))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 140, 141, 23))
        font = QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 0, 401, 51))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 191, 20))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_1 = QSpinBox(self.frame_3)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setGeometry(QRect(260, 20, 42, 22))
        self.spinBox_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 60, 411, 31))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 191, 16))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox_2 = QSpinBox(self.frame_4)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(270, 10, 42, 22))
        self.spinBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.botao_sabores_disponiveis = QPushButton(self.centralwidget)
        self.botao_sabores_disponiveis.setObjectName(u"botao_sabores_disponiveis")
        self.botao_sabores_disponiveis.setGeometry(QRect(50, 40, 171, 23))
        self.botao_sabores_disponiveis.setFont(font)
        self.botao_sabores_disponiveis.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.botao_bebidas_disponiveis = QPushButton(self.centralwidget)
        self.botao_bebidas_disponiveis.setObjectName(u"botao_bebidas_disponiveis")
        self.botao_bebidas_disponiveis.setGeometry(QRect(270, 40, 161, 23))
        self.botao_bebidas_disponiveis.setFont(font)
        self.botao_bebidas_disponiveis.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 485, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"confirmar pedido", None))
        self.label.setText("")
        self.label_2.setText("")
        self.botao_sabores_disponiveis.setText(QCoreApplication.translate("MainWindow", u"sabores dispon\u00edveis", None))
        self.botao_bebidas_disponiveis.setText(QCoreApplication.translate("MainWindow", u"bebidas dispon\u00edveis", None))
    # retranslateUi



    def abrir_tela_pedido_confirmado(self):
        from gui.pedido_confirmado_screen import Ui_MainWindow
        self.janela = QMainWindow()
        self.pedido_confirmado_screen = Ui_MainWindow()
        self.pedido_confirmado_screen.setupUi(self.janela)
        self.janela.show()