for i in range(72, 115):
    arquivo = open(f'ex0{i}.py', 'w') # Modo 'w' cria o arquivo se não existir
    arquivo.close() # Sempre feche o arquivo após usá-lo