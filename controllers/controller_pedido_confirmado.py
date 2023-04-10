from gui.pedido_confirmado_screen import UI_PedidoConfirmadoScreen, QMainWindow
from gui.fazer_pedido_screen import Ui_FazerPedido

class PedidoConfirmadoController:
      def __init__(self):
        pass

      def voltarTelaFazerPedido(self):
            screen_pedido_confirmado = UI_PedidoConfirmadoScreen()
            
            screen_pedido_confirmado.janela = QMainWindow()
            self.tela_fazer_pedido = Ui_FazerPedido()
            self.tela_fazer_pedido.setupUi(screen_pedido_confirmado.janela)
            screen_pedido_confirmado.janela.show()
