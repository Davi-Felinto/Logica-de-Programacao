# Exercício 008: converte uma distância em metros para outras unidades de medida

m = float(input('Uma distancia em metros: '))  # lê a distância em metros

# Tabela de conversão: km (÷1000), hm (÷100), dam (÷10), dm (×10), cm (×100), mm (×1000)
print(f'A medida de {m} corresponde a \n{m/1000}km \n{m/100}hm \n{m/10}dam \n{m*10:.0f}dm \n{m*100:.0f}cm \n{m*1000:.0f}mm')
