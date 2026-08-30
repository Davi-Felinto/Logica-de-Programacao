def Voto(anoNas):
    from datetime import date
    idade = date.today().year - anoNas
    if idade < 16:
        return f'Com {idade} anos: Não Votar.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: Voto Opcional.'
    else:
        return f'Com {idade} anos: Voto Obrigatorio'

print('-'*30)
print(Voto(int(input('Em q ano vc nasceu? '))))