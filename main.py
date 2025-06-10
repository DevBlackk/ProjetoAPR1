

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
            mail = input(f'Digite o E-mail {i+1}')
            emails.append(mail)
        qtd2 = int(input('Digite quantos telefones deseja adicionar:'))
        for i in range(qtd2):
            tel = input(f'Digite o telefone {i}')
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
        return True
    else:
        print('CPF não cadastrado.')
        return False
def editUser(usuarios, cpf):
    if cpf in usuarios:
        print('1 - Alterar Nome do Usuário')
        print('2 - Alterar Rua do Usuário')
        print('3 - Alterar Número do Usuário')
        print('4 - Alterar CEP do Usuário')
        print('5 - Alterar E-mails do Usuário')
        print('6 - Alterar Telefones do Usuário') 
        print('7 - Alterar Data de Nascimento do Usuário')
        print('8 - Alterar Profissão do Usuário')
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
cpf = '07854736103'
editEmail(usuarios, cpf)
editTelefone(usuarios, cpf)
#######Livros#######

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
    import os
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
                    datetime.time.sleep(2)
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

