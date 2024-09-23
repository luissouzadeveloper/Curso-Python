"""
Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
"""

velocidadeCarro = int(input('Informe a velocidade do carro: '))

if velocidadeCarro > 80:
    print(f'A velocidade do carro foi de {velocidadeCarro} km/h. Multado!')
    excesso = velocidadeCarro - 80
    valorMulta = excesso * 5
    print(f'O valor da multa é de R${valorMulta}')
else:
    print('Dirija sempre usando o cinto de segurança!')