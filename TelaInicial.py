#!/usr/bin/env python
# coding: utf-8

# In[66]:


from tkinter import *

janela = Tk()


usuario = Label(janela, width = 12, text = "Usuário")
usuario.place(x = "350", y = "380")
user_janela = Entry(janela)
user_janela.place(x = "375", y = "400")

senha = Label(janela, width = 12, text = "Senha")
senha.place(x = "350", y = "420")
senha_tela = Entry(janela)
senha_tela.place(x = "375", y = "440")


botao_entrar = Button(janela, text = "Entrar")
botao_entrar.place(x = "460" , y = "475")

botao_cadastrar = Button(janela, text = "Cadastre-se")
botao_cadastrar.place(x = "460" , y = "515")





janela.title("Tela Inicial")
janela.geometry("900x600+500+150")
janela.mainloop()


# In[ ]:





# In[ ]:




