def menu_principal():
    print("1. Usúarios")
    print("2. Livros")
    print("3. Empréstimos")
    print("4. Relatórios")
    print("5. Sair")
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        menu_usuario()
    elif opcao == 2:
        print("Este serviço não diponivel!")
    elif opcao == 3:
        print("Este serviço não diponivel!")
    elif opcao == 4:
        print("Este serviço não diponivel!")
    else:
        print("Enserrando o programa!")

def menu_usuario():
    print("\nMenu de usúarios:")
    print("1. Ver lista de usúarios")
    print("2. Editar usúarios")
    print("3. Criar um novo usúario")
    print("4. Deletar um usúario")
    print("5. Voltar")
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        print("Este serviço não diponivel!\n")
        menu_principal()
    elif opcao == 2:
        print("Este serviço não diponivel!\n")
        menu_principal()
    elif opcao == 3:
        print("Este serviço não diponivel!\n")
        menu_principal()
    elif opcao == 4:
        print("Este serviço não diponivel!\n")
        menu_principal()
    elif opcao == 5:
        menu_principal()
    else:
        print("Opção invalida! Por favor, digite uma das opções acima.\n")
        menu_usuario()

def main():
    menu_principal()

main()