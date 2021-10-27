from tkinter import *
from ttkbootstrap import Style
from PIL import ImageTk, Image
from tkinter import ttk
from controller import Usuario_DAO
from controller import Animal_DAO
from controller import Produto_DAO
from controller import Adocao_ou_Compra_DAO
from model.Usuario import Usuario
from model.Animal import Animal
from model.Produto import Produto
from functools import partial
import numpy as np



tela_inicial = Tk()
tela_inicial.title("PetX")
tela_inicial.resizable(FALSE, FALSE)
tela_inicial.iconbitmap("Imagens\pet.ico")
tela_inicial.geometry("1100x750+800+50")
largura = 1100
altura = 750

style = Style('minty')
tela_inicial = style.master

imagem = ImageTk.PhotoImage(Image.open("Imagens\petx.png"))
imagemL = Label(image=imagem)
imagemL.place(x=300, y=50)


# metodos

def esconde_frame():
    frame_login.pack_forget()
    frame_cadastrar.pack_forget()
    produtos_frame.pack_forget()
    frame_animais.pack_forget()
    frame_adocao.pack_forget()
    frame_compra.pack_forget()
    frame_tela_inicial.pack_forget()
    frame_carrinho.pack_forget()
    frame_pedidos.pack_forget()
    frame_listar_usuarios.pack_forget()
    frame_listar_produtos.pack_forget()
    frame_listar_animais.pack_forget()
    
    


def cadastrar_usuario():
    qtd_usuarios = len(Usuario_DAO.read())
    pessoa = Usuario(nome_tela.get(), sobrenome_tela.get(), cpf_tela.get(), email_tela.get(), senha_tela.get())
    Usuario_DAO.create(pessoa)
    # Condição ternária abaixo > <Caso falso> if <teste> else <Caso verdadeiro>
    cadastro_erro() if qtd_usuarios == len(Usuario_DAO.read()) else cadastro_sucesso()

def cadastrar_produto():
    qtd_produtos = len(Produto_DAO.read())
    produtos = Produto(nome_produto_janela.get(), descricao_lb_janela.get(), quantidade_lb_janela.get(), preco_lb_janela.get())
    Produto_DAO.create(produtos)
    cadastro_produto_erro() if qtd_produtos == len(Produto_DAO.read()) else cadastro_produto_sucesso()

def cadastrar_animais():
    qtd_animais = len(Animal_DAO.read())
    animais = Animal(nome_animais_janela.get(), tipo_animais_janela.get() , raca_animais_janela.get(),
                     tamanho_animais_janela.get(), peso_animais_janela.get(), preco_animais_janela.get())
    Animal_DAO.create(animais)
    cadastro_animal_erro() if qtd_animais == len(Animal_DAO.read()) else cadastro_animal_sucesso()

def cadastrar_adocao():
    Adocao_ou_Compra_DAO.create(cod_user_janela.get(), cod_animal_janela.get())

def cadastrar_compra():
    Adocao_ou_Compra_DAO.create(cod_user_janela2.get(), cod_animal_janela2.get())



def cadastro_sucesso():
    confirmacao = Toplevel(frame_cadastrar)
    Label(confirmacao, text="Usuário cadastrado com sucesso!").pack()
    esconde_frame()


def cadastro_erro():
    confirmacao = Toplevel(frame_cadastrar)
    Label(confirmacao, text="Usuário não cadastrado, tente novamente").pack()
    frame_cadastrar.pack(fill="both", expand=1)

def cadastro_produto_sucesso():
    confirmacao = Toplevel(frame_tela_inicial)
    texto = Label(confirmacao, text="Produto cadastrado com sucesso!").pack()
    frame_carrinho.pack(fill="both", expand=1)
    esconde_frame()

def cadastro_produto_erro():
    confirmacao = Toplevel(frame_cadastrar)
    Label(confirmacao, text="Produto não cadastrado, tente novamente").pack()
    frame_produtos.pack(fill="both", expand=1)

def cadastro_animal_sucesso():
    confirmacao = Toplevel(frame_tela_inicial)
    Label(confirmacao, text="Animal cadastrado com sucesso!").pack()
    frame_animais.pack(fill="both", expand=1)
    esconde_frame()

def cadastro_animal_erro():
    confirmacao = Toplevel(frame_animais)
    Label(confirmacao, text="Animal não cadastrado, tente novamente").pack()
    frame_animais.pack(fill="both", expand=1)


def entrar():
    esconde_frame()
    frame_tela_inicial.pack(fill="both", expand=1)


def frame_login():
    esconde_frame()
    frame_login.pack(fill="both", expand=1)


def frame_cadastrar():
    esconde_frame()
    frame_cadastrar.pack(fill="both", expand=1)


def frame_produtos():
    esconde_frame()
    produtos_frame.pack(fill="both", expand=1)


def frame_animais():
    esconde_frame()
    frame_animais.pack(fill="both", expand=1)


def frame_adocao():
    esconde_frame()
    frame_adocao.pack(fill="both", expand=1)


def frame_compra():
    esconde_frame()
    frame_compra.pack(fill="both", expand=1)


def frame_carrinho():
    esconde_frame()
    frame_carrinho.pack(fill="both", expand=1)


def frame_pedidos():
    esconde_frame()
    frame_pedidos.pack(fill="both", expand=1)

def confirm_sair(): 
    confirmacao = Toplevel(tela_inicial)
    texto = Label(confirmacao, text="Deseja realmente sair?").pack()
    botaoSim = Button(confirmacao, text="Sim", command=tela_inicial.destroy).pack()
    botaoNao = Button(confirmacao, text="Não", command=confirmacao.destroy).pack()

def sair_de_cadastro():
    frame_cadastrar.pack_forget()
    frame_login.pack(fill="both", expand=1)


def sair():
    esconde_frame()
    frame_tela_inicial.pack(fill="both", expand=1)




def listar_usuarios():
    esconde_frame()
    frame_listar_usuarios.pack(fill="both", expand=1)
    registros = np.asarray(Usuario_DAO.read())

    for i in dados.get_children():
        dados.delete(i)

    for i in range(registros.shape[0]):
        dados.insert(parent='', index=0, values=(registros[i][0], registros[i][1], registros[i][2], registros[i][3], registros[i][4]))



def listar_produtos():
    esconde_frame()
    frame_listar_produtos.pack(fill="both", expand=1)
    registros = np.asarray(Produto_DAO.read())

    for i in dados2.get_children():
        dados2.delete(i)

    for i in range(registros.shape[0]):
        dados2.insert(parent='', index=0, values=(registros[i][0], registros[i][1], registros[i][2], registros[i][3], registros[i][4]))



def listar_animais():
    esconde_frame()
    frame_listar_animais.pack(fill="both", expand=1)
    registros = np.asarray(Animal_DAO.read)

    for i in dados3.get_children():
        dados3.delete(i)

    for i in range(registros.shape[0]):
        dados3.insert(parent='', index=0, values=(registros[i][0], registros[i][1], registros[i][2], registros[i][3], registros[i][4], registros[i][5]))


# menus

menubar = Menu(tela_inicial)
Login = Menu(menubar, tearoff=0)
Login.add_command(label="Login", command=frame_login)
Login.add_command(label="Cadastre-se", command=frame_cadastrar)
Login.add_separator()
menubar.add_cascade(label="Login", menu=Login)

Produtos = Menu(menubar, tearoff=0)
Produtos.add_command(label="Produtos", command=frame_produtos)
menubar.add_cascade(label="Produtos", menu=Produtos)

Pedidos = Menu(menubar, tearoff=0)
Pedidos.add_command(label="Pedidos", command=frame_pedidos)
menubar.add_cascade(label="Pedidos", menu=Pedidos)

Animais = Menu(menubar, tearoff=0)
Animais.add_command(label="Animais", command=frame_animais)
Animais.add_command(label="Adoção", command=frame_adocao)
Animais.add_command(label="Compra", command=frame_compra)
menubar.add_cascade(label="Animais", menu=Animais)

# frames


# frame tela inicial

frame_tela_inicial = Frame(tela_inicial, width=largura, height=altura)

bt_cadastrar_produtos = Button(frame_tela_inicial, text="CADASTRAR PRODUTOS", font=('Helvetica', 18), command=frame_produtos)
bt_cadastrar_produtos.place(x = 10, y = 500)

bt_cadastrar_animais = Button(frame_tela_inicial, text="CADASTRAR ANIMAIS", font=('Helvetica', 18), command=frame_animais)
bt_cadastrar_animais.place(x = 10, y = 550)

bt_cadastrar = Button(frame_tela_inicial, text="CADASTRE-SE", font=('Helvetica', 18), command=frame_cadastrar)
bt_cadastrar.place(x = 10, y = 600)

bt_listar_animais = Button(frame_tela_inicial, text="ANIMAIS CADASTRADOS", font=('Helvetica', 18), command=listar_animais)
bt_listar_animais.place(x=750, y=500)

bt_listar_produtos = Button(frame_tela_inicial, text="PRODUTOS CADASTRADOS", font=('Helvetica', 18), command=listar_produtos)
bt_listar_produtos.place(x=750, y=550)

bt_listar_usuarios = Button(frame_tela_inicial, text="USUÁRIOS CADASTRADOS", font=('Helvetica', 18), command=listar_usuarios)
bt_listar_usuarios.place(x=750, y=600)

bt_listar_pedidos = Button(frame_tela_inicial, text="LISTAR PEDIDOS", font=('Helvetica', 9))
bt_listar_pedidos.place(x=900, y=80)

bt_carrinho = Button(frame_tela_inicial, text="CARRINHO DE COMPRAS", font=('Helvetica', 9), command=frame_carrinho)
bt_carrinho.place(x = 900, y = 50)

bt_sair = Button(frame_tela_inicial, text="SAIR", font=('Helvetica', 15), command=confirm_sair)
bt_sair.place(x=500, y=650)

# frame login

frame_login = Frame(tela_inicial, width=largura, height=altura)

usuario = Label(frame_login, width=12, text="Usuário")
usuario.place(x="430", y="525")
user_janela = Entry(frame_login)
user_janela.place(x="460", y="550")

senha = Label(frame_login, width=12, text="Senha")
senha.place(x="430", y="585")
senha_tela = Entry(frame_login)
senha_tela.place(x="460", y="610")

botao_entrar = Button(frame_login, text="Entrar", command=entrar)
botao_entrar.place(x="460", y="650")

imagem = ImageTk.PhotoImage(Image.open("Imagens\petx.png"))
imagemL = Label(image=imagem)
imagemL.place(x=300, y=50)

# frame cadastrar

frame_cadastrar = Frame(tela_inicial, width=largura, height=altura)

titulo = ttk.Label(frame_cadastrar, text="Cadastre-se",
                   style="primary.Inverse.TLabel",
                   padding=(50, 30, 50, 30),
                   font=('Helvetica', 30))
titulo.place(x=400, y=40)



nome_lb = Label(frame_cadastrar, text="NOME", font=('Helvetica', 13))
nome_lb.place(x=425, y=200)
nome_tela = Entry(frame_cadastrar)
nome_tela.place(x=425, y=225)

sobrenome_lb = Label(frame_cadastrar, text="SOBRENOME", font=('Helvetica', 13))
sobrenome_lb.place(x=425, y=250)
sobrenome_tela = Entry(frame_cadastrar)
sobrenome_tela.place(x=425, y=275)

cpf_lb = Label(frame_cadastrar, text="CPF", font=('Helvetica', 13))
cpf_lb.place(x=425, y=300)
cpf_tela = Entry(frame_cadastrar)
cpf_tela.place(x=425, y=325)

email_lb = Label(frame_cadastrar, text="EMAIL", font=('Helvetica', 13))
email_lb.place(x=425, y=350)
email_tela = Entry(frame_cadastrar)
email_tela.place(x=425, y=375)

senha_lb = Label(frame_cadastrar, text="SENHA", font=('Helvetica', 13))
senha_lb.place(x=425, y=400)
senha_tela = Entry(frame_cadastrar)
senha_tela.place(x=425, y=425)

cadastrar_bt = Button(frame_cadastrar, text="Cadastrar", font=('Helvetica', 13), command=partial(cadastrar_usuario))
cadastrar_bt.place(x=425, y=480)

quit_bt = Button(frame_cadastrar, text="Sair", font=('Helvetica', 13), command=sair_de_cadastro)
quit_bt.place(x = 530, y=480)

# frame produtos

produtos_frame = Frame(tela_inicial, width=largura, height=altura)
titulo_produtos = ttk.Label(produtos_frame, text="Produtos",
                            style="primary.Inverse.TLabel",
                            padding=(50, 30, 50, 30),
                            font=('Helvetica', 30))
titulo_produtos.place(x=400, y=40)

nome_produto_lb = Label(produtos_frame, text="NOME DO PRODUTO", font=('Helvetica', 13))
nome_produto_lb.place(x=425, y=160)
nome_produto_janela = Entry(produtos_frame)
nome_produto_janela.place(x=425, y=190)

descricao_lb = Label(produtos_frame, text="DESCRIÇÃO", font=('Helvetica', 13))
descricao_lb.place(x=425, y=220)
descricao_lb_janela = Entry(produtos_frame)
descricao_lb_janela.place(x=425, y=250)

quantidade_lb = Label(produtos_frame, text="QUANTIDADE", font=('Helvetica', 13))
quantidade_lb.place(x=425, y=280)
quantidade_lb_janela = Entry(produtos_frame)
quantidade_lb_janela.place(x=425, y=310)

preco_lb = Label(produtos_frame, text="PREÇO", font=('Helvetica', 13))
preco_lb.place(x=425, y=340)
preco_lb_janela = Entry(produtos_frame)
preco_lb_janela.place(x=425, y=370)

carrinho_bt = Button(produtos_frame, text="Cadastrar pedido", font=('Helvetica', 13), command=lambda:[frame_pedidos, cadastrar_produto()])
carrinho_bt.place(x=425, y=420)

sair_bt = Button(produtos_frame, text="Sair", font=('Helvetica', 13), command=sair)
sair_bt.place(x = 425, y = 460)

# frame animais

frame_animais = Frame(tela_inicial, width=largura, height=altura)
titulo_animais = ttk.Label(frame_animais, text="Animais",
                           style="primary.Inverse.TLabel", padding=(50, 30, 50, 30),
                           font=('Helvetica', 30))
titulo_animais.place(x=400, y=40)


nome_animais_lb = Label(frame_animais, text="NOME DO ANIMAL", font=('Helvetica', 13))
nome_animais_lb.place(x=425, y=160)
nome_animais_janela = Entry(frame_animais)
nome_animais_janela.place(x=425, y=190)


tipo_animais_lb = Label(frame_animais, text="TIPO DO ANIMAL", font=('Helvetica', 13))
tipo_animais_lb.place(x=425, y=220)
tipo_animais_janela = Entry(frame_animais)
tipo_animais_janela.place(x=425, y=250)


raca_animais_lb = Label(frame_animais, text="RAÇA DO ANIMAL", font=('Helvetica', 13))
raca_animais_lb.place(x=425, y=280)
raca_animais_janela = Entry(frame_animais)
raca_animais_janela.place(x=425, y=310)

tamanho_animais_lb = Label(frame_animais, text="TAMANHO DO ANIMAL", font=('Helvetica', 13))
tamanho_animais_lb.place(x=425, y=340)
tamanho_animais_janela = Entry(frame_animais)
tamanho_animais_janela.place(x=425, y=370)

peso_animais_lb = Label(frame_animais, text="PESO DO ANIMAL", font=('Helvetica', 13))
peso_animais_lb.place(x=425, y=400)
peso_animais_janela = Entry(frame_animais)
peso_animais_janela.place(x=425, y=430)

preco_animais_lb = Label(frame_animais, text="PREÇO DO ANIMAL", font=('Helvetica', 13))
preco_animais_lb.place(x=425, y=460)
preco_animais_janela = Entry(frame_animais)
preco_animais_janela.place(x=425, y=490)



adocao_bt = Button(frame_animais, text="Cadastrar Animal para Adoção",font=('Helvetica', 13), command=lambda:[frame_adocao, cadastrar_animais()])
adocao_bt.place(x = 250, y = 580)

prosseguir_bt = Button(frame_animais, text="Prosseguir para Adoção",font=('Helvetica', 13), command=frame_adocao)
prosseguir_bt.place(x = 250, y = 630)

compra_bt = Button(frame_animais, text="Cadastrar Animal para Compra",font=('Helvetica', 13), command=lambda:[frame_compra, cadastrar_animais()] )
compra_bt.place(x = 600, y = 580)

prosseguir_bt2 = Button(frame_animais, text="Prosseguir para Compra",font=('Helvetica', 13), command=frame_compra)
prosseguir_bt2.place(x = 600, y = 630)

voltar_bt = Button(frame_animais, text="Sair", font=('Helvetica', 13), command=sair)
voltar_bt.place(x = 520, y = 670)


# frame adoção

frame_adocao = Frame(tela_inicial, width=largura, height=altura)
titulo_adocao = ttk.Label(frame_adocao, text="Adoção",
                          style="primary.Inverse.TLabel", padding=(50, 30, 50, 30),
                          font=('Helvetica', 30))
titulo_adocao.place(x=400, y=40)


cod_user_lb = Label(frame_adocao, text="COD USUÁRIO", font=('Helvetica', 13))
cod_user_lb.place(x=425, y=160)
cod_user_janela = Entry(frame_adocao)
cod_user_janela.place(x=425, y=190)

cod_animal_lb = Label(frame_adocao, text="COD ANIMAL", font=('Helvetica', 13))
cod_animal_lb.place(x=425, y=220)
cod_animal_janela = Entry(frame_adocao)
cod_animal_janela.place(x=425, y=250)



bt_cadastrar_adocao = Button(frame_adocao, text="Cadastrar Adoção", font=('Helvetica', 13), command=cadastrar_adocao)
bt_cadastrar_adocao.place(x = 425, y=330)

bt_pedido = Button(frame_adocao, text="Prosseguir para Pedido", font=('Helvetica', 13), command=frame_pedidos)
bt_pedido.place(x = 425, y=380)

sair_bt = Button(frame_adocao, text="Sair", font=('Helvetica', 13), command=sair)
sair_bt.place(x = 425, y = 440)




# frame compra

frame_compra = Frame(tela_inicial, width=largura, height=altura)
titulo_compra = ttk.Label(frame_compra, text="Compra",
                          style="primary.Inverse.TLabel", padding=(50, 30, 50, 30),
                          font=('Helvetica', 30))
titulo_compra.place(x=400, y=40)


cod_user_lb = Label(frame_compra, text="COD USUÁRIO", font=('Helvetica', 13))
cod_user_lb.place(x=425, y=160)
cod_user_janela2 = Entry(frame_compra)
cod_user_janela2.place(x=425, y=190)

cod_animal_lb = Label(frame_compra, text="COD ANIMAL", font=('Helvetica', 13))
cod_animal_lb.place(x=425, y=220)
cod_animal_janela2 = Entry(frame_compra)
cod_animal_janela2.place(x=425, y=250)


bt_cadastrar_compra = Button(frame_compra, text="Cadastrar Compra", font=('Helvetica', 13), command=cadastrar_compra)
bt_cadastrar_compra.place(x = 425, y=340)

bt_pedido2 = Button(frame_compra, text="Prosseguir para Pedido", font=('Helvetica', 13), command=frame_pedidos)
bt_pedido2.place(x = 425, y=390)

sair3_bt = Button(frame_compra, text="Sair", font=('Helvetica', 13), command=sair)
sair3_bt.place(x = 425, y = 440)

# frame carrinho de compras

frame_carrinho = Frame(tela_inicial, width=largura, height=altura)
titulo_carrinho = ttk.Label(frame_carrinho, text="Carrinho de compras",
                            style="primary.Inverse.TLabel", padding=(50, 30, 50, 30),
                            font=('Helvetica', 30))
titulo_carrinho.place(x=340, y=40)

cod_pedido_lb = Label(frame_carrinho, text="COD PEDIDO", font=('Helvetica', 13))
cod_pedido_lb.place(x=425, y=160)
cod_pedido_janela = Entry(frame_carrinho)
cod_pedido_janela.place(x=425, y=190)

cod_produto_lb = Label(frame_carrinho, text="COD PRODUTO", font=('Helvetica', 13))
cod_produto_lb.place(x=425, y=220)
cod_produto_janela = Entry(frame_carrinho)
cod_produto_janela.place(x=425, y=250)

compra_finalizada_bt = Button(frame_carrinho, text="Finalizar compra", font=('Helvetica', 13))
compra_finalizada_bt.place(x = 425, y=325)

# frame listar usuarios cadastrados

frame_listar_usuarios = Frame(tela_inicial, width = 1100, height = 750)

titulo_ = ttk.Label(frame_listar_usuarios, text = "Usuários cadastrados", 
                   style="primary.Inverse.TLabel",
                   padding=(50,30,50,30),
                   font=('Helvetica', 30))
titulo_.place(x = 400, y= 40)


dados = ttk.Treeview(frame_listar_usuarios, columns=[1,2,3,4,5], show='headings', style='sucess.Treeview')
dados.heading(1, text="Nome")
dados.heading(2, text="Sobrenome")
dados.heading(3, text="Cpf")
dados.heading(4, text="Email")
dados.heading(5, text="Senha")

dados.grid(row=1, column=0)

# frame listar produtos

frame_listar_produtos = Frame(tela_inicial, width = 1100, height = 750)

titulo_2 = ttk.Label(frame_listar_produtos, text = "Produtos cadastrados", 
                   style="primary.Inverse.TLabel",
                   padding=(50,30,50,30),
                   font=('Helvetica', 30))
titulo_2.place(x = 400, y= 40)


dados2 = ttk.Treeview(frame_listar_produtos, columns=[1,2,3,4], show='headings', style='sucess.Treeview')
dados2.heading(1, text="Nome")
dados2.heading(2, text="Descrição")
dados2.heading(3, text="Quantidade")
dados2.heading(4, text="Preço")


dados2.grid(row=1, column=0)


# frame listar animais

frame_listar_animais = Frame(tela_inicial, width = 1100, height = 750)

titulo_3 = ttk.Label(frame_listar_animais, text = "Animais cadastrados", 
                   style="primary.Inverse.TLabel",
                   padding=(50,30,50,30),
                   font=('Helvetica', 30))
titulo_3.place(x = 400, y= 40)

dados3 = ttk.Treeview(frame_listar_animais, columns=[1,2,3,4,5,6], show='headings', style='sucess.Treeview')

dados3.heading(1, text="Nome")
dados3.heading(2, text="Tipo do animal")
dados3.heading(3, text="Raça")
dados3.heading(4, text="Tamanho")
dados3.heading(5, text="Peso")
dados3.heading(6, text="Preço")

dados3.grid(row=1, column=0)


# frame pedidos

frame_pedidos = Frame(tela_inicial, width=largura, height=altura)
titulo_pedidos = ttk.Label(frame_pedidos, text="Pedidos",
                           style="primary.Inverse.TLabel", padding=(50, 30, 50, 30),
                           font=('Helvetica', 30))
titulo_pedidos.place(x=400, y=40)


cod_usuario_lb = Label(frame_pedidos, text="COD USUÁRIO", font=('Helvetica', 13))
cod_usuario_lb.place(x=425, y=160)
cod_usuario_janela = Entry(frame_pedidos)
cod_usuario_janela.place(x=425, y=190)

data_lb = Label(frame_pedidos, text="DATA", font=('Helvetica', 13))
data_lb.place(x=425, y=220)
data_janela = Entry(frame_pedidos)
data_janela.place(x=425, y=250)


cadastrar_pedido_bt = Button(frame_pedidos, text="Cadastrar pedido", font=('Helvetica', 13))
cadastrar_pedido_bt.place(x = 425, y = 290)






tela_inicial.config(menu=menubar)
tela_inicial.mainloop()
