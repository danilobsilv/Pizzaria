from gui.pedido_confirmado_screen import UI_PedidoConfirmadoScreen, QMainWindow
from gui.fazer_pedido_screen import Ui_FazerPedido
from gui.pedido_screen import Ui_PedidoWindow
import json

class PedidoScreenController:
    
    def __init__(self):
        pass

    def abrirPedidoConfirmadoScreen(self):
        self.janela = QMainWindow()
        self.pedido_confirmado_screen = UI_PedidoConfirmadoScreen()
        self.pedido_confirmado_screen.setupUi(self.janela)
        self.janela.show()


    def cancelarPedido(self):
        self.janela = QMainWindow()
        self.fazer_pedido_screen = Ui_FazerPedido()
        self.fazer_pedido_screen.setupUi(self.janela)
        self.janela.show()  

    def getValorPedido(self):
        self.janela = QMainWindow()
        fazer_pedido_screen = Ui_FazerPedido()
        fazer_pedido_screen.setupUi(self.janela)

        pedido_screen = Ui_PedidoWindow()
        
        sabor_pizza = fazer_pedido_screen.pizza_escolhida.text()
        sabor_bebida = fazer_pedido_screen.bebida_escolhida.text()
        
        qtde_pizza = (fazer_pedido_screen.spinBox_1.value())
        qtde_bebida = (fazer_pedido_screen.spinBox_2.value())

        with open("mps_pizzaria\jsons\_bebidas.json", "r") as outfile:
            data_1 = json.load(outfile)

        preco_bebida = float(data_1["bebida"]["price"])

        with open("mps_pizzaria\jsons\_pizza.json", "r") as outfile:
            data_2 = json.load(outfile)

        preco_pizza = float(data_2["pizza"]["price"])
 
        pedido_screen.label_6.setText(f"{sabor_pizza}")
        pedido_screen.label_8.setText(f"{sabor_bebida}")
        pedido_screen.label_7.setText(f"{(preco_pizza*qtde_pizza)}:.2f")
        pedido_screen.label_9.setText(f"{(preco_bebida*qtde_bebida)}:.2f")
        full_price = preco_bebida*qtde_bebida + preco_pizza*qtde_pizza
        pedido_screen.label_5.setText(f"{full_price}:.2f")
    