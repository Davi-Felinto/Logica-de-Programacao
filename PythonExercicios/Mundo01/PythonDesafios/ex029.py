from random import randint

vel = randint(25, 115) # sorteando velocidade entre 25 a 115 e calculando multa
multa = ((vel - 80) * 7)

print('-='*20) # Saida da velocidade
print('Velocidade do carro no pardal: {} KM/h'.format(vel))
print('-='*20)

if vel > 80: # Saida da verificação se passou acima de 80 ou abaixo de 40
    print(f'Multado! Você excedeu o limiite permitido que é de 80KM/h \nVocê deve pagar uma multa de R${multa:.2f}!')
elif vel < 40:
    print('Dirija mais rapido! Abaixo da velocidade minima!')
print('Tenha um bom dia! Dirija com segurança!')