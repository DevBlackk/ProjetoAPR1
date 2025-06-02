def carregar_usuarios():
    """Carrega usuários do arquivo (implementar depois)"""
    # Implementar leitura do arquivo
    return []

def salvar_usuarios(usuarios):
    """Salva usuários no arquivo (implementar depois)"""
    pass

def criar_usuario(usuarios):
    try:
        cpf = input("Digite o CPF: ")
        if buscar_usuario_por_cpf(usuarios, cpf):
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

def excluir_usuario(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado!")
        return False
    
    try:
        cpf = input("Digite o CPF do usuário que deseja excluir: ")
        usuario = buscar_usuario_por_cpf(usuarios, cpf)
        
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

def editar_usuario(usuarios):
    if not usuarios:
        print("nenhum usuário cadastrado!")
        return False
    
    try:
        cpf = input("Digite o CPF do usuário que deseja editar: ")
        usuario = buscar_usuario_por_cpf(usuarios, cpf)
        
        if usuario:
            print("\nDados atuais do usuário:")
            mostrar_usuario(usuario)
            
            print("\nEdição dos dados:")
            print("Prescione ENTER para manter o valor atual")
            
            nome = input(f"Nome [{usuario['nome']}]: ")
            endereco = input(f"Endereço [{usuario['endereco']}]: ")
            numero = input(f"Número [{usuario['numero']}]: ")
            cep = input(f"CEP [{usuario['cep']}]: ")
            data_nasc = input(f"Data de Nascimento [{usuario['data_nasc']}]: ")
            profissao = input(f"Profissão [{usuario['profissao']}]: ")
            
            if nome: usuario['nome'] = nome
            if endereco: usuario['endereco'] = endereco
            if numero: usuario['numero'] = int(numero)
            if cep: usuario['cep'] = cep
            if data_nasc: usuario['data_nasc'] = data_nasc
            if profissao: usuario['profissao'] = profissao
            
            print("\nEditar Emails:")
            print("1. Manter emails atuais")
            print("2. Adicionar novo email")
            print("3. Remover email existente")
            print("3. Remover email existente")
            print("4. Substituir todos os emails")
            
            op_email = input("Escolaha uma opção : ")
            if op_email == "2":
                while True:
                    email = input("Digite o novo email (ou 'sair' para terminar): ")
                    if email.lower() == 'sair':
                        break
                    usuario["emails"].append(email)
            elif op_email == "3":
                for i, email in enumerate(usuario["emails"]):
                    print(f"{i + 1}. {email}")
                idx = int(input("Digite o número do email para remover: ")) - 1
                if 0 <= idx < len(usuario["emails"]):
                    del usuario["emails"][idx]
            elif op_email == "4":
                usuario["emails"] = []
                while True:
                    email = input("Digite o nove email (ou 'sair' para terminar): ")
                    if email.lower() == 'sair':
                        break
                    usuario["emails"].append(email)
            
            print("\nEditar telefones:")
            print("1. Manter telefones atuais")
            print("2. Adicionar novo telefone")
            print("3. Manter telefone existente")
            print("1. Substituir todos os telefones")
            
            op_tel = input("Escolaha uma opção : ")
            if op_tel == "2":
                while True:
                    tel = input("Digite o novo telefone (ou 'sair' para terminar): ")
                    if tel.lower() == 'sair':
                        break
                    usuario["telefones"].append(tel)
            elif op_tel == "3":
                for i, tel in enumerate(usuario["telefones"]):
                    print(f"{i + 1}. {tel}")
                idx = int(input("Digite o número do telefone para remover: ")) - 1
                if 0 <= idx < len(usuario["telefones"]):
                    del usuario["telefones"][idx]
            elif op_tel == "4":
                usuario["telefones"] = []
                while True:
                    tel = input("Digite o nove telefone (ou 'sair' para terminar): ")
                    if tel.lower() == 'sair':
                        break
                    usuario["telefones"].append(tel)
            
            print("\nUsuário atualizado com sucesso!")
            return True
        else:
            print("Usuário não encontrado!")
            return False
        
    except ValueError as e:
        print(f"Erro: valor inválido inserido - {str(e)}")
        return False
    except Exception as e:
        print(f"Erro ao editar usuário: {str(e)}")
        return False


def listar_usuarios(usuarios):
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
                usuario = buscar_usuario_por_cpf(usuarios, cpf)
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
    
    if 'emails' in usuario and isinstance(usuario['emails'], list):
        print("Emails:", ", ".join(usuario['emails']))
    elif 'email' in usuario:  # Para compatibilidade com dados existentes
        print("Email:", usuario['email'])
    else:
        print("Emails: Nenhum email cadastrado")
    
    if 'telefones' in usuario and isinstance(usuario['telefones'], list):
        print("Telefones:", ", ".join(usuario['telefones']))
    else:
        print("Telefones: Nenhum telefone cadastrado")
    
    print("-" * 50)

def buscar_usuario_por_cpf(usuarios, cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def menu_usuario(usuarios):
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
                listar_usuarios(usuarios)
            elif opcao == 2:
                editar_usuario(usuarios)
            elif opcao == 3:
                criar_usuario(usuarios)
            elif opcao == 4:
                excluir_usuario(usuarios)
            elif opcao == 5:
                return True
            elif opcao == 6:
                return False
            else:
                print("Opção inválida!")
        except ValueError:
            print("Por favor, digite um número válido!")

def menu_principal(usuarios):
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
                if not menu_usuario(usuarios):
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

def main():
    usuarios = [
        {"nome": "Camila Alves", "endereco": "Rua das Acácias", "numero": "101", "cep": "01002-010", "data_nasc": "10/05/1990", "profissao": "Arquiteta", "cpf": "111.222.333-01", "email": "camila.alves@emailficticio.com.br"},
        {"nome": "Bruno Costa", "endereco": "Avenida Ipiranga", "numero": "202", "cep": "02003-020", "data_nasc": "25/08/1982", "profissao": "Contador", "cpf": "222.333.444-02", "email": "bruno.costa82@meuemail.com"},
        {"nome": "Larissa Dias", "endereco": "Travessa dos Lírios", "numero": "30", "cep": "03004-030", "data_nasc": "12/01/1995", "profissao": "Psicóloga", "cpf": "333.444.555-03", "email": "lari.dias.psi@emailseguro.net"},
        {"nome": "Rodrigo Ferreira", "endereco": "Alameda das Gardênias", "numero": "404", "cep": "04005-040", "data_nasc": "03/11/1979", "profissao": "Jornalista", "cpf": "444.555.666-04", "email": "rodrigo.ferreira.jorn@provedorexemplo.com"},
        {"nome": "Sofia Gomes", "endereco": "Rua dos Girassóis", "numero": "505", "cep": "05006-050", "data_nasc": "18/07/2001", "profissao": "Estudante", "cpf": "555.666.777-05", "email": "sofia.g2001@emailuniversitario.edu.br"},
        {"nome": "Thiago Lima", "endereco": "Avenida Rebouças", "numero": "606", "cep": "06007-060", "data_nasc": "29/04/1988", "profissao": "Desenvolvedor Web", "cpf": "666.777.888-06", "email": "thiago.dev@webmailficticio.com"},
        {"nome": "Gabriela Martins", "endereco": "Praça Roosevelt", "numero": "70", "cep": "07008-070", "data_nasc": "07/09/1993", "profissao": "Publicitária", "cpf": "777.888.999-07", "email": "gabi.martins.publi@emailcriativo.com.br"},
        {"nome": "Daniel Nunes", "endereco": "Rua da Consolação", "numero": "808", "cep": "08009-080", "data_nasc": "14/02/1975", "profissao": "Engenheiro Civil", "cpf": "888.999.000-08", "email": "daniel.nunes.eng@meuprovedor.com"},
        {"nome": "Isabela Oliveira", "endereco": "Avenida Angélica", "numero": "909", "cep": "09010-090", "data_nasc": "21/06/1999", "profissao": "Fisioterapeuta", "cpf": "999.000.111-09", "email": "isa.oliveira.fisio@emaildesaude.com"},
        {"nome": "Leonardo Pereira", "endereco": "Rua Frei Caneca", "numero": "110", "cep": "01011-100", "data_nasc": "01/12/1986", "profissao": "Chef de Cozinha", "cpf": "000.111.222-10", "email": "leo.chef.pereira@saborearte.com.br"},
        {"nome": "Amanda Ribeiro", "endereco": "Largo do Arouche", "numero": "22", "cep": "02012-110", "data_nasc": "05/10/1991", "profissao": "Veterinária", "cpf": "123.456.789-11", "email": "amanda.vet.ribeiro@mundoanimalemail.com"},
        {"nome": "Felipe Santos", "endereco": "Rua Bela Cintra", "numero": "330", "cep": "03013-120", "data_nasc": "16/03/1983", "profissao": "Fotógrafo", "cpf": "234.567.890-12", "email": "felipe.santos.foto@cliquemail.com.br"},
        {"nome": "Clara Souza", "endereco": "Avenida Brigadeiro Faria Lima", "numero": "440", "cep": "04014-130", "data_nasc": "28/08/1997", "profissao": "Analista de Marketing", "cpf": "345.678.901-13", "email": "clara.mkt.souza@estrategiaemail.com"},
        {"nome": "Vinicius Teixeira", "endereco": "Rua Oscar Freire", "numero": "550", "cep": "05015-140", "data_nasc": "11/05/1970", "profissao": "Empresário", "cpf": "456.789.012-14", "email": "vinicius.teixeira@negociosonline.com.br"},
        {"nome": "Yasmin Vieira", "endereco": "Alameda Jaú", "numero": "66", "cep": "06016-150", "data_nasc": "23/09/1994", "profissao": "Nutricionista", "cpf": "567.890.123-15", "email": "yasmin.nutri.vieira@vidasaudavelemail.com"},
        {"nome": "Pedro Azevedo", "endereco": "Rua Haddock Lobo", "numero": "770", "cep": "07017-160", "data_nasc": "09/07/1980", "profissao": "Economista", "cpf": "678.901.234-16", "email": "pedro.azevedo.econ@analisefinanceira.com.br"},
        {"nome": "Laura Barros", "endereco": "Avenida Pacaembu", "numero": "880", "cep": "08018-170", "data_nasc": "02/02/2000", "profissao": "Designer de Interiores", "cpf": "789.012.345-17", "email": "laura.barros.design@ambientemail.com"},
        {"nome": "Guilherme Carvalho", "endereco": "Rua Itapeva", "numero": "99", "cep": "09019-180", "data_nasc": "13/10/1987", "profissao": "Consultor Financeiro", "cpf": "890.123.456-18", "email": "gui.carvalho.fin@consultoriaemail.com.br"},
        {"nome": "Manuela Castro", "endereco": "Praça Charles Miller", "numero": "121", "cep": "01020-190", "data_nasc": "20/04/1996", "profissao": "Personal Trainer", "cpf": "901.234.567-19", "email": "manu.castro.fit@treinoemail.com"},
        {"nome": "Enzo Cunha", "endereco": "Rua Pamplona", "numero": "212", "cep": "02021-200", "data_nasc": "06/11/1981", "profissao": "Piloto de Avião", "cpf": "012.345.678-20", "email": "enzo.piloto.cunha@voandomail.com.br"},
        {"nome": "Helena Dantas", "endereco": "Avenida Higienópolis", "numero": "313", "cep": "03022-210", "data_nasc": "17/01/1992", "profissao": "Bióloga", "cpf": "109.876.543-21", "email": "helena.dantas.bio@naturezamail.com"},
        {"nome": "Igor Esteves", "endereco": "Rua Maria Antônia", "numero": "414", "cep": "04023-220", "data_nasc": "27/05/1977", "profissao": "Mecânico", "cpf": "210.987.654-22", "email": "igor.mecanico@oficinaemail.com.br"},
        {"nome": "Júlia Farias", "endereco": "Alameda Lorena", "numero": "515", "cep": "05024-230", "data_nasc": "04/08/1989", "profissao": "Farmacêutica", "cpf": "321.098.765-23", "email": "julia.farias.farma@cuidadoemail.com"},
        {"nome": "Murilo Fernandes", "endereco": "Rua Estados Unidos", "numero": "616", "cep": "06025-240", "data_nasc": "10/06/1998", "profissao": "Técnico de Informática", "cpf": "432.109.876-24", "email": "murilo.ti.fernandes@suporteemail.net"},
        {"nome": "Alice Xavier", "endereco": "Rua Gabriel Monteiro da Silva", "numero": "717", "cep": "07026-250", "data_nasc": "22/12/1984", "profissao": "Dentista", "cpf": "543.210.987-25", "email": "alice.xavier.odonto@sorrisomail.com.br"}
    ]
    
    menu_principal(usuarios)
    salvar_usuarios(usuarios)

if __name__ == "__main__":
    main()