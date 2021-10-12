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
	idAdocao_ou_Compra INTEGER PRIMARY KEY NOT NULL,
	id_do_Usuario INTEGER REFERENCES Usuarios (idUsuarios) NOT NULL,
	id_do_Animal INTEGER REFERENCES Animais (idAnimais) NOT NULL,
	data DATE NOT NULL, preco REAL
);

-- Table: Animais
DROP TABLE IF EXISTS Animais;
CREATE TABLE Animais (
	idAnimais INTEGER PRIMARY KEY NOT NULL,
	idTipo_de_Animal INTEGER REFERENCES Tipo_de_Animal (idTipo_de_Animal) NOT NULL,
	nome TEXT,
	raca TEXT,
	tamanho TEXT NOT NULL,
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
	id_do_Usuario INTEGER REFERENCES Usuarios (idUsuarios) NOT NULL,
	data DATE NOT NULL,
	valor_total REAL
);

-- Table: Produtos
DROP TABLE IF EXISTS Produtos;
CREATE TABLE Produtos (
	idProdutos INTEGER PRIMARY KEY NOT NULL,
	nome TEXT NOT NULL,
	descricao TEXT NOT NULL,
	preco REAL
);

-- Table: Tipo_de_Animal
DROP TABLE IF EXISTS Tipo_de_Animal;
CREATE TABLE Tipo_de_Animal (
	idTipo_de_Animal INTEGER PRIMARY KEY NOT NULL,
	nome TEXT NOT NULL
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
