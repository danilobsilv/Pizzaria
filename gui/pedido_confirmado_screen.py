from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UI_PedidoConfirmadoScreen(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(518, 417)
        MainWindow.setStyleSheet(u"background-color: rgb(251, 251, 218);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 501, 361))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 40, 251, 251))
        self.label.setPixmap(QPixmap(u"mps_pizzaria\images\pedido_confirmado.png"))
        self.label.setScaledContents(True)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.clicked.connect(self.voltar_tela_fazer_pedido)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 310, 75, 23))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 518, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

    def voltar_tela_fazer_pedido(self):
        from gui.fazer_pedido_screen import Ui_FazerPedido
        self.janela = QMainWindow()
        self.tela_fazer_pedido = Ui_FazerPedido()
        self.tela_fazer_pedido.setupUi(self.janela)
        self.janela.show()
    