class Produto:

    def __init__(self, nome, descricao, quantidade, preco):
        self.Nome = nome
        self.Descricao = descricao
        self.Quantidade = quantidade
        self.Preco = preco

    def get_nome(self):
        return self.Nome

    def set_nome(self, nome):
        self.Nome = nome

    def get_descricao(self):
        return self.Descricao

    def set_descricao(self, descricao):
        self.Descricao = descricao

    def get_quantidade(self):
        return self.Quantidade

    def set_quantidade(self, quantidade):
        self.Quantidade = quantidade
    
    def get_preco(self):
        return self.Preco

    def set_preco(self, preco):
        self.Preco = preco
