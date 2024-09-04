# Uma tupla é uma estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma tupla são encerrados entre parênteses (), separados por vírgulas.

ponto = (3, 4)
print(ponto[0])
print(ponto[1])

# Métodos
"""
-count: devolve o número de vezes que um elemento aparece na tupla. 
-index: devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
-len: embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.
"""
minha_tupla = (1,2,3,2,4,2)

print(minha_tupla.index(2))
print(minha_tupla.index(2, 2))
print(minha_tupla.index(2, 2, 4))