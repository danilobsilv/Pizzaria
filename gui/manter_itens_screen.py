from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(514, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(254, 254, 221);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 301, 461))
        self.frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 121, 16))
        font = QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 110, 251, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 70, 251, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(130, 160, 51, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.spinBox.setFont(font1)
        self.spinBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 280, 111, 23))
        self.pushButton.setFont(font1)
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
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(290, 0, 20, 451))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 440, 501, 20))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(310, 0, 201, 461))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 20, 71, 16))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.listWidget = QListWidget(self.frame_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(40, 60, 121, 192))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 280, 101, 23))
        self.pushButton_2.setFont(font1)
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
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 439, 201, 21))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(100, 470, 301, 80))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 30, 75, 23))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.menubar.setGeometry(QRect(0, 0, 514, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Item", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Item", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Itens", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Excluir Item", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

