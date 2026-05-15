# Leitura das hrs de inicio e final 
hinicio, hfinal = map(int, input().split())

# calculo se hinicio for mais q hfinal 
if hinicio > hfinal:
    duracao = (24 - hinicio) + hfinal
# calculo se durar 24 hr
elif hinicio == hfinal:
    duracao = 24
# calculo se hfinal for mais q hinicial
else:
    duracao = hfinal - hinicio

print(f"O JOGO DUROU {duracao} HORA(S)")