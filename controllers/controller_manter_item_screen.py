from gui.manter_itens_screen import Ui_MainWindow
from serializer.serializer import Serializer
from models.item import Item
import json

class ManterItemController:
    def __init__(self):
        pass


    def cadastrarItem(self):
        manter_itens_screen = Ui_MainWindow()
        serializer = Serializer()

        preco = manter_itens_screen.lineEdit_2.text()
        produto = manter_itens_screen.lineEdit.text()
        quantidade = manter_itens_screen.spinBox.value()

        new_item = Item(produto, preco, quantidade)

        with open("mps_pizzaria\jsons\_stock.json", "r") as outfile:
            data = json.load(outfile)

            if new_item.product in data:
                return
            else:
                serializer.serializeItem(new_item)
        
        with open("mps_pizzaria\jsons\_stock.json", "w") as outfile:
            data = json.dump(outfile)
        
        self.label_3.setText("Item cadastrado!")


    def excluirItem(self):
        manter_items_screen = Ui_MainWindow()

        listItem = manter_items_screen.listWidget.selectedItems()

        if not listItem:
            return
        
        for item in listItem:
            manter_items_screen.listWidget.takeItem(manter_items_screen.listWidget.row(item))

        with open("mps_pizzaria\jsons\_stock.json", "r") as outfile:
            data = json.load(outfile)

        if listItem in data:
            del data[listItem]

        with open("mps_pizzaria\jsons\_stock.json", "w") as outfile:
            data = json.dump(outfile)


    def setOnExcluirItem(self):
        with open("mps_pizzaria\jsons\_stock.json", "r") as outfile:
            data = json.load(outfile)
            for elem in data:
                self.listWidget.addItem(elem)