val = int(input())

notas = [100, 50, 20, 10, 5, 2, 1] #array (vetor)

print(val)

for nota in notas: #para nota, recebe notas
    quantidae = val//nota #divisão valor inteiro 
    val = val%nota #% resto da divisão

    print(f'{quantidae} nota(s) de R$ {nota},00')