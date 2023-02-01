# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("Selecione o número da operação desejada: ")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")
print("Digite sua opção (1/2/3/4): ")

opcao = int(input())

while opcao not in [1,2,3,4]:
    print("Digite um valor entre as opções apresentadas")
    opcao = int(input())

print("Digite o primeiro número: ")
num1 = int(input())

print("Digite o segundo número: ")
num2 = int(input())

def resultado(num1, num2):
    if opcao == 1:
        resultado = num1 + num2
        print(f'O valor da soma é {resultado}')
    if opcao == 2:
        resultado = num1 - num2
        print(f'O valor da subtração é {resultado}')
    if opcao == 3:
        resultado = num1 * num2
        print(f'O valor da multiplicação é {resultado}')
    if opcao == 4:
        resultado = num1 / num2
        print(f'O valor da divisão é {resultado}')

resultado(num1, num2)
