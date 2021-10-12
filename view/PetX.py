#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from ttkbootstrap import Style
from PIL import ImageTk, Image
from tkinter import ttk

tela_inicial = Tk()
tela_inicial.title("PetX")
tela_inicial.resizable(FALSE, FALSE)
tela_inicial.iconbitmap("F:\Programação\Curso Programador de Sistemas\Projeto PetX\pet.ico")
tela_inicial.geometry("1100x750+800+50")

style = Style('minty')
tela_inicial = style.master

imagem = ImageTk.PhotoImage(Image.open("F:\Programação\Curso Programador de Sistemas\Projeto PetX\petx.png"))
imagemL = Label(image=imagem)
imagemL.place(x = 300, y = 50)


#metodos

def esconde_frame():
    frame_login.pack_forget()
    frame_cadastrar.pack_forget()
    produtos_frame.pack_forget()
    frame_animais.pack_forget()


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
    

# menus

menubar = Menu(tela_inicial)
Login = Menu(menubar, tearoff = 0)
Login.add_command(label="Login", command=frame_login)
Login.add_command(label="Cadastre-se", command=frame_cadastrar)
Login.add_separator()
Login.add_command(label="Sair")

menubar.add_cascade(label="Login", menu=Login)



Produtos = Menu(menubar, tearoff = 0)
Produtos.add_command(label="Produtos", command=frame_produtos)
menubar.add_cascade(label="Produtos", menu=Produtos)

Animais = Menu(menubar, tearoff = 0)
Animais.add_command(label="Animais", command=frame_animais)
Animais.add_command(label="Adoção")
Animais.add_command(label="Compra")
menubar.add_cascade(label="Animais", menu=Animais)





#frames

# frame login

frame_login = Frame(tela_inicial, width = 1100, height = 750)
usuario = Label(frame_login, width = 12, text = "Usuário")
usuario.place(x = "430", y = "525")
user_janela = Entry(frame_login)
user_janela.place(x = "460", y = "550")

senha = Label(frame_login, width = 12, text = "Senha")
senha.place(x = "430", y = "585")
senha_tela = Entry(frame_login)
senha_tela.place(x = "460", y = "610")

botao_entrar = Button(frame_login, text = "Entrar")
botao_entrar.place(x = "460" , y = "650")

imagem = ImageTk.PhotoImage(Image.open("F:\Programação\Curso Programador de Sistemas\Projeto PetX\petx.png"))
imagemL = Label(image=imagem)
imagemL.place(x = 300, y = 50)



# frame cadastrar

frame_cadastrar = Frame(tela_inicial, width = 1100, height = 750)

titulo = ttk.Label(frame_cadastrar, text = "Cadastre-se", 
                   style="primary.Inverse.TLabel",
                   padding=(50,30,50,30),
                   font=('Helvetica', 30))
titulo.place(x = 400, y= 40)

nome_lb = Label(frame_cadastrar, text="NOME",font=('Helvetica', 13) )
nome_lb.place(x = 315, y=160)
nome_janela = Entry(frame_cadastrar)
nome_janela.place(x = 315, y=190)

sobrenome_lb = Label(frame_cadastrar, text="SOBRENOME",font=('Helvetica', 13) )
sobrenome_lb.place(x = 315, y=225)
sobrenome_janela = Entry(frame_cadastrar)
sobrenome_janela.place(x = 315, y=255)

cpf_lb = Label(frame_cadastrar, text="CPF",font=('Helvetica', 13) )
cpf_lb.place(x = 315, y=280)
cpf_janela = Entry(frame_cadastrar)
cpf_janela.place(x = 315, y=310)

email_lb = Label(frame_cadastrar, text="EMAIL",font=('Helvetica', 13) )
email_lb.place(x = 315, y=335)
email_janela = Entry(frame_cadastrar)
email_janela.place(x = 315, y=365)

senha_lb = Label(frame_cadastrar, text="SENHA",font=('Helvetica', 13) )
senha_lb.place(x = 315, y=395)
senha_janela = Entry(frame_cadastrar)
senha_janela.place(x = 315, y=425)

cadastrar_bt = Button(frame_cadastrar, text="Cadastrar", font=('Helvetica', 13))
cadastrar_bt.place(x = 315, y=480)


# frame produtos

produtos_frame = Frame(tela_inicial, width = 1100, height = 750)
titulo_produtos = ttk.Label(produtos_frame, text = "Produtos", 
                   style="primary.Inverse.TLabel",
                   padding=(50,30,50,30),
                   font=('Helvetica', 30))
titulo_produtos.place(x = 400, y= 40)

nome_produto_lb = Label(produtos_frame, text="NOME DO PRODUTO",font=('Helvetica', 13) )
nome_produto_lb.place(x = 315, y=160)
nome_produto_janela = Entry(produtos_frame)
nome_produto_janela.place(x = 315, y=190)

descricao_lb = Label(produtos_frame, text="DESCRIÇÃO",font=('Helvetica', 13) )
descricao_lb.place(x = 315, y=225)
descricao_lb_janela = Entry(produtos_frame)
descricao_lb_janela.place(x = 315, y=255)

preco_lb = Label(produtos_frame, text="PREÇO",font=('Helvetica', 13) )
preco_lb.place(x = 315, y=280)
preco_lb_janela = Entry(produtos_frame)
preco_lb_janela.place(x = 315, y=310)

carrinho_bt = Button(produtos_frame, text="Adicionar ao carrinho", font=('Helvetica', 13))
carrinho_bt.place(x = 315, y=360)



# frame animais

frame_animais = Frame(tela_inicial, width = 1100, height = 750)
titulo_animais = ttk.Label(frame_animais, text = "Animais", 
                   style="primary.Inverse.TLabel",padding=(50,30,50,30),
                   font=('Helvetica', 30))
titulo_animais.place(x = 400, y= 40)

tipo_animais_lb = Label(frame_animais, text="TIPO DO ANIMAL",font=('Helvetica', 13) )
tipo_animais_lb.place(x = 315, y=160)
tipo_animais_janela = Entry(frame_animais)
tipo_animais_janela.place(x = 315, y=190)

nome_animais_lb = Label(frame_animais, text="NOME DO ANIMAL",font=('Helvetica', 13) )
nome_animais_lb.place(x = 315, y=225)
nome_animais_janela = Entry(frame_animais)
nome_animais_janela.place(x = 315, y=255)

raca_animais_lb = Label(frame_animais, text="RAÇA DO ANIMAL",font=('Helvetica', 13) )
raca_animais_lb.place(x = 315, y=280)
raca_animais_janela = Entry(frame_animais)
raca_animais_janela.place(x = 315, y=310)

tamanho_animais_lb = Label(frame_animais, text="TAMANHO DO ANIMAL",font=('Helvetica', 13) )
tamanho_animais_lb.place(x = 315, y=335)
tamanho_animais_janela = Entry(frame_animais)
tamanho_animais_janela.place(x = 315, y=365)

preco_animais_lb = Label(frame_animais, text="PREÇO DO ANIMAL",font=('Helvetica', 13) )
preco_animais_lb.place(x = 315, y=395)
preco_animais_janela = Entry(frame_animais)
preco_animais_janela.place(x = 315, y=425)

adocao_bt = Button(frame_animais, text="Adoção",font=('Helvetica', 13) )
adocao_bt.place(x = 315, y = 470)

compra_bt = Button(frame_animais, text="Compra",font=('Helvetica', 13) )
compra_bt.place(x = 395, y = 470)




tela_inicial.config(menu=menubar)
tela_inicial.mainloop()


# ### Conexão com o banco de dados

# In[ ]:




