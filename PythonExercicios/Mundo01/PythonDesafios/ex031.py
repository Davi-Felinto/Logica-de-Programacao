# Exercício 031: calcula o preço de uma passagem com base na distância

# importando modulos
from random import randint  # sorteia a distância da viagem
from time import sleep      # pausa a execução

# Sorteando distancia
dis = randint(100,1000)  # sorteia uma distância entre 100 e 1000 km

# Saida da distancia sorteada
print('---'*5)
print('Distancia da sua viagem: {}'.format(dis))
sleep(2)

# Verificando se a distancia é maior q 200 e calculando valor da passagem
print('---'*5)
# Versão alternativa (comentada) usando if/else tradicional
'''if dis > 200:
    passagem = dis * 0.45
else:
    passagem = dis * 0.50'''
passagem = (dis * 0.45) if dis > 200 else (dis * 0.50)  # operador ternário: preço por km varia conforme a distância

# Saida do peço da passagem 
print(f'Você esta prestes a começa uma viagem de {dis}KM')
print(f'E o preço da sua passagem sera de R${passagem:.2f}')
