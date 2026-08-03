# Aula 10a: cumprimenta o usuário e reage se o nome for "Davi"

nome = str(input('Qual o seu nome? '))  # lê o nome (str() é redundante aqui, pois input() já retorna string)

if nome.lower() == 'davi':  # compara em minúsculas para ignorar maiúsculas/minúsculas
    print('Que nome lindo você tem!')
else:
    print('Seu nome é muito normal!')
print(f'Bom dia ,{nome.title()}!')  # title() deixa a inicial do nome em maiúscula
