from random import randint

menorNumeroPossivel = 0
maiorNumeroPossivel = 10
tentativas = 5
tentativa_atual = 1

def entrada_usuario():
    try:
        entrada = input(f'Chute um número entre {menorNumeroPossivel} e {maiorNumeroPossivel}: ')
        return int(entrada)
    except ValueError:
        print('Entrada inválida!!!')
        return entrada_usuario()

def sorteia_numero():
    return randint(menorNumeroPossivel, maiorNumeroPossivel)

numero_sorteado = sorteia_numero()
entrada = entrada_usuario()

while entrada != numero_sorteado and tentativa_atual <= tentativas:
    if entrada > numero_sorteado:
        print('🔽 Chute um número menor!')
    elif entrada < numero_sorteado:
        print('🔼 Chute um número maior!')

    print(f'Tentativa atual: {tentativa_atual} de {tentativas}\n')
    tentativa_atual += 1

    if tentativa_atual > tentativas:
        break

    entrada = entrada_usuario()

if entrada == numero_sorteado:
    print('Parabéns, você acertou!')
else:
    print(f'Você tentou {tentativas} vezes e errou. O número era {numero_sorteado}.')
