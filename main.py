########## MENU E SUBMENUS ###########
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
def submenuRelatorios():
    print(f'\n Submenu de Relátorios:')
    print('1 - Listar todos os dados de todos os usuários com mais de X anos de idade')
    print('2 - Listar todos os dados de todos os livros que tenham mais do que X autores')
    print('3 - Listar empréstimos realizados entre dd/mm/aaaa e dd/mm/aaaa')
    print('0 - Voltar ao Menu Principal')
    opcao = input('Escolha uma opção:')
    return opcao

######## USUARIOS #########

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
        print('9 - Alterar TODOS os dados do Usuário(Exceto CPF)')
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
        opc = '1'
        while opc != '0':
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
                if editEmail(usuarios, cpf):
                    print('E-mail alterado com sucesso.')
                else:
                    print('Não foi possível alterar o Email')
            elif opc == '6':
                if editTelefone(usuarios, cpf):
                    print('Telefone alterado com sucesso.')
                else:
                    print('Não foi possível alterar o Telefone')
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
                print('Retornando ao Submenu de Usuários...')
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
                print(' ', end='')
                print(usuarios[i][4][j])
            print(f'Telefones:')
            for j in range(len(usuarios[i][5])):
                print(' ', end='')
                print(usuarios[i][5][j])
            print(f'Data de Nascimento: {usuarios[i][6]}')
            print(f'Profissão: {usuarios[i][7]}')
            print('#' * 45)
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
                print(' ', end='')
                print(usuarios[cpf][4][j])
        print('Telefone(s):')
        for j in range(len(usuarios[cpf][5])):
            print(' ', end='')
            print(usuarios[cpf][5][j])
        print(f'Data de Nascimento: {usuarios[cpf][6]}')
        print(f'Profissão: {usuarios[cpf][7]}')
    else:
        print('CPF não cadastrado')

####### Livros #######

def inserirLivro(livros):  
    isbn = input("Digite o ISBN do livro que deseja adicionar(999-99-999-9999-9): ")
    if isbn in livros:
        print("Livro já existente!")
        return False
    else:
        livros[isbn] = []

        nome_livro = input("Digite o título do livro: ")
        livros[isbn].append(nome_livro)

        genero = input("Digite o gênero do livro: ")
        livros[isbn].append(genero)

        autores = []
        qtd = int(input('Informe a quantidade de autores que deseja adicionar:'))
        for i in range(qtd):
            autor = input('Informe o nome do autor:')
            autores.append(autor)
        livros[isbn].append(autores)

        paginas = int(input("Digite o número de páginas do livro: "))
        livros[isbn].append(paginas)
        return True
def deletarLivro(livros): 
    isbn = input("Digite o ISBN do livro que deseja excluir: ")
    if isbn in livros:
        del livros[isbn]
        return True
    else:
        print("Livro não encontrado!")
        return False
def listarLivros(livros): 
    if len(livros) > 0:
        for i in livros.keys():
            print(f'ISBN: {i}')
            print(f'Título: {livros[i][0]}')
            print(f'Gênero: {livros[i][1]}')
            print('Autores:')
            for j in range(len(livros[i][2])):
                print(' ', end='')
                print(livros[i][2][j])
            print(f'Número de Páginas: {livros[i][3]}')
            print('#' * 45)
    else:
        print('Lista de Livros Vazia')
def listarLivro(livros, isbn): 
    if isbn in livros:
        print(f'ISBN: {isbn}')
        print(f'Título: {livros[isbn][0]}')
        print(f'Gênero: {livros[isbn][1]} ')
        print(f'Autores:')
        for i in range(len(livros[isbn][2])):
            print(' ', end='')
            print(f'{livros[isbn][2][i]}')
        print(f'Número de Páginas: {livros[isbn][3]}')
    else:
        print('Livro não encontrado.')
def editarTítulo(livros,isbn):
    titulo = input('Digite o novo título do livro:')
    livros[isbn][0] = titulo
def editar_genero(livros, isbn):
    genero = input("Digite o novo gênero do livro: ")
    livros[isbn][1] = genero
    return True
def editar_autores(livros, isbn):
    autor = input("Digite o nome autor(a) que deseja alterar: ")
    novo_autor = input("Digite o novo nome do autor(a): ")

    pos = -1
    for i in range(len(livros[isbn][2])):
        if livros[isbn][2][i] == autor:
            pos = i
    
    if pos >= 0:
        livros[isbn][2][i] = novo_autor
        return True
    else:
        return False
def editar_paginas(livros, isbn):
    pags = int(input("Digite o novo número de paginas que deseja editar: "))
    livros[isbn][3] = pags
def menuEditLivro():
        print('1 - Alterar o título do livro.')
        print('2 - Alterar o gênero do livro.')
        print('3 - Alterar os autores do livro.')
        print('4 - Alterar o número de páginas do livro.')
        print('5 - Alterar todos os dados do livro (EXCETO ISBN).')
        print('0 - Voltar ao Submenu de Livros')
        opc = input('Escolha uma opção: ')
        return opc
def main_menu_editar_livro(livros):
    isbn = input('Informe o ISBN do livro que deseja alterar os dados:')
    if isbn in livros:    
        op = '1'
        while op != '0':
            op = menuEditLivro()
            if op == '1':
                print("Editando o título do livro...")
                editarTítulo(livros, isbn)
            elif op == '2':
                print("Editando o gênero do livro...")
                editar_genero(livros, isbn)
            elif op == '3':
                print("Editando os autores do livro...")
                editar_autores(livros, isbn)
            elif op == '4':
                print("Editando o número de paginas do livro...")
                editar_paginas(livros, isbn)
            elif op == '5':
                print("Editando todos dados do livro...")
                editar_genero(livros, isbn)
                editar_paginas(livros, isbn)
                editar_autores(livros, isbn)
            elif op == '0':
                print('Retornando ao Submenu de Livros...')
            else:
                print("Escolha uma opção válida!")
    else:
        print('Livro não encontrado.')
        print('Retornando ao Submenu de Livros...')

####### Empréstimos #######

def chaveEmprestimo():
    cpf = input('Digite o CPF do cliente:')
    isbn = input('Digite o ISBN do livro:')
    data_ret = input('Digite a data de retirada do livro:')
    chave = (cpf, isbn, data_ret)
    return chave
def inserirEmprestimo(emprestimos):
    chave = chaveEmprestimo()
    if chave in emprestimos:
        print('Empréstimo já cadastrado')
    else:
        data_dev = input('Digite a data de devolução do livro')
        multa = input('Digite a multa por atraso')
        emprestimos[chave] = [data_dev, multa]
        print('Empréstimo Cadastrado com Sucesso.')
def deletarEmprestimo(emprestimos):
    chave = chaveEmprestimo()
    if chave in emprestimos:
        del emprestimos[chave]
        print('Empréstimo Deletado com Sucesso.')
    else:
        print('Empréstimo não encontrado')
def listarEmprestimos(emprestimos):
    if len(emprestimos) > 0:
        for chave in emprestimos.keys():
            print(f'CPF: {chave[0]}')
            print(f'ISBN: {chave[1]}')
            print(f'Data de Retirada: {chave[2]}')
            print(f'Data de Devolução: {emprestimos[chave][0]}')
            print(f'Valor Diário da Multa por Atraso: {emprestimos[chave][1]}')
            print('#' * 45)
    else:
        print('Não há empréstimos')
def listarEmprestimo(emprestimos):
    chave = chaveEmprestimo()
    if chave in emprestimos:
            print(f'CPF: {chave[0]}')
            print(f'ISBN: {chave[1]}')
            print(f'Data de Retirada: {chave[2]}')
            print(f'Data de Devolução: {emprestimos[chave][0]}')
            print(f'Valor Diário da Multa por Atraso: {emprestimos[chave][1]}')
    else:
        print('Empréstimo não encontrado')
def editDataDev(emprestimos, chave):
    novaData = input('Informe a nova data de devolução:')
    emprestimos[chave][0] = novaData
def editMulta(emprestimos, chave):
    novaMulta = input('Digite a nova multa:')
    emprestimos[chave][1] = novaMulta
def menuEditEmprestimo():
    print('1 - Alterar Data de Devolução do Empréstimo')
    print('2 - Alterar Valor Diário da Multa por Atraso do Empréstimo')
    print('0 - Retornar ao Submenu de Empréstimos')
    opc = input('Escolha uma opção:')
    return opc
def mainEditEmprestimo(emprestimos):
    chave = chaveEmprestimo()
    opc = '1'
    if chave in emprestimos:
        while opc != '0':
            opc = menuEditEmprestimo()
            if opc == '1':
                print('Alterando Data de Devolução...')
                print()
                editDataDev(emprestimos, chave)
                print()
                print('Data de devolução alterada com sucesso.')
            elif opc == '2':
                print('Alterando Valor diário da multa por atraso...')
                print()
                editMulta(emprestimos, chave)
                print()
                print('Valor diário da multa por atraso alterado com sucesso.')
            elif opc == '0':
                print('Retornando ao Submenu de Empréstimos...')
    else:
        print('Empréstimo não encontrado.')

####### MAIN SUBMENUS #######

def mainSubmenuUsuarios(usuarios):
    opc = '1'
    while opc != '0':
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
            print('Retornando ao menu principal...')
        else:
            print()
            print('Escolha uma opção válida!')
def mainSubmenuLivros(livros):
    opc = '1'
    while opc != '0':
        opc = submenuLivros()
        if opc == '1':
            print('Listando livros...')
            print()
            listarLivros(livros)
        elif opc == '2':
            isbn = input('Informe o ISBN do livro que deseja consultar:')
            print('Consultando Livro...')
            listarLivro(livros, isbn)
        elif opc == '3':
            print('Inserindo Livro...')
            print()
            inserirLivro(livros)
        elif opc == '4':
            main_menu_editar_livro(livros)
        elif opc == '5':
            isbn = input('Informe o ISBN do livro que deseja excluir:')
            print('Deletando Livro...')
            print()
            deletarLivro(livros, isbn)
        elif opc =='0':
            print('Retornando ao menu principal...')
        else:
            print()
            print('Escolha uma opção válida!')
def mainSubmenuEmprestimos(emprestimos):
    opc = '1'
    while opc != '0':
        opc = submenuEmprestimos()
        if opc == '1':
            print('Exibindo Todos os Empréstimos...')
            print()
            listarEmprestimos(emprestimos)
        elif opc == '2':
            print('Consultando Empréstimo...')
            print()
            listarEmprestimo(emprestimos)
        elif opc =='3':
            print('Cadastrando Novo Empréstimo...')
            print()
            inserirEmprestimo(emprestimos)
        elif opc == '4':
            print('Alterando Empréstimo...')
            print()
            mainEditEmprestimo(emprestimos)
        elif opc == '5':
            print('Excluindo Empréstimo...')
            print()
            deletarEmprestimo(emprestimos)
        elif opc == '0':
            print('Retornando ao menu principal...')
def mainSubmenuRelatorios(usuarios, livros, emprestimos):
    relat_usuarios = 'relatorio_idade.txt'
    relat_autores = 'relatorio_autores.txt'
    relat_emprestimos = 'relatorio_emprestimos.txt'
    opc = '1'
    while opc != '0':
        opc = submenuRelatorios()
        if opc == '1':
            relatorioIdade(usuarios,relat_usuarios)
        elif opc == '2':
            relatorioAutores(livros,relat_autores)
        elif opc == '3':
            relatorioEmprestimo(emprestimos, usuarios, livros, relat_emprestimos)
        elif opc == '0':
            print('Retornando ao menu principal...')

####### ARQUIVOS ########

def escreverArquivoUsuario(usuarios, arquivo_usuario):
    arq = open(arquivo_usuario, 'w')
    for cpf in usuarios:
        linha = ''
        linha+= cpf + ';' + usuarios[cpf][0] + ';' + usuarios[cpf][1] + ';' + usuarios[cpf][2] + ';' + usuarios[cpf][3] + ';'
        for email in usuarios[cpf][4]:
            linha += email + '_'
        linha += ';'
        for telefone in usuarios[cpf][5]:
            linha += telefone + '_'
        linha+= ';' + usuarios[cpf][6] + ';' + usuarios[cpf][7] + '\n'
        arq.write(linha)
    arq.close()
def lerArquivoUsuario(arquivo_usuario):
    usuarios = dict()
    if existe_arquivo(arquivo_usuario):
        arq = open(arquivo_usuario, 'r')
        for linha in arq:
            linha = linha.replace('\n', '')
            linha = linha.split(';')
            cpf = linha[0]
            usuarios[cpf] = []
            usuarios[cpf].append(linha[1])
            usuarios[cpf].append(linha[2])
            usuarios[cpf].append(linha[3])
            usuarios[cpf].append(linha[4])
            emails = linha[5].split('_')
            del emails[-1]
            usuarios[cpf].append(emails)
            telefones = linha[6].split('_')
            del telefones[-1]
            usuarios[cpf].append(telefones)
            usuarios[cpf].append(linha[7])
            usuarios[cpf].append(linha[8])
        arq.close()
    return usuarios
def escreverArquivoLivros(livros, arquivo_livros):
    arq = open(arquivo_livros, 'w')
    for isbn in livros:
        linha = ''
        linha += isbn + ';' + livros[isbn][0] + ';' + livros[isbn][1] + ';'
        for autor in livros[isbn][2]:
            linha+= autor + '_'
        linha += ';' + str(livros[isbn][3]) + '\n'
        arq.write(linha)
    arq.close()
def lerArquivoLivros(arquivo_livros):
    livros = dict()
    if existe_arquivo(arquivo_livros):
        arq = open(arquivo_livros, 'r')
        for linha in arq:
            linha = linha.replace('\n', '')
            linha = linha.split(';')
            isbn = linha[0]
            livros[isbn] = []
            livros[isbn].append(linha[1])
            livros[isbn].append(linha[2])
            autores = linha[3].split('_')
            del autores[-1]
            livros[isbn].append(autores)
            livros[isbn].append(linha[4])
        arq.close()
    return livros
def escreverArquivoEmprestimos(emprestimos, arquivo_emprestimos):
    arq = open(arquivo_emprestimos, 'w')
    for chave in emprestimos:
        linha = ''
        chave_str = chave[0] + ';' + chave[1] + ';' + chave[2] 
        linha += chave_str + ';' + emprestimos[chave][0] + ';' + emprestimos[chave][1] + '\n'
        arq.write(linha)
    arq.close()
def lerArquivoEmprestimos(arquivo_emprestimos):
    emprestimos = dict()
    if existe_arquivo(arquivo_emprestimos):
        arq = open(arquivo_emprestimos, 'r')
        for linha in arq:
            linha = linha.replace('\n', '')
            linha = linha.split(';')
            chave = (linha[0], linha[1], linha[2])
            emprestimos[chave] = []
            emprestimos[chave].append(linha[3])
            emprestimos[chave].append(linha[4])
        arq.close()
    return emprestimos    
def escreverRelatorioEmprestimos(arquivo, relatorio):
    arq = open(arquivo, 'w')
    for i in range(len(relatorio)):
        linha = ''
        for j in range(len(relatorio[i])):
            linha += relatorio[i][j] +';'
        linha = linha[:-1]
        linha += '\n'
        arq.write(linha)
    arq.close()
def escreverRelatorioLivros(isbn_desejado, livros, arquivo_livros):
    arq = open(arquivo_livros, 'w')
    for isbn in isbn_desejado:
        linha = ''
        linha += isbn + ';' + livros[isbn][0] + ';' + livros[isbn][1] + ';'
        for autor in livros[isbn][2]:
            linha+= autor + '_'
        linha += ';' + str(livros[isbn][3]) + '\n'
        arq.write(linha)
    arq.close()
def escreverRelatorioUsuario(cpf_desejado,usuarios, arquivo_usuario):
    arq = open(arquivo_usuario, 'w')
    for cpf in cpf_desejado:
        linha = ''
        linha+= cpf + ';' + usuarios[cpf][0] + ';' + usuarios[cpf][1] + ';' + usuarios[cpf][2] + ';' + usuarios[cpf][3] + ';'
        for email in usuarios[cpf][4]:
            linha += email + '_'
        linha += ';'
        for telefone in usuarios[cpf][5]:
            linha += telefone + '_'
        linha+= ';' + usuarios[cpf][6] + ';' + usuarios[cpf][7] + '\n'
        arq.write(linha)
    arq.close()
def existe_arquivo(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False 

##### RELATORIOS ######

def calcularIdade(usuarios, data):

    idades_por_cpf = dict()
    data = data.split('/')
    for cpf in usuarios.keys():
        nasc = usuarios[cpf][6]
        nasc = nasc.split('/')
        if nasc[1] == data[1]:
            if nasc[0] == data[0]:
                idade = int(data[2]) - int(nasc[2])
            elif nasc[0] > data[0]:
                idade = int(data[2]) - int(nasc[2])
            elif nasc[0] < data[0]:
                idade = (int(data[2]) - int(nasc[2])) - 1
        elif nasc[1] > data[1]:
            idade = (int(data[2]) - int(nasc[2])) - 1
        elif nasc[1] < data[1]:
            idade = int(data[2]) - int(nasc[2])
        idades_por_cpf[cpf] = idade
    return idades_por_cpf
def guardarCpfRelatorioIdade(usuarios, x):
    data = input('Informe a data atual (dd/mm/aaaa):')
    idades = calcularIdade(usuarios, data)
    guardar_cpf = []
    for cpf in idades.keys():
        if idades[cpf] >= x:
            guardar_cpf.append(cpf)
    return guardar_cpf
def relatorioIdade(usuarios, arquivo):
    x = int(input('Digite a idade mínima desejada:'))
    cpf_idade_desejada = guardarCpfRelatorioIdade(usuarios, x)
    escreverRelatorioUsuario(cpf_idade_desejada, usuarios, arquivo)
    if len(cpf_idade_desejada) > 0:
        for i in cpf_idade_desejada:
            listUser(usuarios, i)
            print('#' * 20)
    else:
        print()
        print('Não há usuários maiores ou iguais a idade mínima desejada.')
def guardarIsbnQuantAutores(livros, x):
    isbn_desejado = []
    for isbn in livros:
        if len(livros[isbn][2]) >= x:
            isbn_desejado.append(isbn)
    return isbn_desejado
def relatorioAutores(livros, arquivo):
    x = int(input('Informe a quantidade mínima de autores desejada:'))
    isbn_desejado = guardarIsbnQuantAutores(livros, x)
    escreverRelatorioLivros(isbn_desejado, livros, arquivo)
    if len (isbn_desejado) > 0:
        for i in isbn_desejado:
            listarLivro(livros, i)
            print('#' * 20)
    else:
        print()
        print('Não há livros com a quantidade mínima de autores desejada.')
def guardarEmprestimoData(emprestimos, x, y):
    guardar_chave=[]
    x = x.split('/')
    x[0] = int(x[0])
    x[1] = int(x[1])
    x[2] = int(x[2])
    y = y.split('/')
    y[0] = int(y[0])
    y[1] = int(y[1])
    y[2] = int(y[2])
    for chave in emprestimos.keys():
        data = emprestimos[chave][0].split('/')
        data[0] = int(data[0])
        data[1] = int(data[1])
        data[2] = int(data[2])
        if data[2] > x[2] and data[2] < y[2]:
            guardar_chave.append(chave)
        elif data[2] == x[2] and data[2] == y[2]:
            if data[1] > x[1] and data[1] < y[1]:
                guardar_chave.append(chave)
            elif data[1] == x[1] and data[1] == y[1]:
                if data[0] >= x[0] and data[0] <= y[0]:
                    guardar_chave.append(chave)
            elif data[1] == x[1] and data[1] < y[1]:
                if data[0] >= x[0]:
                    guardar_chave.append(chave)
            elif data[1] > x[1] and data[1] == y[1]:
                if data[0] <= y[0]:
                    guardar_chave.append(chave)
        elif data[2] == x[2] and data[2] < y[2]:
            if data[1] > x[1]:
                guardar_chave.append(chave)
            elif data[1] == x[1] and data[0] >= x[0]:
                guardar_chave.append(chave)
        elif data[2] > x[2] and data[2] == y[2]:
            if data[1] < y[1]:
                guardar_chave.append(chave)
            elif data[1] == y[1] and data[0] <= y[0]:
                guardar_chave.append(chave)
    return guardar_chave
def guardarRelatorioEmprestimo(emprestimos,usuarios, livros):
    data1 = input('Informe a data mínima desejada (dd/mm/aaaa):')
    data2 = input('Informe a data máxima desejada (dd/mm/aaaa):')
    chaves = guardarEmprestimoData(emprestimos, data1, data2)
    relatorio = []
    if len(chaves) > 0:
        for dados in chaves:
            dados_relatorio =[]
            dados_relatorio.append(dados[0])
            dados_relatorio.append(usuarios[dados[0]][0])
            dados_relatorio.append(dados[1])
            dados_relatorio.append(livros[dados[1]][0])
            dados_relatorio.append(emprestimos[dados][0])
            dados_relatorio.append(emprestimos[dados][1])
            relatorio.append(dados_relatorio)
    else:
        print('Não há devoluções nessas datas.')
    return relatorio
def relatorioEmprestimo(emprestimos, usuarios, livros, arquivo):
    relatorio = guardarRelatorioEmprestimo(emprestimos,usuarios,livros)
    if len(relatorio) > 0:
        escreverRelatorioEmprestimos(arquivo, relatorio)
        for i in range(len(relatorio)):
            print(f'CPF: {relatorio[i][0]}')
            print(f'Nome: {relatorio[i][1]}')
            print(f'ISBN do Livro: {relatorio[i][2]}')
            print(f'Título do Livro: {relatorio[i][3]}')
            print(f'Data de Devolução: {relatorio[i][4]}')
            print(f'Multa por atraso: {relatorio[i][5]}')
            print('#' *25)
        
def main():
    arquivo_usuario = 'usuarios.txt'
    arquivo_livros = 'livros.txt'
    arquivo_emprestimos = 'emprestimos.txt'
    arquivo_relatorio_emprestimo = 'relatorio_emprestimos.txt'
    usuarios = lerArquivoUsuario(arquivo_usuario)
    livros = lerArquivoLivros(arquivo_livros)
    emprestimos = lerArquivoEmprestimos(arquivo_emprestimos)
    opc = '1'
    while opc != '0':
        opc = menu()
        if opc == '1':
            print()
            mainSubmenuUsuarios(usuarios)
            print()
        elif opc == '2':
            print()
            mainSubmenuLivros(livros)
            print()
        elif opc == '3':
            print()
            mainSubmenuEmprestimos(emprestimos)
            print()
        elif opc == '4':
            print()
            mainSubmenuRelatorios(usuarios, livros, emprestimos)
            print()
        elif opc == '0':
            print()
            print('Encerrando o programa...')
    escreverArquivoUsuario(usuarios, arquivo_usuario)
    escreverArquivoLivros(livros,arquivo_livros)
    escreverArquivoEmprestimos(emprestimos, arquivo_emprestimos)
main()

