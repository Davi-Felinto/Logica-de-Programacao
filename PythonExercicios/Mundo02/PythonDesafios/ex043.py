from random import randint

peso = int(input('Qual é o seu peso? (Kg) '))
peso = randint(35, 165) if peso == 0 else peso  # se digitar 0, sorteia o peso
altura = int(input('Qual a sua altura? (cm)'))
altura = randint(100, 230) if altura == 0 else altura  # se digitar 0, sorteia a altura
print(f'Primeiro numero: {peso}')
print(f'Segundo numero: {altura}')
imc = (peso / ((altura / 100) ** 2))
print(f'O IMC dessa pessoa é de {imc:.1f}')

if 18.5 > imc:
    print('Você esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABENS, você esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Você esta em OBSIDADE!')
elif 40 <= imc:
    print('Você esta em OBESIDADE MÓRBIDA, cuidado!')