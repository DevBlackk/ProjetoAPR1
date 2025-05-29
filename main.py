def menu_principal():
    executando = True
    while executando:
        print("\nMenu Principal:")
        print("1. Usúarios")
        print("2. Livros")
        print("3. Empréstimos")
        print("4. Relatórios")
        print("5. Sair")

        opcao = int(input("\nEscolha uma opção: "))
        if opcao == 1:
            if not menu_usuario():
                executando = False
        elif opcao == 2:
            print("Este serviço não esta disponivel!")
        elif opcao == 3:
            print("Este serviço não esta disponivel!")
        elif opcao == 4:
            print("Este serviço não esta disponivel!")
        elif opcao == 5:
            print("Encerrando o programa!")
            executando = False
        else:
            print("Opção inválida! Por favor, digite uma das opções acima.")


def menu_usuario():
    sem_menu_usuario = True
    while sem_menu_usuario:
        print("\nMenu de usúarios:")
        print("1. Ver lista de usúarios")
        print("2. Editar usúarios")
        print("3. Criar um novo usúario")
        print("4. Deletar um usúario")
        print("5. Voltar")
        print("6. Sair do Programa")

        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            print("Este serviço não diponivel!\n")
        elif opcao == 2:
            print("Este serviço não diponivel!\n")
        elif opcao == 3:
            print("Este serviço não diponivel!\n")
        elif opcao == 4:
            print("Este serviço não diponivel!\n")
        elif opcao == 5:
            return True
        elif opcao == 6:
            return False
        else:
            print("Opção invalida! Por favor, digite uma das opções acima.")


"""def criar_lista():

"""


def criar_usúario():
    usuario = {
        'CPF': '368.715.054-23',
        'NOME': 'Iago Alexandre Samuel Moraes',
        'RUA': "Rua Formosa do Araguaia",
        'NUMERO': 390,
        'CEP': "50690-715",
        'EMAIL': "iago-moraes96@c-a-m.com",
        'TELEFONE': "(81) 98733-6681",
        'DATA_DE_NASC': "07/04/1978",
        'PROFICAÇÃO': "Escritor"
    }

    return print(usuario)


def main():
    menu_principal()
    criar_usúario()


main()

'''
[
	{
		"nome": "Iago Alexandre Samuel Moraes",
		"idade": 47,
		"cpf": "368.715.054-23",
		"rg": "48.041.981-4",
		"data_nasc": "07/04/1978",
		"sexo": "Masculino",
		"signo": "Áries",
		"mae": "Alícia Bruna",
		"pai": "Davi Edson Moraes",
		"email": "iago-moraes96@c-a-m.com",
		"senha": "fw65bAtpkw",
		"cep": "50690-715",
		"endereco": "Rua Formosa do Araguaia",
		"numero": 390,
		"bairro": "Iputinga",
		"cidade": "Recife",
		"estado": "PE",
		"telefone_fixo": "(81) 2982-7453",
		"celular": "(81) 98733-6681",
		"altura": "1,66",
		"peso": 60,
		"tipo_sanguineo": "B-",
		"cor": "amarelo"
	},
	{
		"nome": "Sérgio Pedro José Moreira",
		"idade": 49,
		"cpf": "189.754.211-98",
		"rg": "40.831.329-8",
		"data_nasc": "10/01/1976",
		"sexo": "Masculino",
		"signo": "Capricórnio",
		"mae": "Stefany Alessandra",
		"pai": "Raimundo Gabriel Moreira",
		"email": "sergiopedromoreira@pubdesign.com.br",
		"senha": "u1wXE0lk3s",
		"cep": "29075-665",
		"endereco": "Rua Doutora Zilda Arns",
		"numero": 359,
		"bairro": "Aeroporto",
		"cidade": "Vitória",
		"estado": "ES",
		"telefone_fixo": "(27) 2966-8693",
		"celular": "(27) 99917-8385",
		"altura": "1,70",
		"peso": 75,
		"tipo_sanguineo": "B+",
		"cor": "laranja"
	},
	{
		"nome": "Miguel Iago Drumond",
		"idade": 24,
		"cpf": "744.704.420-20",
		"rg": "24.612.924-4",
		"data_nasc": "12/04/2001",
		"sexo": "Masculino",
		"signo": "Áries",
		"mae": "Alessandra Marina",
		"pai": "André Yuri Drumond",
		"email": "miguel-drumond85@grupomegavale.com.br",
		"senha": "dywkGQymhu",
		"cep": "76962-208",
		"endereco": "Avenida Itapemirim",
		"numero": 913,
		"bairro": "Novo Cacoal",
		"cidade": "Cacoal",
		"estado": "RO",
		"telefone_fixo": "(69) 3999-9948",
		"celular": "(69) 99528-6924",
		"altura": "1,68",
		"peso": 81,
		"tipo_sanguineo": "B+",
		"cor": "vermelho"
	},
	{
		"nome": "Ian Felipe da Costa",
		"idade": 66,
		"cpf": "038.718.631-06",
		"rg": "37.517.985-9",
		"data_nasc": "08/04/1959",
		"sexo": "Masculino",
		"signo": "Áries",
		"mae": "Milena Antônia",
		"pai": "Matheus Mário da Costa",
		"email": "ian.felipe.dacosta@compuativa.com.br",
		"senha": "oPtN7qbOnh",
		"cep": "57061-624",
		"endereco": "Rua Gastone Lúcia de Carvalho Beltrão",
		"numero": 767,
		"bairro": "Tabuleiro do Martins",
		"cidade": "Maceió",
		"estado": "AL",
		"telefone_fixo": "(82) 3598-3617",
		"celular": "(82) 99258-0843",
		"altura": "1,65",
		"peso": 55,
		"tipo_sanguineo": "A-",
		"cor": "amarelo"
	},
	{
		"nome": "Marcelo Joaquim Antonio Silveira",
		"idade": 79,
		"cpf": "802.002.117-57",
		"rg": "40.322.127-4",
		"data_nasc": "19/03/1946",
		"sexo": "Masculino",
		"signo": "Peixes",
		"mae": "Emilly Isis Jennifer",
		"pai": "Theo Kevin Silveira",
		"email": "marcelo-silveira74@findout.com.br",
		"senha": "B3UqJfbHlR",
		"cep": "07400-190",
		"endereco": "Rua Angelina Augusto Fernandes",
		"numero": 216,
		"bairro": "Centro",
		"cidade": "Arujá",
		"estado": "SP",
		"telefone_fixo": "(11) 3644-7317",
		"celular": "(11) 99476-2918",
		"altura": "1,62",
		"peso": 75,
		"tipo_sanguineo": "B-",
		"cor": "vermelho"
	}
]
'''
