# Aula 10b: calcula a média de duas notas e informa aprovação

n1 = float(input('Digite a primeira nota: '))  # lê a 1ª nota
n2 = float(input('Digite a segunda nota: '))   # lê a 2ª nota

m = ((n1 + n2)/2)  # calcula a média aritmética das duas notas

print(f'A sua media foi {m:.1f}')

# Forma alternativa (comentada) usando if/else tradicional
'''if m >= 6.0:
    print('Sua media foi boa! PARABENS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')'''

print(f'Sua media foi boa! PARABENS!' if m>= 6.0 else 'Sua media foi ruim! ESTUDE MAIS!')  # operador ternário equivalente ao if/else acima
