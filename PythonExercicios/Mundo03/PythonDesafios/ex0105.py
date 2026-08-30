def notas(*n, sit=False):
    '''
        -> Função para analisar notas e situações de vários alunos.
    : param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    : return: dicionário com várias informações sobre a situação da turma.
    '''
    dicionario = dict()
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n)/len(n)
    # maior =  menor = soma = 0
    # c = 0
    # while c < dicionario['total']:
    #     soma += n[c]
    #     if c == 0:
    #         maior = menor = n[c]
    #     else:
    #         if maior < n[c]:
    #             maior = n[c]
    #         if menor > n[c]:
    #             menor = n[c]
    #     c += 1
    # dicionario['maior'] = maior
    # dicionario['menor'] = menor
    # dicionario['media'] = soma / dicionario['total']
    if sit:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'BOA'
        elif 7 > dicionario['media'] >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario


resp = notas(5.5, 9.5, 6.5, 10, sit=True)
print(resp)