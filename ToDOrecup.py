tarefas = []
def cadastro_tarefa():
    print("Cadastro de Tarefa")
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("tarefa cadastrada com sucesso")
def listar_tarefas():
    print("Lista de Tarefas")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")
    input("press enter for skip")
def alterar_tarefa():
    print("Alterar Tarefa")
    listar_tarefas()
    indice = int(input("Digite o numero da tarefa a ser alterada: ")) - 1
    nova_tarefa = input("Digite a nova descrição da tarefa: ")
    tarefas[indice] = nova_tarefa
    print("Tarefa alterada com sucesso!")
    print("Número de tarefa inválido.")
def excluir_tarefa():
    print("Excluir Tarefa")
    listar_tarefas()
    indice = int(input(" \n digite o número da tarefa a ser excluida \n ")) - 1
    tarefa_excluida = tarefas.pop(indice)
    print(f"Tarefa '{tarefa_excluida}' excluida com sucesso")
while True:
    print("=== Gerenciador de Tarefas === \n")
    print("1 - Cadastra Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Alterar Tarefa")
    print("4 - Excluir Tarefas")
    print("5 - Sair")
    opcao = input("\n digite a opção desejada: ")
    if opcao == "1":
        cadastro_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        alterar_tarefa()
    elif opcao == "4":
        excluir_tarefa()
    elif opcao == "5":
        break
