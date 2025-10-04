vogais = ['a','e','i','o','u','A','E','I','O','U']

entrada_crua = input('Digite uma palavra: ')

entrada = list(entrada_crua)

qt_vogais = 0

vogais_localizadas = []

for i in entrada:
    for b in vogais:
        if i == b:
            vogais_localizadas.append(b)
            qt_vogais = len(vogais_localizadas)


print(f'A palavra {entrada} tem {qt_vogais} vogais')
print(f'As vogais localizadas em {entrada_crua} foram: {vogais_localizadas}')

