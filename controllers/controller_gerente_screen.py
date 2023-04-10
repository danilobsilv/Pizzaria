
from gui.fazer_pedido_screen import Ui_FazerPedido, QMainWindow
from gui.manter_funcionários_screen import Ui_ManterFuncionariosScreen
from gui.manter_itens_screen import Ui_MainWindow

class gerenteScreenController:
    def __init__(self):
        pass
    
    def abrirFazerPedidoScreen(self):
        self.janela1 = QMainWindow()
        self.window1 = Ui_FazerPedido()
        self.window1.setupUi(self.janela1)
        self.janela1.show()

    def abrirManterFuncionariosScreen(self):
        self.janela2 = QMainWindow()
        self.window2 = Ui_ManterFuncionariosScreen()
        self.window2.setupUi(self.janela2)
        self.janela2.show()

    def abrirManterItensScreen(self):
        self.janela3 = QMainWindow()
        self.window3 = Ui_MainWindow()
        self.window3.setupUi(self.janela3)
        self.janela3.show()