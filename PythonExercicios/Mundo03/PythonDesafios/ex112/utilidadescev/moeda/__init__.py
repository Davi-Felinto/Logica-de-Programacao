def Aumentar(valor=0, porcentagem=0, formatacao=False):
    resp = (valor + (valor * (porcentagem / 100)))
    return resp if formatacao is False else moeda(resp)

def Diminuir(valor=0, porcentagem=0, formatacao=False):
    resp = (valor - (valor * (porcentagem / 100)))
    return resp if formatacao is False else moeda(resp)

def Dobro(valor=0, formatacao=False):
    resp = (valor * 2)
    return resp if formatacao is False else moeda(resp)

def Metade(valor=0, formatacao=False):
    resp = (valor / 2)
    return resp if formatacao is False else moeda(resp)

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(valor, porcentagemAumentar, porcentagemDiminuir):
    print('-'*35)
    print('RESUMO DO VALOR'.center(35))
    print('-'*35)
    print(f"{'Preço analisado:':<15}", f"{'':^7}", f"{moeda(valor):>8}")
    print(f"{'Dobro do preço:':<15}", f"{'':^7}", f"{Dobro(valor, True):>8}")
    print(f"{'Metade do preço:':<15}", f"{'':^7}", f"{Metade(valor, True):>8}")
    print(f'{porcentagemAumentar:2}',(f"% de aumentor:").ljust(13), f"{'':^7}", f"{Aumentar(valor, porcentagemAumentar, True):>8}")
    print(f'{porcentagemDiminuir:2}',(f"% de redução:").ljust(13), f"{'':^7}", f"{Diminuir(valor, porcentagemDiminuir, True):>8}")
    print('-'*35)