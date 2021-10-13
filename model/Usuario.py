class Usuario:

    def __init__(self, nome, sobrenome, cpf, email, senha):
        self.Nome = nome
        self.Sobrenome = sobrenome
        self.CPF = cpf
        self.Email = email
        self.Senha = senha

    def get_nome(self):
        return self.Nome

    def set_nome(self, nome):
        self.Nome = nome

    def get_sobrenome(self):
        return self.Sobrenome

    def set_sobrenome(self, sobrenome):
        self.Sobrenome = sobrenome

    def get_cpf(self):
        return self.CPF

    def set_cpf(self, cpf):
        self.CPF = cpf

    def get_email(self):
        return self.Email

    def set_email(self, email):
        self.Email = email
