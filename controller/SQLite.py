import sqlite3
from sqlite3 import Error


def criar_conexao():
    """Função para iniciar conexão com o Banco de Dados SQLite"""

    conexao = None
    try:
        conexao = sqlite3.connect("database.sqlite")
    except Error as e:
        print("Erro:", e)
    return conexao


def criar_db_usando_script(nome_do_arquivo):
    """Função para criar um Banco de Dados a partir de um script .sql"""

    db = criar_conexao()
    cursor = db.cursor()

    script = open(nome_do_arquivo).read()
    cursor.executescript(script)
    db.commit()
    db.close()


def executar_consulta(consulta):
    """Função para realizar consultas ao Banco de Dados SQLite"""

    db = criar_conexao()
    cursor = db.cursor()
    try:
        cursor.execute(consulta)
        if str(consulta).__contains__("SELECT"):
            return cursor.fetchall()
        db.commit()
        print("Consulta realizada com sucesso")
    except Error as e:
        print("Erro: ", e)
    finally:
        db.close()


def executar_consulta_com_dados(consulta, dados):
    """Função para realizar consultas com dados ao Banco de Dados SQLite"""

    db = criar_conexao()
    cursor = db.cursor()
    try:
        cursor.execute(consulta, dados)
        if str(consulta).__contains__("SELECT"):
            return cursor.fetchall()
        db.commit()
        print("Consulta realizada com sucesso")
    except Error as e:
        print("Erro: ", e)
    finally:
        db.close()
