'''
Cada Submenu deverá oferecer as opções: Listar todos, Listar um elemento específico
do conjunto, Incluir (sem repetição), Alterar e Excluir (após confirmação dos dados) um
elemento do conjunto. Observe que os atributos que estão no plural indicam que deverá ser
possível incluir vários itens daquele mesmo atributo

'''
import os
import time
import datetime

usuarios = [
    {"nome": "Camila Alves", "endereco": "Rua das Acácias", "numero": "101", "cep": "01002-010", "data_nasc": "10/05/1990", "profissao": "Arquiteta", "cpf": "111.222.333-01", "email": "camila.alves@emailficticio.com.br"},
    {"nome": "Bruno Costa", "endereco": "Avenida Ipiranga", "numero": "202", "cep": "02003-020", "data_nasc": "25/08/1982", "profissao": "Contador", "cpf": "222.333.444-02", "email": "bruno.costa82@meuemail.com"},
    {"nome": "Larissa Dias", "endereco": "Travessa dos Lírios", "numero": "30", "cep": "03004-030", "data_nasc": "12/01/1995", "profissao": "Psicóloga", "cpf": "333.444.555-03", "email": "lari.dias.psi@emailseguro.net"},
    {"nome": "Rodrigo Ferreira", "endereco": "Alameda das Gardênias", "numero": "404", "cep": "04005-040", "data_nasc": "03/11/1979", "profissao": "Jornalista", "cpf": "444.555.666-04", "email": "rodrigo.ferreira.jorn@provedorexemplo.com"},
    {"nome": "Sofia Gomes", "endereco": "Rua dos Girassóis", "numero": "505", "cep": "05006-050", "data_nasc": "18/07/2001", "profissao": "Estudante", "cpf": "555.666.777-05", "email": "sofia.g2001@emailuniversitario.edu.br"},
    {"nome": "Thiago Lima", "endereco": "Avenida Rebouças", "numero": "606", "cep": "06007-060", "data_nasc": "29/04/1988", "profissao": "Desenvolvedor Web", "cpf": "666.777.888-06", "email": "thiago.dev@webmailficticio.com"},
    {"nome": "Gabriela Martins", "endereco": "Praça Roosevelt", "numero": "70", "cep": "07008-070", "data_nasc": "07/09/1993", "profissao": "Publicitária", "cpf": "777.888.999-07", "email": "gabi.martins.publi@emailcriativo.com.br"},
    {"nome": "Alice Xavier", "endereco": "Rua Gabriel Monteiro da Silva", "numero": "717", "cep": "07026-250", "data_nasc": "22/12/1984", "profissao": "Dentista", "cpf": "543.210.987-25", "email": "alice.xavier.odonto@sorrisomail.com.br"}
]

livros = [
    {"ISBN": "978-3-16-148410-0", "Título": "O Último Dragão de Fogo", "Gênero": "Fantasia Épica", "Autores": ["Elara Vance"], "Número de Páginas": 450},
    {"ISBN": "978-1-23-456789-7", "Título": "Sombras de Neon", "Gênero": "Cyberpunk Noir", "Autores": ["Kenji Tanaka", "Sarah Miller"], "Número de Páginas": 320},
    {"ISBN": "979-8-76-543210-9", "Título": "O Jardim Secreto dos Sussurros", "Gênero": "Realismo Mágico", "Autores": ["Isabella Rossi"], "Número de Páginas": 288},
    {"ISBN": "978-0-55-216650-3", "Título": "Crônicas do Tempo Perdido", "Gênero": "Ficção Científica", "Autores": ["Dr. Aris Thorne"], "Número de Páginas": 512},
    {"ISBN": "978-8-53-330227-5", "Título": "A Receita da Felicidade Eterna", "Gênero": "Autoajuda", "Autores": ["Sofia Almeida"], "Número de Páginas": 190},
    {"ISBN": "978-9-87-654321-0", "Título": "Mistério na Rua das Magnólias", "Gênero": "Suspense Policial", "Autores": ["Ricardo Barros"], "Número de Páginas": 350},
    {"ISBN": "978-2-07-036002-4", "Título": "O Coração da Selva Esquecida", "Gênero": "Aventura", "Autores": ["Leo Fernandez"], "Número de Páginas": 270},
    {"ISBN": "978-3-44-226778-7", "Título": "Entre Estrelas e Poeira Cósmica", "Gênero": "Space Opera", "Autores": ["Capitã Eva Rostova"], "Número de Páginas": 600},
]

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

def sub_menu_livro():
    print("#=====Menu de Livros=====")
    print("1. Adicionar livro")
    print()
    print()
    print()
    print()
    print()
    print()

####### Manioulação de Arquivo/Relatorio ######
def calcular_idade(usuario):
    data_nasc = usuario["data_nasc"]
    data_atual = datetime.datetime.now().year
    ano_nasc = data_nasc.split('/')
    return int(data_atual) - int(ano_nasc[2])


def limpar_terminal():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Mac e Linux
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


def gravar_filtro_idade_usuario():
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


gravar_filtro_idade_usuario()
ler_arquivo()