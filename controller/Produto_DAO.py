import SQLite
# from model.Produto import Produto       # Usado para testes da função create


def create(produto):
    """Função para criar animal no banco de dados"""

    # noinspection SqlInsertValues
    consulta = """
        INSERT INTO
            Produtos (nome, descricao, quantidade, preco)
        VALUES 
            (?, ?, ?, ?);
    """
    dados = (produto.Nome, produto.Descricao, produto.Quantidade, produto.Preco)
    SQLite.executar_consulta_com_dados(consulta, dados)


def read():
    """Função para listar todos os animais do banco de dados"""

    consulta = "SELECT * FROM Produtos"
    return SQLite.executar_consulta(consulta)


def read_dados(busca, categoria):
    """
       Função para fazer uma busca específica, onde você insere um texto a ser encontrado numa determinada coluna da tabela
       categorias podem ser nome, tipo de animal, raça, tamanho e preço
       ex: read_dados("Bidu", "nome") ou read_dados("Grande", "tamanho")
       """

    consulta = """
        SELECT *
        FROM Produtos
        WHERE {}
        LIKE ?
    """.format(categoria)
    dados = ('%' + busca + '%',)
    return SQLite.executar_consulta_com_dados(consulta, dados)


def update(id_produto, info, categoria):
    """
        Função para atualizar animais no banco de dados
        categorias podem ser nome, tipo de animal, raça, tamanho e preço
        ex: update(1, "Pastor Alemão", "raca")

        OBS. verifique o id do usuário ANTES de fazer o update pra não ferrar com o banco :)
        """

    consulta ="""
        UPDATE  Produtos
        SET {} = ?
        WHERE idProdutos = {}
    """.format(categoria, id_produto)
    dados = (info,)
    return SQLite.executar_consulta_com_dados(consulta, dados)


def delete(id_produto):
    """Função para remover animais do banco de dados"""

    consulta = "DELETE FROM Produtos WHERE idProdutos = {}".format(id_produto)
    SQLite.executar_consulta(consulta)
