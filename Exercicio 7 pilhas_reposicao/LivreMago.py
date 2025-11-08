Lista_de_magias = []

def adicionar_magia(magia):
  Lista_de_magias.append(magia)
  print(magia, "Foi carregada.")

def usar_magia():
  if len(Lista_de_magias) == 0:
    print("Nenhuma mágia carregada!!!")
  else:
    usar_magia = Lista_de_magias [-1]
    Lista_de_magias.pop()
    print(f"O mago utilizou {usar_magia} !!!!")
    return usar_magia

def magiasCarregadas():
    if len(Lista_de_magias) == 0:
        print("\nNenhuma magia carregada!!!!!")
    else:
        contador = 1
        print('\nNovas magias carregadas:\n')
        for i in Lista_de_magias:
            print(f'{contador}. {i}')
            contador += 1

def verUltimaMagia():
    if len(Lista_de_magias) == 0:
        print("Nenhuma magia carregada!!! Carregue seu Poder!!!!")
    else:
        print(Lista_de_magias[-1], "foi a última magia carregada.")

def menu():
    print('\n\n------ Menu ------\n')
    print('1 - Carregar Magia')
    print('2 - Usar Magia')
    print('3 - Mostrar Magias Carregadas')
    print('4 - Ver última Magia Carregada.')
    print('5 - Finalizar Combate.')

    try:
        opcaoEscolhida = int(input("\nEscolha uma opção: "))
        if (opcaoEscolhida >= 1 and opcaoEscolhida <= 5):

            if opcaoEscolhida == 1:
                novaMagia = input('Informe o nome da magia: ')
                adicionar_magia(novaMagia)
                menu()

            elif opcaoEscolhida == 2:
                usar_magia()
                menu()

            elif opcaoEscolhida == 3:
                magiasCarregadas()
                menu()

            elif opcaoEscolhida == 4:
                verUltimaMagia()
                menu()

            elif opcaoEscolhida == 5:
                sair()
        else:
            print('\nVocê digitou uma opção inválida.\nPor favor, informe um número de 1 a 5.\n')
            menu()

    except ValueError:
        print('\nVocê digitou uma opção inválida.\nPor favor, informe um número de 1 a 5.\n')
        menu()


def sair():
    print(f"\nSua aventura foi concluída, você usou bem as suas magias: {Lista_de_magias}.")
    exit()


# Execução principal
menu()