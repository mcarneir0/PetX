from controller import SQLite
# from model.Animal import Animal       # Usado para testes da função create


def create(animal):
    """Função para criar animal no banco de dados"""

    # noinspection SqlInsertValues
    consulta = """
        INSERT INTO
            Animais (nome, tipo_de_animal, raca, tamanho, preco)
        VALUES 
            (?, ?, ?, ?, ?);
    """
    dados = (animal.Nome, animal.Tipo_de_Animal, animal.Raca, animal.Tamanho, animal.Preco)
    SQLite.executar_consulta_com_dados(consulta, dados)


def read():
    """Função para listar todos os animais do banco de dados"""

    consulta = "SELECT * FROM Animais"
    return SQLite.executar_consulta(consulta)


def read_dados(busca, categoria):
    """
    Função para fazer uma busca específica, onde você insere um texto a ser encontrado numa determinada coluna da tabela
    categorias podem ser nome, tipo de animal, raça, tamanho e preço
    ex: read_dados("Bidu", "nome") ou read_dados("Grande", "tamanho")
    """

    consulta = """
        SELECT *
        FROM Animais
        WHERE {}
        LIKE ?
    """.format(categoria)
    dados = ('%' + busca + '%',)  # Não remova a vírgula senão eu paro de funcionar :)
    return SQLite.executar_consulta_com_dados(consulta, dados)


def update(id_animal, info, categoria):
    """
    Função para atualizar animais no banco de dados
    categorias podem ser nome, tipo de animal, raça, tamanho e preço
    ex: update(1, "Pastor Alemão", "raca")

    OBS. verifique o id do usuário ANTES de fazer o update pra não ferrar com o banco :)
    """

    consulta = """
        UPDATE Animais
        SET {} = ?
        WHERE idAnimais = {}
    """.format(categoria, id_animal)
    dados = (info,)  # Não remova a vírgula senão eu paro de funcionar :)
    SQLite.executar_consulta_com_dados(consulta, dados)


def delete(id_animal):
    """Função para remover animais do banco de dados"""

    consulta = "DELETE FROM Animais WHERE idAnimais = {}".format(id_animal)
    SQLite.executar_consulta(consulta)
