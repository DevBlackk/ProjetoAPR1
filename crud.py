'''
Cada Submenu deverá oferecer as opções: Listar todos, Listar um elemento específico
do conjunto, Incluir (sem repetição), Alterar e Excluir (após confirmação dos dados) um
elemento do conjunto. Observe que os atributos que estão no plural indicam que deverá ser
possível incluir vários itens daquele mesmo atributo

'''
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