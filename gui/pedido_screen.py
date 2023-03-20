from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UI_PedidoWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(522, 382)
        MainWindow.setStyleSheet(u"background-color: rgb(252, 252, 219);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 501, 341))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 20, 481, 80))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 81, 20))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 81, 20))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 10, 141, 21))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 40, 141, 21))
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 100, 481, 80))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 81, 20))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 81, 20))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(160, 10, 141, 20))
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(160, 40, 141, 20))
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(50, 230, 391, 101))
        self.frame_4.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 10, 131, 20))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 60, 91, 23))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 60, 91, 23))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 522, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sabor da Pizza", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_7.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bebida", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_5.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"confirmar pedido", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"cancelar pedido", None))
    # retranslateUi