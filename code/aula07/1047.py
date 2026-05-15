# Leitura das hrs e min de inicio e final 
hini, mini, hfin, mfin = map(int, input().split())

# Calcula horas e minutos
hr = hfin - hini
min = mfin - mini

# Ajusta se os minutos ficaram negativos
if min < 0:
    min += 60
    hr -= 1

# Ajusta se as horas ficaram negativas (passou pela meia-noite)
if hr < 0:
    hr += 24

print (f"O JOGO DUROU {hr} HORA(S) E {min} MINUTO(S)")