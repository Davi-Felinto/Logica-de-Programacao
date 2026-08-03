from random import randint

print(f'{' LOJAS GUANABARA ':=^40}')
paga = float(input('Preço das compras: R$'))
if paga == 0:
    paga = randint(30, 10000)
    print('=='*5, 'LOJAS GUANABARA', '=='*5)
    print('Preço das compras: R${}'.format(paga))

print('''FROMASDE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a OPÇÃO? '))

if opcao == 1:
    print(f'Sua compra de R${paga:.2f} vai custar R${(paga * 0.90):.2f}')
elif opcao == 2:
    print(f'Sua compra de R${paga:.2f} vai custar R${(paga * 0.95):.2f}')
elif opcao == 3:
    print(f'Sua compra sera parcelada em 2x de R${paga/2}')
    print(f'Sua compra de R${paga:.2f} vai custar R${(paga):.2f}')
elif opcao == 4:
    num_parc = int(input('Quantas parcelas? '))
    tot_paga = paga*1.20
    parc = tot_paga/num_parc
    print(f'Sua compra sera parcelada em {num_parc}x de R${parc:.2f} COM JUROS')
    print(f'Sua compra de R${paga:.2f} vai custar R${tot_paga:.2f}')
else:
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')
