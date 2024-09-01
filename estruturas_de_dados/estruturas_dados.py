# Listas = arrays
frutas = ['maçã', 'banana', 'laranja']
# Acesso por índices
print(frutas[0])
print(frutas[1])
print(frutas[2])
# Índices negativos
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

# Métodos
"""
- append(elemento): adiciona um elemento ao final da lista.
- insert(indice, elemento): insere um elemento em uma posição específica da lista.
- remove(elemento): remove a primeira ocorrência de um elemento na lista.
- pop(indice): remove e retorna o elemento em uma posição específica da lista.
- sort(): ordena os elementos da lista em ordem ascendente.
- reverse(): inverte a ordem dos elementos na lista.
"""

# append
frutas.append('Uva')
print(frutas)

# insert
frutas.insert(3, 'Abacaxi')
print(frutas)

# remove
frutas.remove('banana')
print(frutas)

# pop
fruta_removida = frutas.pop(1)
print(frutas)
print(fruta_removida)

# sort
frutas.sort()
print(frutas)

# reverse
frutas.reverse()
print(frutas)

# Lista de compreensão
numeros = [1,2,3,4,5]
quadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(quadrados)