# Exercício 025: verifica se a palavra "felinto" está contida no nome digitado

nome = input('Qual o seu nome? ')  # lê o nome do usuário

print(f'Seu nome tem Felinto? {'felinto' in nome.lower()}')  # verifica se a substring 'felinto' existe no nome (ignorando maiúsculas/minúsculas)
