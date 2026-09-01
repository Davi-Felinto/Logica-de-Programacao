try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    r = a /b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voê digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir por zero!')
except KeyboardInterrupt:
    print('O usuario não informou os dados')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')