def menu_principal():
    executando = True
    while executando:
        print("\nMenu Principal:")
        print("1. Usúarios")
        print("2. Livros")
        print("3. Empréstimos")
        print("4. Relatórios")
        print("5. Sair")
        
        opcao = int(input("\nEscolha uma opção: "))
        if opcao == 1:
            if not menu_usuario():
                executando = False
        elif opcao == 2:
            print("Este serviço não esta disponivel!")
        elif opcao == 3:
            print("Este serviço não esta disponivel!")
        elif opcao == 4:
            print("Este serviço não esta disponivel!")
        elif opcao == 5:
            print("Encerrando o programa!")
            executando = False
        else:
            print("Opção inválida! Por favor, digite uma das opções acima.")

def menu_usuario():
    sem_menu_usuario = True
    while sem_menu_usuario:
        print("\nMenu de usúarios:")
        print("1. Ver lista de usúarios")
        print("2. Editar usúarios")
        print("3. Criar um novo usúario")
        print("4. Deletar um usúario")
        print("5. Voltar")
        print("6. Sair do Programa")
        
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            print("Este serviço não diponivel!\n")
        elif opcao == 2:
            print("Este serviço não diponivel!\n")
        elif opcao == 3:
            print("Este serviço não diponivel!\n")
        elif opcao == 4:
            print("Este serviço não diponivel!\n")
        elif opcao == 5:
            return True
        elif opcao == 6:
            return False
        else:
            print("Opção invalida! Por favor, digite uma das opções acima.")

def main():
    menu_principal()
main()