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
            print('Consultando usuário...')
            #Função
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


 
    