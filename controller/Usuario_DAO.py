import SQLite
# from model.Usuario import Usuario     # para testes da função create


def create(usuario):
    """Função para criar usuário no banco de dados"""

    # noinspection SqlInsertValues
    consulta = """
    INSERT INTO
      Usuarios (nome, sobrenome, cpf, email, senha)
    VALUES
      (?,?,?,?,?);
    """
    dados = (usuario.Nome, usuario.Sobrenome, usuario.CPF, usuario.Email, usuario.Senha)
    SQLite.executar_consulta_com_dados(consulta, dados)


def read():
    """Função para listar todos os usuários do banco de dados"""

    consulta = "SELECT * FROM Usuarios"
    return SQLite.executar_consulta(consulta)


def read_dados(busca, categoria):
    """
    Função para fazer uma busca específica, onde você insere um texto a ser encontrado numa determinada coluna da tabela
    categorias podem ser nome, sobrenome, ,cpf e email
    ex: read_dados("Mat", "nome") ou read_dados("123", "cpf")
    """
    consulta = """
        SELECT *
        FROM Usuarios
        WHERE {}
        LIKE ?
        """.format(categoria)
    dados = ('%' + busca + '%',)  # Não remova a vírgula senão eu paro de funcionar :)
    return SQLite.executar_consulta_com_dados(consulta, dados)


def update(id_usuario, info, categoria):
    """
    Função para atualizar usuários no banco de dados
    categorias podem ser nome, sobrenome, ,cpf, email e senha
    ex: update(1, "Matheus", "nome")

    OBS. verifique o id do usuário ANTES de fazer o update pra não ferrar com o banco :)
    """

    consulta = """
        UPDATE Usuarios
        SET {} = ?
        WHERE idUsuarios = {}
        """.format(categoria, id_usuario)
    dados = (info,)  # Não remova a vírgula senão eu paro de funcionar :)
    SQLite.executar_consulta_com_dados(consulta, dados)


def delete(id_usuario):
    """Função para remover usuário do banco"""

    consulta = "DELETE FROM Usuarios WHERE idUsuarios = {}".format(id_usuario)
    SQLite.executar_consulta(consulta)
