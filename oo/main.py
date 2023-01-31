from cliente import Cliente
from conta import Conta

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    cliente = Cliente("marco")
    cliente.nome = "nico"
    print(cliente.nome)

    conta1 = Conta(123, "Nico", 55.5, 1000.0)
    conta1.limite
    #conta1.limite = 2000.0
    print(conta1.limite)
    print(conta1.titular)

    conta1.saca(1200.0)
    conta1.saca(100.0)
    print(conta1.saldo)

conta1 = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(356, "Marco", 120.0, 3000.0)

print(Conta.codigo_banco())
print(Conta.codigos_banco())


#conta1.saldo = 10.0
#print(conta1.saldo)
#print(conta1._Conta__saldo)

#conta2.trasfere(10.0, conta1)

#print(conta1.get_limite())

#conta1.set_limite(50000.0)

#print(conta1.get_limite())

#print(conta1._Conta__limite)

#conta1.extrato()
#conta1.deposita(25.0)
#conta1.extrato()
#conta1.saca(10)
#conta1.extrato()

#conta2.extrato()