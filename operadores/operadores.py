# Operadores aritméticos
"""
Soma = (+)
Subtração = (-)
Multiplicação = (*)
Divisão = (/)
Divisão inteira = (//)
Módulo = (%)
Exponenciação = (**)
"""

# Exemplos

a = 10
b = 12

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
modulo = a % b
expo = a ** b

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisao_inteira)
print(modulo)
print(expo)

# Comparação
"""
igual a = (==)
Diferente de = (!=)
maior que = (>)
menor que = (<)
maior ou igual = (>=)
menor ou igual = (<=)
"""

print(a == b);
print(a != b);
print(a > b);
print(a < b);
print(a >= b);
print(a <= b);

# Lógicos

"""
and = devolve True se ambas as condições são verdadeiras.
or = devolve True se ao menos uma das condições é verdadeira.
not = inverte o valor de uma condição, devolve True se a condição é falsa e False se a condição é verdadeira.
"""
res_and = (a > 5) and (b < 5)
res_or = (a > 15) or (b < 10)
res_not = not (a > 5)

print(res_and)
print(res_or)
print(res_not)