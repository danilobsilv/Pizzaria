from serializer.serializer import Serializer
from models.cliente import Cliente
from models.funcionario import Funcionario

lista = []
serial = Serializer()
# cliente = Cliente("danilo bruno da silva","12345","89328","1283891231231","male")
# lista.append(cliente)
# cliente2 = Cliente("miguel","123182371939871","18237917","12739182379817","male")
# lista.append(cliente2)

# for client in lista:
#     serial.serializeClient(client)

func1 = Funcionario("funcionario 1","123456789","819273",100.21, "10/05/2050")
lista.append(func1)
func2 = Funcionario("funcionario 2", "098080","09808098123",109.90,"17/04/2025")
lista.append(func2)

for func in lista:
    serial.serializeFunctionary(func)
