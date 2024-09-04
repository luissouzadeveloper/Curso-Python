# Dicionário
pessoa = {'nome' : 'João', 'idade' : 25, 'cidade':'Madri'}
print(pessoa['cidade'])

# Métodos
"""
keys(): retorna uma visualização de todas as chaves do dicionário.

values(): retorna uma visualização de todos os valores do dicionário.

items(): retorna uma visualização de todos os pares chave-valor do dicionário.

update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.
"""
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

print(pessoa.update({'profissão':'Programador'}))
print(pessoa)
