from gui.pedido_screen import Ui_PedidoWindow, QMainWindow
from gui.fazer_pedido_screen import Ui_FazerPedido
from serializer.serializer import Serializer
from models.pedido import Pedido
import json

class FazerPedidoScreenController:
    def __init__(self) -> None:
        self.file_name_stock = "mps_pizzaria\jsons\_stock.json"
    
        
    def checkSaboresDisponiveis(self):
        from gui.fazer_pedido_screen import Ui_FazerPedido
        screen = Ui_FazerPedido()

        with open(self.file_name_stock, "r") as outfile:
            data = json.load(outfile)

            for sabor in data:
                screen.lista_pizzas.addItems(sabor)

    def abrirTelaPedido(self):
        screen_pedido = Ui_PedidoWindow()
        new_pedido = Pedido()
        serializer = Serializer()

        new_pedido.pushItemInList(screen_pedido.lista_pizzas.currentItem().text())
        new_pedido.pushItemInList(screen_pedido.listaBebidas.currentItem().text())
        
        serializer.serializePedido(new_pedido)

        self.janela = QMainWindow()
        self.pedido_screen = Ui_PedidoWindow()
        self.pedido_screen.setupUi(self.janela)
        self.janela.show()

    def setPedidoOnLabel(self):
        screen_fazer_pedido = Ui_FazerPedido()
        
        pizza = screen_fazer_pedido.lista_pizzas.currentItem().text()
        bebida = screen_fazer_pedido.listaBebidas.currentItem().text()

        screen_fazer_pedido.pizza_escolhida.setText(pizza)
        screen_fazer_pedido.bebida_escolhida.setText(bebida)

    def setSaboresOnLabel(self):
        screen_fazer_pedido = Ui_FazerPedido()
        with open("mps_pizzaria\jsons\_pizza.json","r") as outfile:
            data = json.load(outfile)
            for elem in data:
                screen_fazer_pedido.lista_pizzas.addItem(elem)
        with open("mps_pizzaria\jsons\_bebidas.json","r") as outfile:
            data = json.load(outfile)
            for elem in data:
                screen_fazer_pedido.listaBebidas.addItem(elem)