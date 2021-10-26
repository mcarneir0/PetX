--
-- File generated with SQLiteStudio v3.3.3 on ter out 12 14:30:25 2021
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Adocao_ou_Compra
DROP TABLE IF EXISTS Adocao_ou_Compra;
CREATE TABLE Adocao_ou_Compra (
	idAdocao_ou_compra INTEGER PRIMARY KEY NOT NULL,
	id_do_usuario INTEGER REFERENCES Usuarios (idUsuarios) NOT NULL,
	id_do_animal INTEGER REFERENCES Animais (idAnimais) UNIQUE NOT NULL,
	data TEXT NOT NULL
);

-- Table: Animais
DROP TABLE IF EXISTS Animais;
CREATE TABLE Animais (
	idAnimais INTEGER PRIMARY KEY NOT NULL,
	nome TEXT,
	tipo_de_animal TEXT NOT NULL,
	raca TEXT,
	tamanho TEXT NOT NULL,
	peso REAL,
	preco REAL
);

-- Table: Carrinho_de_Compras
DROP TABLE IF EXISTS Carrinho_de_Compras;
CREATE TABLE Carrinho_de_Compras (
	idCarrinho INTEGER PRIMARY KEY NOT NULL,
	id_do_pedido INTEGER REFERENCES Pedido (idPedido) NOT NULL,
	id_do_produto INTEGER REFERENCES Produtos (idProdutos) NOT NULL
);

-- Table: Pedido
DROP TABLE IF EXISTS Pedido;
CREATE TABLE Pedido (
	idPedido INTEGER PRIMARY KEY NOT NULL,
	id_do_usuario INTEGER REFERENCES Usuarios (idUsuarios) NOT NULL,
	data TEXT NOT NULL
);

-- Table: Produtos
DROP TABLE IF EXISTS Produtos;
CREATE TABLE Produtos (
	idProdutos INTEGER PRIMARY KEY NOT NULL,
	nome TEXT NOT NULL,
	descricao TEXT NOT NULL,
	preco REAL
);

-- Table: Usuarios
DROP TABLE IF EXISTS Usuarios;
CREATE TABLE Usuarios (
	idUsuarios INTEGER PRIMARY KEY NOT NULL,
	nome TEXT NOT NULL,
	sobrenome TEXT NOT NULL,
	cpf TEXT UNIQUE NOT NULL,
	email TEXT UNIQUE NOT NULL,
	senha TEXT NOT NULL
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;