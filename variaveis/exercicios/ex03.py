# Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.

salario = float(input('Informe o salário: '))

percentual = 15

calc = (percentual / 100) * salario

novoSalario = calc + salario

print(f'O novo salário é de R${novoSalario}')



