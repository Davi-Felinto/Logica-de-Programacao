nome = str(input('Qual o seu nome? '))

if nome.lower() == 'davi':
    print('Que nome lindo você tem!')
elif nome.lower() == 'pedro' or nome.lower() == 'maria' or nome.lower() == 'paulo':
    print('Seu nome é bem popular no Brasil.!')
elif nome.lower() in 'ana claúudia jéssica juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é muito normal!')
print(f'Bom dia , {nome.title()}!')