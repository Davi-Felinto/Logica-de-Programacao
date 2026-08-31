def Aumentar(valor, porcentagem):
    resp = (valor + (valor * (porcentagem / 100)))
    return resp

def Diminuir(valor, porcentagem):
    resp = (valor - (valor * (porcentagem / 100)))
    return resp

def Dobro(valor):
    resp = (valor * 2)
    return resp

def Metade(valor):
    resp = (valor / 2)
    return resp