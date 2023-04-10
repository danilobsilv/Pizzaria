from gui.gerente_screen import UI_GerenteScreen, QMainWindow
from gui.manter_funcionários_screen import Ui_ManterFuncionariosScreen
from serializer.serializer import Serializer
from models.funcionario import Funcionario
import json

class ManterFuncionariosController:
    def __init__(self):
         pass

    def cadastrarFuncionario(self): 
            screen_manter_funcionario = Ui_ManterFuncionariosScreen()
            serializer = Serializer()
            
            nome = screen_manter_funcionario.lineEdit.text()
            password = screen_manter_funcionario.lineEdit_2.text()
            rg = screen_manter_funcionario.lineEdit_3.text()
            cargo = screen_manter_funcionario.lineEdit_5.text()
            salary = screen_manter_funcionario.lineEdit_4.text()
            hiring_date = screen_manter_funcionario.dateEdit.text()

            new_funcionario = Funcionario(nome, password, rg, cargo, salary, hiring_date)
 
            serializer.serializeFunctionary(new_funcionario)
            
            screen_manter_funcionario.label_usuario_cadastrado.setText("funcionário cadastrado")


    def excluirFuncionario(self):  # último método faltando
        screen_manter_funcionarios = Ui_ManterFuncionariosScreen()

        listItems = screen_manter_funcionarios.listWidget.selectedItems()
        if not listItems: 
            return
        
        for item in listItems:
            screen_manter_funcionarios.listWidget.takeItem(self.listWidget.row(item))

        with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
            data = json.load(outfile)

        if listItems in data:
            del data[listItems]

        with open("mps_pizzaria\jsons\_funcionary.json", "w") as outfile:
            json.dump(data, outfile)


    def voltarScreenGerente(self):
        self.janela = QMainWindow()
        self.window = UI_GerenteScreen()
        self.window.setupUi(self.janela)
        self.janela.show()


    def showListWidgetFuncionarios(self):
        screen_manter_funcionarios = Ui_ManterFuncionariosScreen()
        with open("mps_pizzaria\jsons\_funcionary.json", "r") as outfile:
            data = json.load(outfile)
            for elem in data:
                screen_manter_funcionarios.listWidget.addItem(elem)