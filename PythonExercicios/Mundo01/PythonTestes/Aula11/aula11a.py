# Aula 11a: exemplos de cores no terminal usando códigos ANSI de escape

# Formato geral: \033[<estilo>;<cor do texto>;<cor do fundo>m TEXTO \033[m (o \033[m reseta a formatação)
print('\033[;30;41m TESTE \033[m')  # texto preto (30), fundo vermelho (41)
print('\033[4;36;43m TESTE \033[m')  # estilo sublinhado (4), texto ciano (36), fundo amarelo (43)
print('\033[;35;43m TESTE \033[m')  # texto magenta (35), fundo amarelo (43)
print('\033[;30;42m TESTE \033[m')  # texto preto (30), fundo verde (42)
print('\033[;30;47m TESTE \033[m')  # texto preto (30), fundo branco (47)
print('\033[;37;40m TESTE \033[m')  # texto branco/cinza claro (37), fundo preto (40)
