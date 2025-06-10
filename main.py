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
def cadastrarUsuario(usuarios, cpf):
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
#######Livros#######

def sub_menu_livro():
    print("#=====Menu de Livros=====")
    print("1. Exibir Todos os Livros")
    print("2. Adicionar Livro")
    print("3. Editar Livro")
    print("4. Buscar Livro")
    print("5. Excluir Livro")
    print("6. Voltar")


livros = {
    '978-85-359-0277-2': {
        "TITULO": "Dom Casmurro",
        "GENERO": "Romance",
        "NUMERO_PAGS": 256,
        "AUTORES": ["Machado de Assis"] # Uma lista de autores
    },
    '978-0-7653-2635-5': {
        "TITULO": "O Nome do Vento",
        "GENERO": "Fantasia",
        "NUMERO_PAGS": 662,
        "AUTORES": ["Patrick Rothfuss"]
    },
    '978-0-13-468599-1': {
        "TITULO": "Effective Modern C++",
        "GENERO": "Técnico",
        "NUMERO_PAGS": 336,
        "AUTORES": ["Scott Meyers"]
    }
}


def adicionar_livro(list_livro):
    try:
        autores = []

        livro = {
            input("Digite o titulo do livro: "): {
                'ISBN': input("Digite o ISBN do livro (999-9-99-999999-9): "),
                'GENERO': input("Digite o gênero do livro: "),
                'AUTORES': autores,
                'NUMERO_PAGS': int(input("Digite no número de paginas: "))
            }
        }
        autor = input("Digite o nome do autor: ")
        autores.append(autor)

        list_livro = livro

        return print(livro, list_livro)
    except ValueError as e:
        print(f"Erro: {e}")

def exibir_livros(livros):
    try:
        if not livros:
            print("Não há livros pra exibir!")
            return False
        print("===== Catalogo de FIlmes =====\n")
        for isbn, dados in livros.items():
            print("-" * 20)
            print(
                f"ISBN: {isbn}",
                f"\nTITULO: {dados.get("TITULO")}",
                f"\nGÊNERO: {dados.get("GENERO")}",
                f"\nPAGINAS: {dados.get("NUMERO_PAGS")}",
            )

            autores = dados.get("AUTORES", [])
            if autores:
                print(f"AUTOR(ES): {", ".join(autores)}")

            print("-" * 20)
        return True
    except ValueError as e:
        print(f"Erro: {e}")
    except:
        print("Não foi possível adicionar o livro!")

def editar_livro_iniciante(livros):
    print("====== Editando Livro (Versão Iniciante) ======")
    nome_livro_procurado = input("Digite o título do livro que deseja editar: ")

    lista_de_titulos = list(livros.keys())

    indice = 0
    livro_foi_encontrado = False
    chave_encontrada = ""

    while indice < len(lista_de_titulos) and not livro_foi_encontrado:
        titulo_atual = lista_de_titulos[indice]

        if titulo_atual.lower() == nome_livro_procurado.lower():
            livro_foi_encontrado = True
            chave_encontrada = titulo_atual

        indice = indice + 1

    if livro_foi_encontrado:
        try:
            print("\n--- Livro encontrado! Digite as novas informações ---")
            print(f"(Deixe em branco para manter a informação atual)")

            dados_atuais = livros[chave_encontrada]

            novo_titulo = input(f"Novo título (Atual: {chave_encontrada}): ")
            if novo_titulo == "":
                novo_titulo = chave_encontrada

            novo_isbn = input(f"Novo ISBN (Atual: {dados_atuais.get('ISBN', 'N/A')}): ")
            if novo_isbn == "":
                novo_isbn = dados_atuais.get('ISBN')

            novo_genero = input(f"Novo gênero (Atual: {dados_atuais.get('GENERO', 'N/A')}): ")
            if novo_genero == "":
                novo_genero = dados_atuais.get('GENERO')

            pagina_valida = False
            novo_num_pags = dados_atuais.get('NUMERO_PAGS')  # Valor padrão
            while not pagina_valida:
                num_pags_str = input(
                    f"Novo número de páginas (Atual: {dados_atuais.get('NUMERO_PAGS', 'N/A')}): ")
                if num_pags_str == "":
                    pagina_valida = True
                else:
                    try:
                        novo_num_pags = int(num_pags_str)
                        pagina_valida = True
                    except ValueError:
                        print("Erro: Por favor, digite um número válido.")

            novos_autores = []
            print(f"Autores atuais: {', '.join(dados_atuais.get('AUTORES', ['N/A']))}")

            continuar_adicionando = True
            while continuar_adicionando:
                autor = input("Digite um novo autor (ou deixe em branco para terminar): ")
                if autor != "":
                    novos_autores.append(autor)
                else:
                    continuar_adicionando = False

            if len(novos_autores) == 0:
                novos_autores = dados_atuais.get('AUTORES', [])

            livro_atualizado = {
                'ISBN': novo_isbn,
                'GENERO': novo_genero,
                'AUTORES': novos_autores,
                'NUMERO_PAGS': novo_num_pags
            }

            if novo_titulo != chave_encontrada:
                del livros[chave_encontrada]

            livros[novo_titulo] = livro_atualizado

            print("\nLivro editado com sucesso!")
            return True

        except Exception as e:
            print(f"\nOcorreu um erro inesperado ao editar: {e}")
            return False
    else:
        print("\nLivro não encontrado no nosso acervo!")
        return False

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
