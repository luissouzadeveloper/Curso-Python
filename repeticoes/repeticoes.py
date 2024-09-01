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