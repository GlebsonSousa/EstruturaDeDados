listaCompilacao = []
 
def adicionarTarefa(processo):
  listaCompilacao.append(processo)
  print(f"Processo {processo} entrou na fila de compilação!")
  menu()
 
def compilartarefas():
  ultimaTarefa = listaCompilacao[0]
  listaCompilacao.remove(ultimaTarefa)
  print(f"Tarefa {ultimaTarefa} executada com sucesso!")
  return ultimaTarefa
 
def filaProcessos():
  contador = 1
  print("\n Processos pendentes: \n")
  for i in listaCompilacao:
    print(f"{contador} . {i}")
    contador +=1
 
def encerrar():
    exit()
 
def menu():
 
  print("\n\n-----MENU-----\n\n")
  print(f"1 - Adicionar tarefa \n2 - Compilar tarefas \n3 - Compilar Tarefa(rodar programa)\n4 - Sair do programa4")
  try:
    entradaUsuario = int(input('Digite sua escolha de 1 a 4: '))
 
    if entradaUsuario == 1:
      entradaTarefa = input('Digite a tarefa que deve ser adicionada: ')
      adicionarTarefa(entradaTarefa)
      menu()
    elif entradaUsuario == 2:
      filaProcessos()
      menu()
    elif entradaUsuario == 3:
      compilartarefas()
      menu()
    elif entradaUsuario == 's':
      exit()
  except:
    print('Digite uma entrada válida !!!\n\n')
    menu()
 
 
menu()