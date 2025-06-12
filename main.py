### JÁ ACABEI MINHA PARTE, FOFALTA VOCÊ TERMINAR A SUA PRA PODEMOS TESTAR O PROJETO!!!


from datetime import datetime
import os
import time


def menu():
    print('Menu de opções:')
    print('1 - Submenu de Usuários.')
    print('2 - Submenu de Livros.')
    print('3 - Submenu de Empréstimos.')
    print('4 - Submenu Relatórios.')
    print('Digite 0 para encerrar o programa.')
    opcao = input('Escolha uma opção:')
    return opcao
def submenuUsuarios():
    print(f'\n Submenu Usuários:')
    print('1 - Exibir Todos')
    print('2 - Consultar Usuário')
    print('3 - Novo Cadastro')
    print('4 - Editar Usuário')
    print('5 - Excluir Cadastro')
    print('0 - Voltar ao Menu Principal')
    opcao = input('Escolha uma opção:')
    return opcao
def submenuLivros():
    print(f'\n Submenu  de Livros:')
    print('1 - Exibir Todos')
    print('2 - Consultar Livro')
    print('3 - Cadastrar Novo Livro')
    print('4 - Alterar Livro')
    print('5 - Excluir Livro')
    print('0 - Voltar ao Menu Principal')
    opcao = input('Escolha uma opção:')
    return opcao
def submenuEmprestimos():
    print(f'\n Submenu de Empréstimos:')
    print('1 - Exibir Todos')
    print('2 - Consultar Empréstimo')
    print('3 - Cadastrar Novo Empréstimo')
    print('4 - Alterar Empréstimo')
    print('5 - Excluir Empréstimo')
    print('0 - Voltar ao Menu Principal')
    opcao = input('Escolha uma opção:')
    return opcao
def submenuRelatórios():
    print(f'\n Submenu de Relátorios:')
    print('1 - Listar todos os dados de todos os usuários com mais de X anos de idade')
    print('2 - Listar todos os dados de todos os livros que tenham mais do que X autores')
    print('3 - Listar empréstimos realizados entre dd/mm/aaaa e dd/mm/aaaa')
    print('0 - Voltar ao Menu Principal')
    opcao = input('Escolha uma opção:')
    return opcao
def existe_arquivo(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False
usuarios = {
    '07854736103' : ['nome', 'rua', 'nro', 'cep', ['email1', 'email2'], ['telefone1', 'telefone2'], 'nasc', 'profissao'],
    '91325994120' : ['nome', 'rua', 'nro', 'cep', ['email1', 'email2'], ['telefone1', 'telefone2'], 'nasc', 'profissao']
}
def registerUser(usuarios, cpf):
    if cpf in usuarios:
        print('cpf ja cadastrado!')
        return False
    else:
        emails = []
        telefones = []
        dados = []
        nome = input('Digite o nome do usuário:')
        rua = input('Digite o a rua do usuário:')
        nro = input('Digite o número da casa do usuário:')
        cep = input('Digite o CEP do usuário:')
        qtd = int(input('Quantos E-mails deseja adicionar?'))
        for i in range(qtd):
            mail = input(f'Digite o E-mail {i+1}:')
            emails.append(mail)
        qtd2 = int(input('Digite quantos telefones deseja adicionar:'))
        for i in range(qtd2):
            tel = input(f'Digite o telefone {i+1}:')
            telefones.append(tel)
        nasc = input('Digite a data de nascimento do usuário (dd/mm/aaaa):')
        profissao = input('Digite a profissão do usuário:')
        dados.append(nome)
        dados.append(rua)
        dados.append(nro)
        dados.append(cep)
        dados.append(emails)
        dados.append(telefones)
        dados.append(nasc)
        dados.append(profissao)
        usuarios[cpf] = dados
        return True
def deleteUser(usuarios, cpf): 
    if cpf in usuarios:
        del usuarios[cpf]
        print('Cadastro excluído com sucesso!')
    else:
        print('CPF não cadastrado.')
def menuEditUser(usuarios, cpf):
    if cpf in usuarios:
        print('1 - Alterar Nome do Usuário')
        print('2 - Alterar Rua do Usuário')
        print('3 - Alterar Número do Usuário')
        print('4 - Alterar CEP do Usuário')
        print('5 - Alterar E-mails do Usuário')
        print('6 - Alterar Telefones do Usuário') 
        print('7 - Alterar Data de Nascimento do Usuário')
        print('8 - Alterar Profissão do Usuário')
        print('9 - Alterar TODOS os dados do Usuário')
        print('0 - Voltar')
        opc = input('Escolha uma opção:')
        return opc
    else:
        print('CPF não cadastrado.')
def editName(usuarios, cpf):
    nome = input('Informe o novo nome do usuário:')
    usuarios[cpf][0] = nome
def editRua(usuarios, cpf):
    rua = input('Informe a nova rua do usuário:')
    usuarios[cpf][1] = rua
def editNro(usuarios, cpf):
    nro = input('Digite o novo número da casa do usuário:')
    usuarios[cpf][2] = nro
def editCep(usuarios, cpf):
    cep = input('Digite o novo CEP do usuário:')
    usuarios[cpf][3] = cep
def editEmail(usuarios, cpf):
    email = input('Digite o email que deseja alterar:')
    novo_email = input('Digite o email alterado:')
    pos = -1
    for i in range(len(usuarios[cpf][4])):
        if usuarios[cpf][4][i] == email:
            pos = i
    if pos >= 0:
        usuarios[cpf][4][pos] = novo_email
        print()
        return True
    else:
        return False
def editTelefone(usuarios, cpf):
    tel = input('Digite o telefone que deseja alterar:')
    novo_tel = input('Digite o telefone alterado:')
    pos = -1
    for i in range(len(usuarios[cpf][5])):
        if usuarios[cpf][5][i] == tel:
            pos = i
    if pos >=0:
        usuarios[cpf][5][pos] = novo_tel
        return True
    else:
        return False
def editNasc(usuarios,cpf):
    nascimento = input('Digite a nova data de nascimento (dd/mm/aaaa) do usuário:')
    usuarios[cpf][6] = nascimento
def editProfissao(usuarios,cpf):
    profissao = input('Digite a nova profissão do usuário:')
    usuarios[cpf][7] = profissao
def mainEditUser(usuarios, cpf):
    if cpf in usuarios:
        opc = 1
        while opc != 0:
            opc = menuEditUser(usuarios,cpf)
            if opc == '1':
                editName(usuarios, cpf)
                print('Nome alterado com sucesso.')
            elif opc == '2':
                editRua(usuarios, cpf)
                print('Rua alterada com sucesso.')
            elif opc == '3':
                editNro(usuarios, cpf)
                print('Número da casa alterado com sucesso.')
            elif opc == '4':
                editCep(usuarios, cpf)
                print('CEP alterado com sucesso.')
            elif opc == '5':
                editEmail(usuarios, cpf)
                print('E-mail(s) alterados com sucesso.')
            elif opc == '6':
                editTelefone(usuarios, cpf)
                print('Telefone(s) alterados com sucesso.')
            elif opc == '7':
                editNasc(usuarios, cpf)
                print('Data de nascimento alterada com sucesso.')
            elif opc == '8':
                editProfissao(usuarios, cpf)
                print('Profissão alterada com sucesso')
            elif opc == '9':
                submenuUsuarios()
                editRua(usuarios, cpf)
                editNro(usuarios, cpf)
                editCep(usuarios, cpf)
                editEmail(usuarios, cpf)
                editTelefone(usuarios, cpf)
                editNasc(usuarios, cpf)
                editProfissao(usuarios, cpf)
                editName(usuarios, cpf)
                print('Dados alterados com sucesso')
            elif opc == '0':
                submenuUsuarios()
            else:
                print()
                print('Escolha uma opção válida')
                print()
    else:
        print('Digite um CPF válido!')
        mainSubmenuUsuarios(usuarios)
def listUsers(usuarios):
    if len(usuarios) > 0:
        for i in usuarios.keys():
            print(f'CPF: {i}')
            print(f'Nome:{usuarios[i][0]} ')
            print(f'Rua: {usuarios[i][1]}')
            print(f'Número: {usuarios[i][2]}')
            print(f'CEP: {usuarios[i][3]}')
            print(f'E-mails:')
            for j in range(len(usuarios[i][4])):
                print(usuarios[i][4][j])
            for j in range(len(usuarios[i][5])):
                print(usuarios[i][5][j])
            print(f'Data de Nascimento: {usuarios[i][6]}')
            print(f'Profissão: {usuarios[i][7]}')
    else:
        print('Lista de Usuários Vazia')
def listUser(usuarios, cpf):
    if cpf in usuarios:
        print(f'CPF: {cpf}')
        print(f'Nome:{usuarios[cpf][0]} ')
        print(f'Rua: {usuarios[cpf][1]}')
        print(f'Número: {usuarios[cpf][2]}')
        print(f'CEP: {usuarios[cpf][3]}')
        print(f'E-mail(s):')
        for j in range(len(usuarios[cpf][4])):
                print(usuarios[cpf][4][j])
        print('Telefone(s):')
        for j in range(len(usuarios[cpf][5])):
            print(usuarios[cpf][5][j])
        print(f'Data de Nascimento: {usuarios[cpf][6]}')
        print(f'Profissão: {usuarios[cpf][7]}')
    else:
        print('CPF não cadastrado')
def mainSubmenuUsuarios(usuarios):
    opc = 1
    while opc != 0:
        opc = submenuUsuarios()
        if opc == '1':
            print('Listando usuários...')
            listUsers(usuarios)
        elif opc == '2':
            cpf = input('Informe o CPF do usuário que deseja consultar:')
            print('Consultando usuário...')
            listUser(usuarios, cpf)
        elif opc == '3':
            cpf = input('Informe o CPF do usuário que deseja cadastrar:')
            registerUser(usuarios, cpf)
        elif opc == '4':
            cpf = input('Informe o CPF do usuário que deseja editar:')
            mainEditUser(usuarios, cpf)
        elif opc == '5':
            cpf = input('Informe o CPF do usuário que deseja excluir:')
            deleteUser(usuarios, cpf)
        elif opc =='0':
            menu()
        else:
            print()
            print('Escolha uma opção válida!')


#######Livros#######
livros = {
    'Effective Modern C++': [
        '978-0-13-468599-1',
        'Técnico',
        336,
        ['Scott Meyers']
    ],
    'O Nome do Vento': [
        '978-0-7653-2635-5',
        'Fantasia',
        662,
        ['Patrick Rothfuss']
    ],
    'Dom Casmurro': [
        '978-85-359-0277-2',
        'Romance',
        256,
        ['Machado de Assis']
    ]
}

def inserir_livro(livros):
    nome_livro = input("Digite o nome do livro que deseje a adicionar: ")
    if nome_livro in livros:
        print("Livro já existente!")
        return False
    else:
        livros[nome_livro] = []

        isbn = input("Digite o ISBN do livro(999-99-999-9999-9): ")
        livros[nome_livro].append(isbn)

        genero = input("Digite o gênero do livro: ")
        livros[nome_livro].append(genero)

        autores = []
        inserindo_atores = True
        while inserindo_atores:
            autor = input("Informe o nome dos autor(a): ")
            if autor.lower() == 'sair':
                inserindo_atores = False
            else:
                autores.append(autor)
        livros[nome_livro].append(autores)

        paginas = int(input("Digite o número de páginas do livro: "))
        livros[nome_livro].append(paginas)
        return True

def deletar_livro(livros, nome_livro):
    nome_livro = input("Digite o nome do livro que desaja excluir: ")
    if nome_livro in livros:
        del livros[nome_livro]
        return True
    else:
        print("Livro não encontrado!")
        return False

def menu_editar_livro(livros):
    nome_livro = input("Digite o nome do livro que deseja editar: ")
    if nome_livro in livros:
        print('1 - Alterar ISBN do Livro')
        print('2 - Alterar Gênero do Livro')
        print('3 - Alterar Autores do Livro')
        print('4 - Alterar Número de paginas do Livro')
        print('5 - Alterar Todos os Dados do Livro')
        print('6 - Voltar')

        op = input("Escolha uma opção: ")
        return op
    else:
        print("Erro: por favor escolha uma das opções entre 1 e 6!")

def editar_isbn(livros, nome_livro):
    isbn = input("Digite o no ISBN para editar do livro: ")
    livros[nome_livro][0] = isbn
    return True

def editar_genero(livros, nome_livro):
    genero = input("Digite o novo gênero do livro: ")
    livros[nome_livro][1] = genero
    return True

def editar_paginas(livvros, nome_livro):
    pags = int(input("Digite o novo número de paginas que deseja editar: "))
    livros[nome_livro][2] = pags

def editar_autores(livros, nome_livro):
    autor = input("Digite o nome autor(a) que deseja alterar: ")
    novo_autor = input("Digite o novo nome do autor(a): ")

    pos = 1
    for i in range(len(livros[nome_livro][3])):
        if livros[nome_livro][2][i] == autor:
            pos = i
    
    if pos >= 0:
        livros[nome_livro][2] = novo_autor
        return True
    else:
        return False

def exibir_livros(livros):
    if len(livros) > 0:
        print(f"{'=' * 10} Livros {'=' * 10}")
        for dados in livros.keys():
            print(f'Livro: {dados}')
            print(f"ISBN: {livros[dados][0]}")
            print(f"Gênero: {livros[dados][1]}")
            print(f"Pagina: {livros[dados][2]}")
            for autor in range(len(livros[dados][3])):
                print(livros[dados][3][autor])
            print(f"{'=' * 20}\n")
    else:
        print("Nenhum livro cadastrado!")

def main_menu_editar_livro(livros, nome_livro):
    op = menu_editar_livro(livros)

    if op == '1':
        print("Editando o ISBN do livro...")
        editar_isbn(livros,nome_livro)
    elif op == '2':
        print("Editando o gênero do livro...")
        editar_genero(livros, nome_livro)
    elif op == '3':
        print("Editando os autores do livro...")
        editar_autores(livros, nome_livro)
    elif op == '4':
        print("Editando o número de paginas do livro...")
        editar_paginas(livros, nome_livro)
    elif op == '5':
        print("Editando todos dados do livro...")
        editar_isbn(livros, nome_livro)
        editar_genero(livros, nome_livro)
        editar_paginas(livros, nome_livro)
        editar_autores(livros, nome_livro)
    elif op == '7':
        submenuLivros()
    else:
        print("Escolha uma opção válida!")

#######Empréstimos#######
emprestimos_por_cpf = {
    "111.222.333-44": [
        {
            "ISBN": "978-85-359-0277-5", # Dom Casmurro
            "Data Retirada": "2025-05-10",
            "Data de Devolção": "2025-05-24", # Devolvido no prazo
            "Multa por emprestimo diario": 0.50
        },
        {
            "ISBN": "978-85-9807-827-2", # 1984
            "Data Retirada": "2025-05-15",
            "Data de Devolção": None, # Livro emprestado e já em atraso
            "Multa por emprestimo diario": 1.00
        }
    ],
    "222.333.444-55": [
        {
            "ISBN": "978-85-7164-588-9", # O Alquimista
            "Data Retirada": "2025-04-20",
            "Data de Devolção": "2025-05-15", # Devolvido com atraso
            "Multa por emprestimo diario": 0.75
        }
    ],
    "333.444.555-66": [
        {
            "ISBN": "978-85-7980-323-8", # A Culpa é das Estrelas
            "Data Retirada": "2025-06-01",
            "Data de Devolção": None, # Livro ainda emprestado, dentro do prazo
            "Multa por emprestimo diario": 0.50
        }
    ],
    "444.555.666-77": [
        {
            "ISBN": "978-0-7475-3274-3", # Harry Potter and the Philosopher's Stone
            "Data Reterida": "2025-03-01",
            "Data Devolucao": "2025-03-15", # Devolvido no prazo
            "Multa por Emprestimo Diario": 0.50
        }
    ]
}

def exibir_emprestimos(emprestimos):
    print(f"{'=' * 10} Emprestimos {'=' * 10}")
    if len(emprestimos) > 0:
        for cpf in emprestimos.keys():
            print(f'Usuário: {cpf}')
            print("Livros:")
            i = 0
            livros = emprestimos[cpf]
            while i < len(livros):
                for livro in livros[i]:
                    print(f"{livro}: {livros[i][livro]}")
                print(f"Livro emprestado {i}")
                i += 1
            print(f'{"=" * 20}\n')
    else:
        print("Nenhum livro cadastrado!")

def inserir_emprestimo(emprestimos, usuarios, livros):
    cpf_usuario = input("Informe o CPF do usúario: ")
    if cpf_usuario not in usuarios:
        print("Usuario não existente!")
        return False
    else:
        emprestimos[cpf_usuario] = []

        isbn_livro = input("Informe o ISBN do livro (999-99-999-9999-9): ")
        if isbn_livro not in livros:
            print("Livro não existente!")
            return False
        else:
            emprestimos[cpf_usuario].append(isbn_livro)
        
        data_reterida = input("Digite a data de retirada (2000-02-02): ")
        emprestimos[cpf_usuario].append(data_reterida)

        data_devolucao = None
        emprestimos[cpf_usuario].append(data_devolucao)


        valor_multa_diaria = .50
        emprestimos[cpf_usuario].append(valor_multa_diaria)
        
        return True

def devolvido(emprestimos):
    cpf_usuario = input("Digite o CPF do usuario: ")
    if cpf_usuario in emprestimos:
        if emprestimos[cpf_usuario][2] == None:
            return True

def deletar_emprestimo(emprestimos):
    cpf_usuario = input("Digite o CPF do usúario: ")
    if cpf_usuario in emprestimos:
        del emprestimos[cpf_usuario]
        return True
    else:
        print("Emprestimo não encontrado!")
        return False
    
def menu_editar_emprestimo(emprestimos, ):
    cpf_usuario = input("Informe o CPF do usúario que desaja editar o empréstimos: ")
    if cpf_usuario in emprestimos:
        print("1 - Alterar ISBN do livro emprestado")
        print("2 - Alterar data de retira do livro emprestado")
        print("3 - Alterar data de devolução do livro eprestado")
        print("4 - Alterar valor da multa diaria do livro emprestado")
        print("5 - Sair")

        op = input("Escolha uma opção: ")
        return op
    else:
        print("Erro: por favor escolha uma das opções entre 1 e 6!")

def editar_isbn_emprestimo(emprestimos, cpf_usuario):
    isbn = input("Insira o novo ISBN do livro que deseja do empréstimo: ")
    emprestimos[cpf_usuario][0] = isbn
    return True

def editar_data_retirada(emprestimos, cpf_usuario):
    data_retirada = input("Digite data que deseja atualizar: ")
    emprestimos[cpf_usuario][1] = data_retirada
    return True

def editar_data_retida(emprestimos, cpf_usuario):
    if devolvido(emprestimos):
        data_devolução = input("Digite o a data de dvolução do livro (2000-02-02): ")
        emprestimos[cpf_usuario][2] = data_devolução
        return True
    
def editar_valor_multa(emprestimos, cpf_usuario):
    valor_multa = int(input("Digite valor que deseja editar: "))
    emprestimos[cpf_usuario][3] = valor_multa
    return True

def main_editar_livro(emprestimos, cpf_usuario):
    op = menu_editar_emprestimo(emprestimos)

    if op =='1':
        print("Editando o ISBN do livro...")
        editar_isbn_emprestimo(emprestimos, cpf_usuario)
    elif op == '2':
        print("Editado a data de retirada do livro emprestado...")
        editar_data_retida(emprestimos, cpf_usuario)
    elif op == '3':
        print("Editando a data de devolução do livro emprestado...")
    elif op == '4':
        print("Editando valor da multa diaria por empréstimo...")
    elif op == '5':
        submenuEmprestimos()
    else:
        print("Escolha uma opção valida!")


####### Manipulação de Arquivo/Relatorio ######
def calcular_idade(usuarios, cpf_usuario):
    data_nasc = usuarios[cpf_usuario][6]
    data_atual = datetime.datetime.now().year
    ano_nasc = data_nasc.split('/')
    return int(data_atual) - int(ano_nasc[2])

def limpar_terminal():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def filtro_idade(usuarios, cpf_usuario):
    limpar_terminal()
    idade_minima = int(input("Digite a idade minima para filtrar: "))
    usuarios_filtrados = []
    resultado = f"\nUsúarios com mais de {idade_minima} anos:\n"

    for usuario in usuarios:
        idade = calcular_idade(usuarios, cpf_usuario)

        if idade > idade_minima:
            usuarios_filtrados.append(usuario)

    if usuarios_filtrados:
        for usuario in usuarios_filtrados:
            resultado += "\n-------------------\n"
            for chave, valor in usuario.items():
                resultado += f"{chave}: {valor}\n"
    else:
        resultado += "\nNenhum usuário encontrado com o critério especificado."

    return resultado

def ler_arquivo():
    with open("relatorio_filtro_idade_usuario.txt", "r", encoding='utf-8') as arquivo:
        dados_arquivo = arquivo.read()

def gravar_filtro_idade_usuario(usuarios, cpf_usuario):
    limpar_terminal()
    nome_arquivo = "relatorio_filtro_idade_usuario.txt"

    if os.path.exists(nome_arquivo):
        verificando = True
        while verificando:
            resposta = input(f"O arquivo {nome_arquivo} já existe. Deseja sobrescrevê-lo? (s/n): ").lower()
            if resposta in ['s', 'n']:
                if resposta == 'n':
                    print("Operação cancelada.")
                    datetime.time.sleep(2)
                    limpar_terminal()
                    return
                verificando = False
            print("Por favor, responda com 's' para sim ou 'n' para não.")
            time.sleep(1)
            limpar_terminal()

    with open(nome_arquivo, "w", encoding='utf-8') as arquivo_usuario:
        dados_filtro_usuario = filtro_idade(usuarios, cpf_usuario)
        arquivo_usuario.write(dados_filtro_usuario)
        print(f"Dados gravados com sucesso em {nome_arquivo}")
        time.sleep(2)
        limpar_terminal()

exibir_livros(livros)