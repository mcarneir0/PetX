#!/usr/bin/env python
# coding: utf-8

# ## Tela Inicial

# In[29]:


from tkinter import *
from ttkbootstrap import Style
from PIL import ImageTk, Image
import ttkbootstrap
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
    frame_adocao.pack_forget()
    frame_compra.pack_forget()
    frame_carrinho.pack_forget()
    
    
    
def cadastro_sucesso():
    esconde_frame()
    frame_login.pack(fill="both", expand=1)
    
def entrar():
    esconde_frame()
    tela_inicial.pack(fill="both", expand=1)

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
    
    
bt_produtos = Button(tela_inicial, text="PRODUTOS", font=('Helvetica', 18), command=frame_produtos)
bt_produtos.place(x = 200, y = 600)

bt_animais = Button(tela_inicial, text="ANIMAIS", font=('Helvetica', 18), command=frame_animais)
bt_animais.place(x = 400, y = 600)

bt_carrinho = Button(tela_inicial, text="CARRINHO DE COMPRAS", font=('Helvetica', 9), command=frame_carrinho)
bt_carrinho.place(x = 900, y = 50)



    

# menus

menubar = Menu(tela_inicial)
Login = Menu(menubar, tearoff = 0)
Login.add_command(label="Login", command=frame_login)
Login.add_command(label="Cadastre-se", command=frame_cadastrar)
Login.add_separator()
menubar.add_cascade(label="Login", menu=Login)



Produtos = Menu(menubar, tearoff = 0)
Produtos.add_command(label="Produtos", command=frame_produtos)
menubar.add_cascade(label="Produtos", menu=Produtos)



Animais = Menu(menubar, tearoff = 0)
Animais.add_command(label="Animais", command=frame_animais)
Animais.add_command(label="Adoção", command=frame_adocao)
Animais.add_command(label="Compra", command=frame_compra)
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

botao_entrar = Button(frame_login, text = "Entrar", command=entrar)
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

cod_user_lb = Label(frame_cadastrar, text="COD USUÁRIO",font=('Helvetica', 13) )
cod_user_lb.place(x = 425, y=200)
cod_user_janela = Entry(frame_cadastrar)
cod_user_janela.place(x = 425, y=225)

nome_lb = Label(frame_cadastrar, text="NOME",font=('Helvetica', 13) )
nome_lb.place(x = 425, y=250)
nome_janela = Entry(frame_cadastrar)
nome_janela.place(x = 425, y=275)

sobrenome_lb = Label(frame_cadastrar, text="SOBRENOME",font=('Helvetica', 13) )
sobrenome_lb.place(x = 425, y=300)
sobrenome_janela = Entry(frame_cadastrar)
sobrenome_janela.place(x = 425, y=325)

cpf_lb = Label(frame_cadastrar, text="CPF",font=('Helvetica', 13) )
cpf_lb.place(x = 425, y=350)
cpf_janela = Entry(frame_cadastrar)
cpf_janela.place(x = 425, y=375)

email_lb = Label(frame_cadastrar, text="EMAIL",font=('Helvetica', 13) )
email_lb.place(x = 425, y=400)
email_janela = Entry(frame_cadastrar)
email_janela.place(x = 425, y=425)

senha_lb = Label(frame_cadastrar, text="SENHA",font=('Helvetica', 13) )
senha_lb.place(x = 425, y=450)
senha_janela = Entry(frame_cadastrar)
senha_janela.place(x = 425, y=475)

cadastrar_bt = Button(frame_cadastrar, text="Cadastrar", font=('Helvetica', 13), command=cadastro_sucesso)
cadastrar_bt.place(x = 425, y=515)


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

carrinho_bt = Button(produtos_frame, text="Adicionar ao carrinho", font=('Helvetica', 13), command=frame_carrinho)
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

adocao_bt = Button(frame_animais, text="Adoção",font=('Helvetica', 13), command=frame_adocao )
adocao_bt.place(x = 315, y = 470)

compra_bt = Button(frame_animais, text="Compra",font=('Helvetica', 13), command=frame_compra )
compra_bt.place(x = 395, y = 470)




# frame adoção

frame_adocao = Frame(tela_inicial, width = 1100, height = 750)
titulo_adocao = ttk.Label(frame_adocao, text = "Adoção", 
                   style="primary.Inverse.TLabel",padding=(50,30,50,30),
                   font=('Helvetica', 30))
titulo_adocao.place(x = 400, y= 40)

cod_adocao_lb = Label(frame_adocao, text="COD ADOÇÃO",font=('Helvetica', 13) )
cod_adocao_lb.place(x = 315, y=160)
cod_adocao_janela = Entry(frame_adocao)
cod_adocao_janela.place(x = 315, y=190)

cod_user_lb = Label(frame_adocao, text="COD USUÁRIO",font=('Helvetica', 13) )
cod_user_lb.place(x = 315, y=225)
cod_user_janela = Entry(frame_adocao)
cod_user_janela.place(x = 315, y=255)

cod_animal_lb = Label(frame_adocao, text="COD ANIMAL",font=('Helvetica', 13) )
cod_animal_lb.place(x = 315, y=280)
cod_animal_janela = Entry(frame_adocao)
cod_animal_janela.place(x = 315, y=310)

data_lb = Label(frame_adocao, text="DATA",font=('Helvetica', 13) )
data_lb.place(x = 315, y=335)
data_janela = Entry(frame_adocao)
data_janela.place(x = 315, y=365)

preco_lb = Label(frame_adocao, text="PREÇO",font=('Helvetica', 13) )
preco_lb.place(x = 315, y=395)
preco_janela = Entry(frame_adocao)
preco_janela.place(x = 315, y=425)



# frame compra 

frame_compra = Frame(tela_inicial, width = 1100, height = 750)
titulo_compra = ttk.Label(frame_compra, text = "Compra", 
                   style="primary.Inverse.TLabel",padding=(50,30,50,30),
                   font=('Helvetica', 30))
titulo_compra.place(x = 400, y= 40)

cod_compra_lb = Label(frame_compra, text="COD ADOÇÃO",font=('Helvetica', 13) )
cod_compra_lb.place(x = 315, y=160)
cod_compra_janela = Entry(frame_compra)
cod_compra_janela.place(x = 315, y=190)

cod_user_lb = Label(frame_compra, text="COD USUÁRIO",font=('Helvetica', 13) )
cod_user_lb.place(x = 315, y=225)
cod_user_janela = Entry(frame_compra)
cod_user_janela.place(x = 315, y=255)

cod_animal_lb = Label(frame_compra, text="COD ANIMAL",font=('Helvetica', 13) )
cod_animal_lb.place(x = 315, y=280)
cod_animal_janela = Entry(frame_compra)
cod_animal_janela.place(x = 315, y=310)

data_lb = Label(frame_compra, text="DATA",font=('Helvetica', 13) )
data_lb.place(x = 315, y=335)
data_janela = Entry(frame_compra)
data_janela.place(x = 315, y=365)

preco_lb = Label(frame_compra, text="PREÇO",font=('Helvetica', 13) )
preco_lb.place(x = 315, y=395)
preco_janela = Entry(frame_compra)
preco_janela.place(x = 315, y=425)


# frame carrinho de compras

frame_carrinho = Frame(tela_inicial, width = 1100, height = 750)
titulo_carrinho = ttk.Label(frame_carrinho, text = "Carrinho de compras", 
                   style="primary.Inverse.TLabel",padding=(50,30,50,30),
                   font=('Helvetica', 30))
titulo_carrinho.place(x = 340, y= 40)

cod_pedido_lb = Label(frame_carrinho, text="COD PEDIDO",font=('Helvetica', 13) )
cod_pedido_lb.place(x = 425, y=160)
cod_pedido_janela = Entry(frame_carrinho)
cod_pedido_janela.place(x = 425, y=190)

cod_produto_lb = Label(frame_carrinho, text="COD PRODUTO",font=('Helvetica', 13) )
cod_produto_lb.place(x = 425, y=220)
cod_produto_janela = Entry(frame_carrinho)
cod_produto_janela.place(x = 425, y=250)





tela_inicial.config(menu=menubar)
tela_inicial.mainloop()


# ### Conexão com o banco de dados

# In[ ]:




