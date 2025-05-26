# Projeto de APR1 do IFSP - Campus São Carlos

## Descritivo do projeto

Uma aplicação para uma Biblioteca precisa armazenar informações sobre os seus
usuários (alunos e professores), livros e sobre o empréstimo de livros. Os dados a serem
armazenados sobre cada uma dessas entidades são apresentados a seguir:

- Usuário = (CPF, Nome, Rua, Nro, CEP, E-mails, Telefones, Data de Nascimento, Profissão)
- Livro = (ISBN, Título, Gênero, Autores, Número de Páginas)
- Empréstimo = (CPF Pessoa, ISBN Livro, Data de Retirada, Data de Devolução, Valor Diário da Multa por atraso)

        Atenção: os atributos grifados são chaves e você NÃO deve permitir a inclusão de mais de um cadastro com os mesmos valores para os atributos chaves.

*Utilizando os conhecimentos aprendidos nas aulas, desenvolva um programa em
Python que apresente o seguinte menu de opções para o usuário e implemente cada operação
usando função. Escolha a estrutura de dados mais apropriada para armazenar os dados de
cada entidade descrita anteriormente.*

### Menu de Opções:
    
    1. Submenu de Usuários
    2. Submenu de Livros
    3. Submenu de Empréstimos
    4. Submenu Relatórios
    5. Sair

### Cada Submenu deverá oferecer as opções: 

**Listar todos, Listar um elemento específico do conjunto, Incluir (sem repetição), Alterar e Excluir (após confirmação dos dados) um elemento do conjunto.**
  
- Observe que os atributos que estão no plural indicam que deverá ser possível incluir vários itens daquele mesmo atributo. 

Por exemplo, o atributo **Telefones** indica que uma pessoa pode ter vários telefones (a quantidade é indefinida). Portanto, deve-se utilizar uma estrutura que seja adequada para armazenar todos os telefones que a entidade possuir. O Submenu Relatórios deverá ter uma opção para cada um dos relatórios solicitados a seguir.

**Relatórios:**

a) Mostrar todos os dados de todos os usuários com mais de X anos de idade, onde X é fornecido pelo usuário;

b) Mostrar todos os dados de todos os livros que tenham mais do que X autores, sendo X fornecido pelo usuário;

c) Mostrar o CPF da pessoa, o nome da pessoa, o ISBN do livro, o título do livro e todos os demais atributos dos empréstimos que possuem data de devolução entre as datas X e Y (inclusive), ambas fornecidas pelo usuário.

    Obs: Não utilize variáveis globais. Use parâmetros para fazer a transferência de valores entre as funções. Dê nomes significativos para variáveis e funções.

*O programa deverá utilizar Arquivos para a persistência dos dados manipulados pela aplicação.*

Em outras palavras, cada registro de Usuário, Livro e de Empréstimo deverá ser armazenado em um arquivo texto específico, que conterá apenas registros daquele
mesmo tipo de entidade. O submenu Relatórios também deverá usar arquivos textos para a persistência dos relatórios gerados.
