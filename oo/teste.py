
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))


minha_conta = cria_conta(123, "Thiago", 55.0, 1000.0)

deposita(minha_conta, 15.0)
extrato(minha_conta)
saca(minha_conta, 30.0)
extrato(minha_conta)

minha_conta["saldo"] = 500.0
print(minha_conta)