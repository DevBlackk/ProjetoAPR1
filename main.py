'''
Cada Submenu deverá oferecer as opções: Listar todos, Listar um elemento específico
do conjunto, Incluir (sem repetição), Alterar e Excluir (após confirmação dos dados) um
elemento do conjunto. Observe que os atributos que estão no plural indicam que deverá ser
possível incluir vários itens daquele mesmo atributo

'''
import os
import time
import datetime

def submenuUsuarios():
    usuarios = {'usuario1':{"cpf" : '23456', 'nome': 'joao'}, 'usuario2': {'cpf': '56789', 'nome': 'joana' }}
    print(f'\n Submenu Usuários:')
    print('1 - Exibir Todos')
    print('2 - Consultar Usuário')
    print('3 - Novo Cadastro')
    print('4 - Editar Usuário')
    print('5 - Excluir Cadastro')
    print('0 - Voltar ao Menu Principal')
    opcao = input('Escolha uma opção:')
    continuar = True
    while continuar: #repetir o menu até o usuário sair
        if opcao == '1':
            print('Exibindo usuários...')
            lerUsuarios(usuarios)
        elif opcao == '2':
            cpf = print(f'Digite o CPF do usuárop que deseja consultar:')
            print('Consultando usuário...')
            #função
        elif opcao == '3':
            print('Criando novo cadastro...')
            #função
        elif opcao == '4':
            cpf = input('Digite o CPF do usuário que deseja editar:')
            print('Editando Usuário...')
            #função
        elif opcao == '5':
            cpf = input('Digite o CPF do usuário que deseja excluir')
            print('Excluindo usuário...')
            #função
        else:
            #Menu principal()
            continuar = False

def lerUsuarios(usuarios):
    if len(usuarios) == 0:
        print('Não há usuarios para exibir!')
    else:
        for chave, dados in usuarios.items():
            print(f'''
            {chave}:
            CPF: {dados["cpf"]}
            Nome: {dados["nome"]}
            Rua: {dados["rua"]}, Número: {dados["nro"]}
            CEP: {dados["cep"]}
            E-mails: {(dados["emails"])}
            Telefones: {(dados["telefones"])}
            Data de Nascimento: {dados["data_nasc"]}
            Profissão: {dados["profissao"]}
            ''')

def criarUsuario(dicionario):
    quant = int(input('Digite a quantidade de usuários que deseja cadastrar:'))
    for i in range(quant):
        cpf = input(f'Digite o cpf do usuario {i}:')
        #chamar função que verifica se há cpf duplicado
        nome = input(f'Digite o nome do usuário {i}:')
        rua = input(f'Digite o nome da rua do usuário {i}:')
        nro = input(f'Digite o número da casa do usuário {i}:')
        cep = input(f'Digite o CEP do usuário {i}:')
        nasc = input(f'Digite a data de nascimento do usuário {i} (dd/mm/yy):').replace('/', '')
        profissao = input(f'Digite a profissão do usuário {i}:')
        tel = []
        emails = []
        quant_tel = int(input('Digite quantos telefones deseja adicionar:'))
        for j in range(quant_tel):
            fone = input(f'Digite o telefone {j}:')
            tel.append(fone)
        quant_email = int(input('Digite quantos e-mails deseja adicionar:'))
        for j in range(quant_email):
            email = input(f'Digite o email {j} (ex:name@email.com):')
            emails.append(email)
        dados ={
            'cpf': cpf,
            'nome': nome,
            'rua': rua,
            'numero': nro,
            'cep': cep,
            'nascimento': nasc,
            'emails': emails,
            'telefones': tel,
            'profissao': profissao
        }
        chave = f'usuario{len(dicionario) + 1}'
        dicionario[chave] = dados

#######Livros#######
livros = {
    '978-0-13-468599-1': [
        'Effective Modern C++',
        'Técnico',
        336,
        ['Scott Meyers']
    ],
    '978-0-7653-2635-5': [
        'O Nome do Vento',
        'Fantasia',
        662,
        ['Patrick Rothfuss']
    ],
    '978-85-359-0277-2': [
        'Dom Casmurro',
        'Romance',
        256,
        ['Machado de Assis']
    ]
}

def inserir_livro(livros):
    nome_livro = input("Digite o nome do filme que deseja adicionar: ")
    if nome_livro in livros:
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


def sub_menu_livro():
    print("#=====Menu de Livros=====")
    print("1. Exibir Todos os Livros")
    print("2. Adicionar Livro")
    print("3. Editar Livro")
    print("4. Buscar Livro")
    print("5. Excluir Livro")
    print("6. Voltar")

    op = input("Escolha uma opção: ")
    if op == '1':
        print("Adicionando livro...")
        if inserir_livro(livros):
            print("Livro adicionado com sucesso!")

####### Manipulação de Arquivo/Relatorio ######
def calcular_idade(usuario):
    data_nasc = usuario["data_nasc"]
    data_atual = datetime.datetime.now().year
    ano_nasc = data_nasc.split('/')
    return int(data_atual) - int(ano_nasc[2])


def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def filtro_idade(usuarios):
    limpar_terminal()
    idade_minima = int(input("Digite a idade minima para filtrar: "))
    usuarios_filtrados = []
    resultado = f"\nUsúarios com mais de {idade_minima} anos:\n"

    for usuario in usuarios:
        idade = calcular_idade(usuario)

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
        print(dados_arquivo)


def gravar_filtro_idade_usuario(usuarios):
    limpar_terminal()
    nome_arquivo = "relatorio_filtro_idade_usuario.txt"

    if os.path.exists(nome_arquivo):
        verificando = True
        while verificando:
            resposta = input(f"O arquivo {nome_arquivo} já existe. Deseja sobrescrevê-lo? (s/n): ").lower()
            if resposta in ['s', 'n']:
                if resposta == 'n':
                    print("Operação cancelada.")
                    time.sleep(2)
                    limpar_terminal()
                    return
                verificando = False
            print("Por favor, responda com 's' para sim ou 'n' para não.")
            time.sleep(1)
            limpar_terminal()

    with open(nome_arquivo, "w", encoding='utf-8') as arquivo_usuario:
        dados_filtro_usuario = filtro_idade(usuarios)
        arquivo_usuario.write(dados_filtro_usuario)
        print(f"Dados gravados com sucesso em {nome_arquivo}")
        time.sleep(2)
        limpar_terminal()
