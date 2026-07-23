a = input('Digite algo: ')
# Analisando oq foi escrito 
print('O tipo primitivo desse valor é', type(a)) #Tipo primitivo
print('Só tem espaços?', a.isspace()) # Tem espaços
print('É um numero?', a.isnumeric()) # É um numero
print('É alfabetico?', a.isalpha()) # É alfabetico
print('É alfanumerico?', a.isalnum()) # É alfanumerico
print('Esta em maiusculas?', a.isupper()) # Esta em maiusculas
print('Esta em minusculas?', a.islower()) # Esta em minusculas
print('Esta capitalizado?', a.istitle()) # Esta capitalizado