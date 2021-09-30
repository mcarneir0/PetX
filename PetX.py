#!/usr/bin/env python
# coding: utf-8

# In[127]:


from tkinter import *
from ttkbootstrap import Style
from PIL import ImageTk, Image


pagina_inicial = Tk()
pagina_inicial.title("PetX")
pagina_inicial.resizable(FALSE, FALSE)
pagina_inicial.iconbitmap("F:\Programação\Curso Programador de Sistemas\Projeto PetX\pet.ico")
pagina_inicial.geometry("1100x750+400+150")

style = Style('minty')
pagina_inicial = style.master



imagem = ImageTk.PhotoImage(Image.open("F:\Programação\Curso Programador de Sistemas\Projeto PetX\petx.png"))
imagemL = Label(image=imagem)
imagemL.place(x = 300, y = 45)


usuario = Label(pagina_inicial, width = 12, text = "Usuário")
usuario.place(x = "430", y = "525")
user_janela = Entry(pagina_inicial)
user_janela.place(x = "460", y = "550")

senha = Label(pagina_inicial, width = 12, text = "Senha")
senha.place(x = "430", y = "585")
senha_tela = Entry(pagina_inicial)
senha_tela.place(x = "460", y = "610")


botao_entrar = Button(pagina_inicial, text = "Entrar")
botao_entrar.place(x = "460" , y = "650")







pagina_inicial.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




