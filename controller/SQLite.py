import sqlite3
from sqlite3 import Error


def criar_conexao():
    conexao = None
    try:
        conexao = sqlite3.connect("database.sqlite")
    except Error as e:
        print("Erro:", e)
    return conexao


def criar_db_usando_script(nome_do_arquivo):
    db = criar_conexao()
    cursor = db.cursor()

    script = open(nome_do_arquivo)
    script_string = script.read()
    cursor.executescript(script_string)
    db.commit()
    db.close()


criar_db_usando_script("petx.sql")
