"""
Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().
"""

# Criação e operações básicas

frutas = {'Maçã', 'Banana', 'Laranja'}
numeros = set([1, 2, 3, 4, 5])

"""
Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).
"""

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(f'A uniao é {uniao}')

intersecao = conjunto1 & conjunto2
print(f'A intersecao é {intersecao}')

diferenca = conjunto1 - conjunto2
print(f'A diferença é {diferenca}')

diferenca_simetrica = conjunto1 ^ conjunto2
print(f'A diferença simétrica é {diferenca_simetrica}')

# Métodos de conjuntos

"""
Os conjuntos em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

add(elemento): adiciona um elemento ao conjunto.
remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
clear(): remove todos os elementos do conjunto.
"""

frutas.add('Pêra')
print(frutas)

frutas.remove('Banana')
print(frutas)

frutas.discard('Morango')
print(frutas)

frutas.clear()
print(frutas)