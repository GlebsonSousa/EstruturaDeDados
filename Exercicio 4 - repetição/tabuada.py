texto_A = 'Digite um numero: '
texto_B = '\nVocê digitou um caracter invalido \nDigite um valor numerico inteiro:'

def entrada_usuario(erro):
    try:
        if erro == False:
            print('\n')
            entrada = input(texto_A)
            return int(entrada)
        else:
            print('\n')
            entrada = input(texto_B)
            return int(entrada)
        
    except ValueError:
        return entrada_usuario(erro=True)
    

def calcula_tabuada(entrada):
    print('\n')
    for i in range(11):  
        print(f"{entrada} x {i} = {entrada * i}")
    print('\n')


calcula_tabuada(entrada_usuario(erro=False))