# Aula 12a: cumprimenta o usuário e reage a nomes populares/femininos

nome = str(input('Qual o seu nome? '))  # lê o nome digitado (str() é redundante, pois input() já retorna string)

if nome.lower() == 'davi':  # verifica se o nome é 'davi' (ignorando maiúsculas/minúsculas)
    print('Que nome lindo você tem!')
elif nome.lower() == 'pedro' or nome.lower() == 'maria' or nome.lower() == 'paulo':  # verifica se é um dos nomes populares
    print('Seu nome é bem popular no Brasil.!')
elif nome.lower() in 'ana claúudia jéssica juliana':  # verifica se o nome é uma substring dessa string de nomes femininos
    print('Belo nome feminino!')
else:  # qualquer outro nome
    print('Seu nome é muito normal!')
print(f'Bom dia , {nome.title()}!')  # title() deixa a inicial do nome em maiúscula
