# Exercício 029: simula um radar de velocidade e calcula multa

from random import randint  # sorteia a velocidade do carro

vel = randint(25, 115)  # sorteia uma velocidade entre 25 e 115 km/h
multa = ((vel - 80) * 7)  # calcula quanto seria a multa caso ultrapasse o limite (R$7 por km acima de 80)

print('-='*20)
print('Velocidade do carro no pardal: {} KM/h'.format(vel))
print('-='*20)

if vel > 80:  # se a velocidade passou do limite permitido (80 km/h), aplica multa
    print(f'Multado! Você excedeu o limiite permitido que é de 80KM/h \nVocê deve pagar uma multa de R${multa:.2f}!')
elif vel < 40:  # se estiver muito abaixo do limite mínimo (40 km/h), alerta o motorista
    print('Dirija mais rapido! Abaixo da velocidade minima!')
print('Tenha um bom dia! Dirija com segurança!')
