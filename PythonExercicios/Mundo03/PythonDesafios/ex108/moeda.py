def Aumentar(valor=0, porcentagem=0):
    resp = (valor + (valor * (porcentagem / 100)))
    return resp

def Diminuir(valor=0, porcentagem=0):
    resp = (valor - (valor * (porcentagem / 100)))
    return resp

def Dobro(valor=0):
    resp = (valor * 2)
    return resp

def Metade(valor=0):
    resp = (valor / 2)
    return resp

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')