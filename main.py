usuarios = []

def carregar_usuarios():
    """Carrega usuários do arquivo (implementar depois)"""
    pass

def salvar_usuarios():
    """Salva usuários no arquivo (implementar depois)"""
    pass

def criar_usuario():
    try:
        cpf = input("Digite o CPF: ")
        if buscar_usuario_por_cpf(cpf):
            print("Erro: CPF já cadastrado!")
            return False
        
        usuario = {
            "nome": input("Digite o nome: "),
            "cpf": cpf,
            "endereco": input("Digite o endereço: "),
            "numero": int(input("Digite o número: ")),
            "cep": input("Digite o CEP: "),
            "emails": [],
            "telefones": [],
            "data_nasc": input("Digite a data de nascimento: "),
            "profissao": input("Digite a profissão: ")
        }

        while True:
            email = input("Digite um email (ou 'sair' para terminar): ")
            if email.lower() == 'sair':
                break
            usuario["emails"].append(email)

        while True:
            telefone = input("Digite um telefone (ou 'sair' para terminar): ")
            if telefone.lower() == 'sair':
                break
            usuario["telefones"].append(telefone)

        usuarios.append(usuario)
        print(f"Usuário {usuario['nome']} adicionado com sucesso!")
        return True

    except ValueError:
        print("Erro: por favor, insira um número válido para o campo 'numero'.")
        return False
    except Exception as e:
        print(f"Erro ao criar usuário: {str(e)}")
        return False

def excluir_usuario():
    if not usuarios:
        print("Nenhum usuário cadastrado!")
        return False
    
    try:
        cpf = input("Digite o CPF do usuário que deseja excluir: ")
        usuario = buscar_usuario_por_cpf(cpf)
        
        if usuario:
            print("\nDados do usuário a ser excluído:")
            mostrar_usuario(usuario)
            
            confirmacao = input("\nTem certeza que deseja excluir este usuário? (s/n): ")
            if confirmacao.lower() == 's':
                usuarios.remove(usuario)
                print(f"\nUsuário {usuario['nome']} excluído com sucesso!")
                return True
            else:
                print("\nOperação cancelada!")
                return False
        else:
            print("Usuário não encontrado!")
            return False
            
    except Exception as e:
        print(f"Erro ao excluir usuário: {str(e)}")
        return False

# def editar_usuario():

def listar_usuarios():
    while True:
        print("\nListar Usuários:")
        print("1. Listar todos os usuários")
        print("2. Buscar usuário específico")
        print("3. Voltar")
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 1:
                if not usuarios:
                    print("Nenhum usuário cadastrado!")
                    return
                
                for i, usuario in enumerate(usuarios, 1):
                    print(f"\nUsuário {i}:")
                    mostrar_usuario(usuario)
                    
            elif opcao == 2:
                if not usuarios:
                    print("Nenhum usuário cadastrado!")
                    return
                
                cpf = input("Digite o CPF do usuário: ")
                usuario = buscar_usuario_por_cpf(cpf)
                if usuario:
                    mostrar_usuario(usuario)
                else:
                    print("Usuário não encontrado!")
                    
            elif opcao == 3:
                return
            else:
                print("Opção inválida!")
                
        except ValueError:
            print("Por favor, digite um número válido!")

def mostrar_usuario(usuario):
    print(f"Nome: {usuario['nome']}")
    print(f"CPF: {usuario['cpf']}")
    print(f"Endereço: {usuario['endereco']}, {usuario['numero']}")
    print(f"CEP: {usuario['cep']}")
    print(f"Data de Nascimento: {usuario['data_nasc']}")
    print(f"Profissão: {usuario['profissao']}")
    print("Emails:", ", ".join(usuario['emails']))
    print("Telefones:", ", ".join(usuario['telefones']))
    print("-" * 50)

def buscar_usuario_por_cpf(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def menu_usuario():
    while True:
        print("\nMenu de Usuários:")
        print("1. Ver lista de usuários")
        print("2. Editar usuários")
        print("3. Criar um novo usuário")
        print("4. Deletar um usuário")
        print("5. Voltar")
        print("6. Sair do Programa")
        
        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                listar_usuarios()
            elif opcao == 2:
                print("Este serviço não está disponível!\n")
            elif opcao == 3:
                criar_usuario()
            elif opcao == 4:
                excluir_usuario()
            elif opcao == 5:
                return True
            elif opcao == 6:
                return False
            else:
                print("Opção inválida!")
        except ValueError:
            print("Por favor, digite um número válido!")

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Usuários")
        print("2. Livros")
        print("3. Empréstimos")
        print("4. Relatórios")
        print("5. Sair")
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 1:
                if not menu_usuario():
                    break
            elif opcao == 2:
                print("Este serviço não está disponível!")
            elif opcao == 3:
                print("Este serviço não está disponível!")
            elif opcao == 4:
                print("Este serviço não está disponível!")
            elif opcao == 5:
                print("Encerrando o programa!")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Por favor, digite um número válido!")

if __name__ == "__main__":
    carregar_usuarios()
    menu_principal()
    salvar_usuarios()