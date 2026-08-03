# Exercício 006: calcula dobro, triplo e raiz quadrada de um número

n = int(input('Digite um numero: '))  # lê um número inteiro

# n*2 = dobro | n*3 = triplo | n**0.5 = raiz quadrada (elevar a 0.5 equivale a tirar a raiz)
# {:.2f} formata a raiz com 2 casas decimais
print('O dobro de {} vale {}\nO triplo de {} vale {}\nA raiz quadrada de {} vale {:.2f}'.format(n, (n*2), n, (n*3), n, (n**0.5)))
