# Condicionais

# if
idade = 18
if idade >= 18:
    print('É de maior!')

# if-else
idade_2 = 15
if idade_2 >= 18:
    print('Pode tirar a habilitação')
else:
    print('Ainda não pode tirar a habilitação')

# if-elif
nota = 6.4

if nota >= 9.0:
    print('Nota excelente')
elif nota >= 8.9:
    print('Nota regular')
elif nota >= 7.0:
    print('Nota baixa')
else:
    print('Reprovado!')

# Exercício:

idade_3 = 25
if idade_3 <= 16:
    print('Você não pode votar!')
elif idade_3 >= 17 and idade_3 <= 18 or idade_3 >= 70:
    print('O voto é facultativo')
else:
    print('O voto é obrigátorio')