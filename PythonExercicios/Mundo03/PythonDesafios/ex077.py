palavras = ('aprender', 'programar', 'liguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar', 
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper():^15} temos ', end='')
    for letra in p:
        print(letra, end=' ') if letra.lower() in 'aeiou' else letra