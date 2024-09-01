# Repetições

# EX: for
frutas = ['maçã', 'banana', 'morango']

for fruta in frutas:
    print(fruta)

# EX: while
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1

# Controle de loops: break
cont = 0
while True:
    print(cont)
    cont += 1

    if cont == 5:
        break

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass
for i in range(5):
    pass

# Exercício 1: Escreva um programa que imprima todos os números de 1 a 10 usando um loop for.
print('-----------Exercício----------------')
soma = 0
for nums in range(1, 101):
    soma += nums

print('Soma de todos os valores:', soma)

# Exercício 2: Escreva um programa que faça uma contagem regressiva a partir de 10 até 1 e, em seguida, imprima "Feliz Ano Novo!" no final. Use um loop while.

contador2 = 10

while contador2 >= 1:
    print(contador2)
    contador2 -= 1

# Exercício 3: Escreva um programa que imprima a tabuada de 5 (de 1 a 10) usando um loop for.

for i in range(1, 11):
    print(i * 5)