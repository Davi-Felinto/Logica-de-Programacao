from time import sleep
ficha = []
aluno = []

while True:
    aluno.append(input('Nome: ').title())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    ficha.append(aluno[:])
    aluno.clear()
    resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break

print('-='*30)
print(f'{'No.':<5}', f'{'NOME':<10}', f'{'MÉDIA':^5}')
print('-'*30)
for i, alun in enumerate(ficha):
    print(f'{i:<5}', f'{alun[0]:<10}',f'{(alun[1] + alun[2])/2:>5.1f}')
print('-'*30)

while True:
    respAlunoNota = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if respAlunoNota == 999:
        print('FINALIZANDO...')
        sleep(1)
        print('<<< VOLTE SEMPRE >>>')
        break
    if respAlunoNota <= len(ficha):
        print(f'Notas de {ficha[respAlunoNota][0]} são {ficha[respAlunoNota][1], ficha[respAlunoNota][2]}')
        print('-'*30)




# while True:
#     nome = (input('Nome: ').title())
#     nota1 = (float(input('Nota 1: ')))
#     nota2 = (float(input('Nota 2: ')))
#     media = (nota1 + nota2)/2
#     ficha.append([nome,[nota1, nota2], media])
#     resp = input('Quer continuar? [S/N] ').upper()
#     if resp == 'N':
#         break

# print('-='*30)
# print(f'{'No.':<5}{'NOME':<10}{'MÉDIA':^5}')
# print('-'*30)
# for i, alun in enumerate(ficha):
#     print(f'{i:<5}{alun[0]:<10}{media:>5.1f}')
# print('-'*30)

# while True:
#     respAlunoNota = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
#     if respAlunoNota == 999:
#         print('FINALIZANDO...')
#         sleep(1)
#         print('<<< VOLTE SEMPRE >>>')
#         break
#     if respAlunoNota <= len(ficha):
#         print(f'Notas de {ficha[respAlunoNota][0]} são {ficha[respAlunoNota][1]}')
#         print('-'*30)