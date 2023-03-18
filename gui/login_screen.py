from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 575)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 222);")
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(80, 230, 451, 281))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 222);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        
        self.txt_usuario = QLineEdit(self.frame)
        self.txt_usuario.setObjectName("txt_usuario")
        self.txt_usuario.setFont(QFont("Arial", 11))
        self.txt_usuario.setStyleSheet("color: rgb(37, 34, 51)")
        self.txt_usuario.setAlignment(Qt.AlignCenter)
        
        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName("txt_senha")
        self.txt_senha.setFont(QFont("Arial", 11))
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        
        self.btn_entrar = QPushButton(self.frame)
        self.btn_entrar.setObjectName("btn_entrar")
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet("""
            QPushButton {
                background-color: rgb(0,0,0);
                color: rgb(255,255,255);
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgb(255,255,255);
                color: rgb(0,0,0);
            }
        """)
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setPixmap(QPixmap("../../images/logo_2.png"))
        self.label.setScaledContents(True)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        # Add layout for central widget
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        # Add spacer item to layout
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)
        
        # Add label to layout
        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)
        
        # Add frame to layout
        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)
        
        # Add spacer item to layout
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer_2)
        
        # Set layout for central widget
        self.centralwidget.setLayout(self.verticalLayout)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        self.txt_usuario.setPlaceholderText("USUÁRIO")
