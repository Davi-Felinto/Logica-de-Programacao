N1, N2, N3, N4 = map(float, input().split(' '))

media = ( N1*2 + N2*3 + N3*4 + N4*1) / (2+3+4+1)

print(f"Media: {media}")
if 7 <= media:
    print('Aluno aprovado')
elif 5 > media:
    print('Aluno reprovado')
elif 5 <= media and 7 > media:
    print('Aluno em exame')
    N5 = float(input())
    print(f"Nota do exame: {N5}")
    media = (media + N5) / 2
    if media >=  5:
        print('Aluno aprovado')
        print(f"Media final: {media}")
    elif media < 5:
        print('Aluno reprovado')
        print(f"Media final: {media}")