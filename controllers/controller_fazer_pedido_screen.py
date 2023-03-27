import json

class FazerPedidoScreenController:
    def __init__(self) -> None:
        self.file_name_pedido = "mps_pizzaria\jsons\_pedido.json"
    
        
    def checkSaboresDisponiveis(self):
        from gui.fazer_pedido_screen import Ui_FazerPedido
        screen = Ui_FazerPedido()

        with open(self.file_name_pedido, "r") as outfile:
            data = json.load(outfile)
            
            for _ in range(len(data)):
                nome = data.get("calabresa")
                screen.lista_pizzas.addItems(nome)