class Animal:

    def __init__(self, nome, tipo_de_animal, raca, tamanho, peso, preco):
        self.Nome = nome
        self.Tipo_de_Animal = tipo_de_animal
        self.Raca = raca
        self.Tamanho = tamanho
        self.Peso = peso
        self.Preco = preco

    def get_nome(self):
        return self.Nome

    def set_nome(self, nome):
        self.Nome = nome

    def get_tipo_de_animal(self):
        return self.Tipo_de_Animal

    def set_tipo_de_animal(self, tipo_de_animal):
        self.Tipo_de_Animal = tipo_de_animal

    def get_raca(self):
        return self.Raca

    def set_raca(self, raca):
        self.Raca = raca

    def get_tamanho(self):
        return self.Tamanho

    def set_tamanho(self, tamanho):
        self.Tamanho = tamanho

    def get_peso(self):
        return self.Peso

    def set_peso(self, peso):
        self.Peso = peso

    def get_preco(self):
        return self.Preco

    def set_preco(self, preco):
        self.Preco = preco
