class Produto:

    def __init__(self, nome, descricao, preco):
        self.Nome = nome
        self.Descricao = descricao
        self.Preco = preco

    def get_nome(self):
        return self.Nome

    def set_nome(self, nome):
        self.Nome = nome

    def get_descricao(self):
        return self.Descricao

    def set_descricao(self, descricao):
        self.Descricao = descricao
    
    def get_preco(self):
        return self.Preco

    def set_preco(self, preco):
        self.Preco = preco
