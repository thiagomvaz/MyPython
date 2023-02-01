matriz = [[42, 23, 34], [100, 215, 114], [10.1, 98.7, 12.3]]
maior_numero = 0

help(matriz.count)
print(dir(matriz.count))
quit()

for linha in matriz:

    for num in linha:

        if num > maior_numero:
            maior_numero = num

print("Maior número:", maior_numero)