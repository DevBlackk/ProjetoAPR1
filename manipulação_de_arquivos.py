### Manipulação de arquivos
import datetime

usuarios = [
    {"nome": "Camila Alves", "endereco": "Rua das Acácias", "numero": "101", "cep": "01002-010", "data_nasc": "10/05/1990", "profissao": "Arquiteta", "cpf": "111.222.333-01", "email": "camila.alves@emailficticio.com.br"},
    {"nome": "Bruno Costa", "endereco": "Avenida Ipiranga", "numero": "202", "cep": "02003-020", "data_nasc": "25/08/1982", "profissao": "Contador", "cpf": "222.333.444-02", "email": "bruno.costa82@meuemail.com"},
    {"nome": "Larissa Dias", "endereco": "Travessa dos Lírios", "numero": "30", "cep": "03004-030", "data_nasc": "12/01/1995", "profissao": "Psicóloga", "cpf": "333.444.555-03", "email": "lari.dias.psi@emailseguro.net"},
    {"nome": "Rodrigo Ferreira", "endereco": "Alameda das Gardênias", "numero": "404", "cep": "04005-040", "data_nasc": "03/11/1979", "profissao": "Jornalista", "cpf": "444.555.666-04", "email": "rodrigo.ferreira.jorn@provedorexemplo.com"},
    {"nome": "Sofia Gomes", "endereco": "Rua dos Girassóis", "numero": "505", "cep": "05006-050", "data_nasc": "18/07/2001", "profissao": "Estudante", "cpf": "555.666.777-05", "email": "sofia.g2001@emailuniversitario.edu.br"},
    {"nome": "Thiago Lima", "endereco": "Avenida Rebouças", "numero": "606", "cep": "06007-060", "data_nasc": "29/04/1988", "profissao": "Desenvolvedor Web", "cpf": "666.777.888-06", "email": "thiago.dev@webmailficticio.com"},
    {"nome": "Gabriela Martins", "endereco": "Praça Roosevelt", "numero": "70", "cep": "07008-070", "data_nasc": "07/09/1993", "profissao": "Publicitária", "cpf": "777.888.999-07", "email": "gabi.martins.publi@emailcriativo.com.br"},
    {"nome": "Daniel Nunes", "endereco": "Rua da Consolação", "numero": "808", "cep": "08009-080", "data_nasc": "14/02/1975", "profissao": "Engenheiro Civil", "cpf": "888.999.000-08", "email": "daniel.nunes.eng@meuprovedor.com"},
    {"nome": "Isabela Oliveira", "endereco": "Avenida Angélica", "numero": "909", "cep": "09010-090", "data_nasc": "21/06/1999", "profissao": "Fisioterapeuta", "cpf": "999.000.111-09", "email": "isa.oliveira.fisio@emaildesaude.com"},
    {"nome": "Leonardo Pereira", "endereco": "Rua Frei Caneca", "numero": "110", "cep": "01011-100", "data_nasc": "01/12/1986", "profissao": "Chef de Cozinha", "cpf": "000.111.222-10", "email": "leo.chef.pereira@saborearte.com.br"},
    {"nome": "Amanda Ribeiro", "endereco": "Largo do Arouche", "numero": "22", "cep": "02012-110", "data_nasc": "05/10/1991", "profissao": "Veterinária", "cpf": "123.456.789-11", "email": "amanda.vet.ribeiro@mundoanimalemail.com"},
    {"nome": "Felipe Santos", "endereco": "Rua Bela Cintra", "numero": "330", "cep": "03013-120", "data_nasc": "16/03/1983", "profissao": "Fotógrafo", "cpf": "234.567.890-12", "email": "felipe.santos.foto@cliquemail.com.br"},
    {"nome": "Clara Souza", "endereco": "Avenida Brigadeiro Faria Lima", "numero": "440", "cep": "04014-130", "data_nasc": "28/08/1997", "profissao": "Analista de Marketing", "cpf": "345.678.901-13", "email": "clara.mkt.souza@estrategiaemail.com"},
    {"nome": "Vinicius Teixeira", "endereco": "Rua Oscar Freire", "numero": "550", "cep": "05015-140", "data_nasc": "11/05/1970", "profissao": "Empresário", "cpf": "456.789.012-14", "email": "vinicius.teixeira@negociosonline.com.br"},
    {"nome": "Yasmin Vieira", "endereco": "Alameda Jaú", "numero": "66", "cep": "06016-150", "data_nasc": "23/09/1994", "profissao": "Nutricionista", "cpf": "567.890.123-15", "email": "yasmin.nutri.vieira@vidasaudavelemail.com"},
    {"nome": "Pedro Azevedo", "endereco": "Rua Haddock Lobo", "numero": "770", "cep": "07017-160", "data_nasc": "09/07/1980", "profissao": "Economista", "cpf": "678.901.234-16", "email": "pedro.azevedo.econ@analisefinanceira.com.br"},
    {"nome": "Laura Barros", "endereco": "Avenida Pacaembu", "numero": "880", "cep": "08018-170", "data_nasc": "02/02/2000", "profissao": "Designer de Interiores", "cpf": "789.012.345-17", "email": "laura.barros.design@ambientemail.com"},
    {"nome": "Guilherme Carvalho", "endereco": "Rua Itapeva", "numero": "99", "cep": "09019-180", "data_nasc": "13/10/1987", "profissao": "Consultor Financeiro", "cpf": "890.123.456-18", "email": "gui.carvalho.fin@consultoriaemail.com.br"},
    {"nome": "Manuela Castro", "endereco": "Praça Charles Miller", "numero": "121", "cep": "01020-190", "data_nasc": "20/04/1996", "profissao": "Personal Trainer", "cpf": "901.234.567-19", "email": "manu.castro.fit@treinoemail.com"},
    {"nome": "Enzo Cunha", "endereco": "Rua Pamplona", "numero": "212", "cep": "02021-200", "data_nasc": "06/11/1981", "profissao": "Piloto de Avião", "cpf": "012.345.678-20", "email": "enzo.piloto.cunha@voandomail.com.br"},
    {"nome": "Helena Dantas", "endereco": "Avenida Higienópolis", "numero": "313", "cep": "03022-210", "data_nasc": "17/01/1992", "profissao": "Bióloga", "cpf": "109.876.543-21", "email": "helena.dantas.bio@naturezamail.com"},
    {"nome": "Igor Esteves", "endereco": "Rua Maria Antônia", "numero": "414", "cep": "04023-220", "data_nasc": "27/05/1977", "profissao": "Mecânico", "cpf": "210.987.654-22", "email": "igor.mecanico@oficinaemail.com.br"},
    {"nome": "Júlia Farias", "endereco": "Alameda Lorena", "numero": "515", "cep": "05024-230", "data_nasc": "04/08/1989", "profissao": "Farmacêutica", "cpf": "321.098.765-23", "email": "julia.farias.farma@cuidadoemail.com"},
    {"nome": "Murilo Fernandes", "endereco": "Rua Estados Unidos", "numero": "616", "cep": "06025-240", "data_nasc": "10/06/1998", "profissao": "Técnico de Informática", "cpf": "432.109.876-24", "email": "murilo.ti.fernandes@suporteemail.net"},
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
    {"ISBN": "978-0-74-327356-5", "Título": "A Melodia Silenciosa da Alma", "Gênero": "Romance Contemporâneo", "Autores": ["Clara Mendes"], "Número de Páginas": 310},
    {"ISBN": "978-9-72-004384-8", "Título": "Histórias Não Contadas da Velha Vila", "Gênero": "Contos", "Autores": ["Antônio Pereira", "Júlia Silva"], "Número de Páginas": 215},
    {"ISBN": "978-0-14-103614-4", "Título": "O Código do Infinito", "Gênero": "Thriller Tecnológico", "Autores": ["Maximus Byte"], "Número de Páginas": 420},
    {"ISBN": "978-8-80-616040-8", "Título": "A Arte de Desaprender", "Gênero": "Filosofia", "Autores": ["Professor Kael"], "Número de Páginas": 180},
    {"ISBN": "978-1-85-326000-7", "Título": "Lendas do Reino Submerso", "Gênero": "Mitologia", "Autores": ["Marina Aguas"], "Número de Páginas": 390},
    {"ISBN": "978-0-30-759400-9", "Título": "O Segredo da Rosa Escarlate", "Gênero": "Romance Histórico", "Autores": ["Lady Annelise Beaumont"], "Número de Páginas": 480},
    {"ISBN": "978-4-08-874878-6", "Título": "A Jornada do Pequeno Samurai", "Gênero": "Infantojuvenil", "Autores": ["Yuki Sato"], "Número de Páginas": 150},
    {"ISBN": "978-0-67-973577-9", "Título": "Teoria Quântica para Céticos", "Gênero": "Divulgação Científica", "Autores": ["Dr. Elara Chen"], "Número de Páginas": 250},
    {"ISBN": "978-3-59-617892-9", "Título": "O Enigma da Mansão Abandonada", "Gênero": "Terror Gótico", "Autores": ["Victor Blackwood"], "Número de Páginas": 333},
    {"ISBN": "978-9-50-071290-1", "Título": "A Cozinha Afetiva da Vovó", "Gênero": "Culinária", "Autores": ["Nona Emilia"], "Número de Páginas": 170},
    {"ISBN": "978-0-45-152493-5", "Título": "Revolução nas Estrelas Distantes", "Gênero": "Ficção Científica Militar", "Autores": ["General Rex"], "Número de Páginas": 550},
    {"ISBN": "978-8-57-542788-6", "Título": "Poemas ao Luar", "Gênero": "Poesia", "Autores": ["Luna Seraphina"], "Número de Páginas": 120},
    {"ISBN": "978-1-40-007917-9", "Título": "A Sombra do Imperador Caído", "Gênero": "Fantasia Sombria", "Autores": ["Kaelen Morek"], "Número de Páginas": 410},
    {"ISBN": "978-0-31-262273-1", "Título": "Verdades Escondidas na Névoa", "Gênero": "Thriller Psicológico", "Autores": ["Dr. Evelyn Reed"], "Número de Páginas": 375},
    {"ISBN": "978-6-07-070849-5", "Título": "O Mapa dos Sonhos Perdidos", "Gênero": "Aventura Fantástica", "Autores": ["Marco Viajante"], "Número de Páginas": 305},
    {"ISBN": "978-1-59-307770-6", "Título": "Manual do Jovem Empreendedor", "Gênero": "Negócios", "Autores": ["Carlos Visionário", "Ana Prática"], "Número de Páginas": 200},
    {"ISBN": "978-0-81-299583-9", "Título": "A Última Canção da Floresta", "Gênero": "Realismo Fantástico", "Autores": ["Iara Verde"], "Número de Páginas": 260}
]

def calcular_idade(usuario):
    data_nasc = usuario["data_nasc"]
    data_atual = datetime.datetime.now().year
    ano_nasc = data_nasc.split('/')
    return int(data_atual) - int(ano_nasc[2])

