
############################################################################################
def adicionar_tarefa(nome_tarefa, tarefas):
    tarefa = {
        "nome": nome_tarefa, 
        "completada": False
    }
    tarefas.append(tarefa)
    print(f"A tarefa '{nome_tarefa}' foi adicionada com sucesso!")
    return
    
############################################################################################
def ver_tarefas(tarefas):
    print("\nLista de tarefas:")

    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["nome"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

############################################################################################
def renomear_tarefa(tarefas, indice, novo_nome):
        indice = int(indice) - 1
        if indice >= 0 and indice < len(tarefas):
            tarefas[indice]["nome"] = novo_nome
            print(f"Tarefa {indice} atualizada para {novo_nome}")
        else:
            print("Insira um número válido.")
            return

############################################################################################
def finalizar_tarefa(indice, tarefas):
    indice = int(indice) - 1
    tarefas[indice]["completada"] = True
    print(f"Tarefa finalizada com sucesso!")
    return

############################################################################################
def deletar_finalizadas(tarefas):
    for item in tarefas:
        if item["completada"]:
            tarefas.remove(item)
    print("Tarefas finalizadas foram deletadas.")
    return

############################################################################################

lista_de_tarefas = []

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Renomear tarefa")
    print("4. Finalizar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input ("Digite a sua escolha: ")

    if escolha == "1":
        nome_da_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(nome_da_tarefa, lista_de_tarefas)

    elif escolha == "2":
        ver_tarefas(lista_de_tarefas)

    elif escolha == "3":
        ver_tarefas(lista_de_tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja renomear: ")
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        renomear_tarefa(lista_de_tarefas, indice_tarefa, novo_nome_tarefa)

    elif escolha == "4":
        ver_tarefas(lista_de_tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja finalizar: ")
        finalizar_tarefa(indice_tarefa, lista_de_tarefas)

    elif escolha == "5":
        deletar_finalizadas(lista_de_tarefas)
        ver_tarefas(lista_de_tarefas)

    else:
        escolha == "6"
        break

print ("Programa finalizado")

