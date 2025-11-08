Lista_de_ingredientes = []


def adicionarIngrediente(ingrediente):
    Lista_de_ingredientes.append(ingrediente)
    print(ingrediente, "foi adicionado ao pedido!")


def removerIngrediente():
    if len(Lista_de_ingredientes) == 0:
        print("O sanduíche está vazio! Nada para remover.")
    else:
        aRemover = Lista_de_ingredientes[-1]
        Lista_de_ingredientes.pop()
        print(aRemover, "foi retirado do pedido!")
        return aRemover


def mostraSanduiche():
    if len(Lista_de_ingredientes) == 0:
        print("\nO sanduíche ainda está vazio!")
    else:
        contador = 1
        print('\nIngredientes adicionados:\n')
        for i in Lista_de_ingredientes:
            print(f'{contador}. {i}')
            contador += 1


def verUltimoIngrediente():
    if len(Lista_de_ingredientes) == 0:
        print("O sanduíche está vazio! Nenhum ingrediente adicionado ainda.")
    else:
        print(Lista_de_ingredientes[-1], "foi o último ingrediente adicionado.")


def menu():
    print('\n\n------ Menu ------\n')
    print('1 - Adicionar ingrediente')
    print('2 - Remover ingrediente')
    print('3 - Mostrar sanduíche')
    print('4 - Ver último ingrediente adicionado')
    print('5 - Finalizar pedido')

    try:
        opcaoEscolhida = int(input("\nEscolha uma opção: "))
        if (opcaoEscolhida >= 1 and opcaoEscolhida <= 5):

            if opcaoEscolhida == 1:
                novoIngrediente = input('Informe o nome do ingrediente: ')
                adicionarIngrediente(novoIngrediente)
                menu()

            elif opcaoEscolhida == 2:
                removerIngrediente()
                menu()

            elif opcaoEscolhida == 3:
                mostraSanduiche()
                menu()

            elif opcaoEscolhida == 4:
                verUltimoIngrediente()
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
    print(f"\nSeu pedido de sanduíche com {Lista_de_ingredientes} está pronto!")
    exit()


# Execução principal
menu()
