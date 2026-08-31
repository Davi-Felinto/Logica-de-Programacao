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