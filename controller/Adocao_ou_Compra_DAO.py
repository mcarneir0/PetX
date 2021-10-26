from controller import SQLite
from datetime import datetime


def create(id_usuario, id_animal):
    """Função para cadastrar uma compra ou adoção de animal no banco de dados"""

    # noinspection SqlInsertValues
    consulta = """
        INSERT INTO
           Adocao_ou_Compra (id_do_usuario, id_do_animal, data)
        VALUES 
            (?, ?, ?);
    """

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Obtendo data e hora
    dados = (id_usuario, id_animal, data)
    SQLite.executar_consulta_com_dados(consulta, dados)


def read():
    """Função para listar todas as adoções ou compras de animais"""

    consulta = "SELECT * FROM Adocao_ou_Compra"
    return SQLite.executar_consulta(consulta)


def read_dados(busca, categoria):
    """
    Função para fazer uma busca específica, onde você insere um texto a ser encontrado numa determinada coluna da tabela
    categorias podem ser id do Usuário, id do Animal ou data da adoção/compra
    ex: read_dados("1", "id_do_usuario") ou read_dados("5", "id_do_animal") ou read_dados("25/10/2021", data)
    """

    consulta = """
        SELECT *
        FROM Adocao_ou_Compra
        WHERE {}
        LIKE ?
    """.format(categoria)

    dados = ('%' + busca + '%',)  # Não remova a vírgula senão eu paro de funcionar :)
    return SQLite.executar_consulta_com_dados(consulta, dados)


def update(id_adocao_ou_compra, info, categoria):
    """
    Função para editar adoções e compras  no banco de dados
    categorias podem ser id do Usuário, id do Animal ou data da adoção/compra
    ex: update(1, 3, "id_do_animal") ou update(2, "25/10/2021 21:53:00")

    OBS. verifique o id da adoção/compra ANTES de fazer o update pra não ferrar com o banco :)
    """

    consulta = """
        UPDATE Adocao_ou_Compra
        SET {} = ?
        WHERE idAdocao_ou_compra = {}
    """.format(categoria, id_adocao_ou_compra)

    dados = (info,)  # Não remova a vírgula senão eu paro de funcionar :)
    SQLite.executar_consulta_com_dados(consulta, dados)


def delete(id_adocao_ou_compra):
    """Função para remover adoções ou compras do banco de dados"""

    consulta = "DELETE FROM Adocao_ou_Compra WHERE idAdocao_ou_compra = {}".format(id_adocao_ou_compra)
    SQLite.executar_consulta(consulta)
