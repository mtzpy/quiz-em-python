import tkinter as tk

janela=tk.Tk()
janela.title("teste de sabiencia")
janela.geometry("900x600")
pagina_inicial=tk.Frame(janela)
pagina_inicial.place(x=0,y=0,relwidth=1,relheight=1)

fundo=tk.PhotoImage(file="meme.png")
fundo=fundo.zoom(5)
label_fundo=tk.Label(pagina_inicial,image=fundo)
label_fundo.place(x=0,y=0,relwidth=1,relheight=1)

texto=tk.Label(pagina_inicial,text="Teste pra ver se você é sabido",font=('Arial',40,'bold'),pady=80)
texto.pack()

def clicar_botao():
    pagina_inicial.place_forget()
    quiz.place(x=0,y=0,relwidth=1,relheight=1)
botao=tk.Button(pagina_inicial,
            text="começar",
            font=('Arial',30),
            width=15,
            height=2,
            command=clicar_botao

)
botao.place(relx=0.5,rely=0.5,anchor="center")

quiz=tk.Frame(janela)
texto=tk.Label(quiz,text="responde as perguntas ai aurudo",font=('Comic Sans MS',30))
texto.pack()

pergunta=tk.Label(quiz,
                  text="Quem descobriu o Brasil?",
                  relief="solid",
                  borderwidth=1,
                  font=("Comic Sans MS",
                  30),
                  pady=80
)
pergunta.pack()

pontos=0
respostas=["Neymar","Capitão América","Pelé","Silvio Santos"]
resposta_certa=respostas[2]

botao_proxima=tk.Button(quiz,
                        text="próxima",
                        font=('Arial',20),
                        width=10,
                        height=2
)
botao_proxima.place_forget()

def verificar_acerto(escolhido):
    global pontos
    if escolhido==resposta_certa:
        mensagem['text']="acertou,farmou aura 67"
        pontos = pontos + 1
    else:
        mensagem['text']="errou ai beta"

    botao_proxima.place(relx=0.9,rely=0.9,anchor="center")

area_botoes=tk.Frame(quiz)
area_botoes.pack()
botao1=tk.Button(area_botoes,text=respostas[0],font=("Arial",20),width=15,height=2,command=lambda:verificar_acerto(respostas[0]))
botao1.grid(row=0,column=0,padx=50,pady=50)

botao2=tk.Button(area_botoes,text=respostas[1],font=("Arial",20),width=15,height=2,command=lambda:verificar_acerto(respostas[1]))
botao2.grid(row=0,column=1,padx=50,pady=50)

botao3=tk.Button(area_botoes,text=respostas[2],font=("Arial",20),width=15,height=2,command=lambda:verificar_acerto(respostas[2]))
botao3.grid(row=1,column=0,padx=50,pady=50)

botao4=tk.Button(area_botoes,text=respostas[3],font=("Arial",20),width=15,height=2,command=lambda:verificar_acerto(respostas[3]))
botao4.grid(row=1,column=1,padx=50,pady=50)


mensagem=tk.Label(quiz,text="",font=("Comic Sans MS",40,"bold"))
mensagem.pack()

respostas2=[4,22,5,67]
def proxima_pergunta2():
    global resposta_certa
    mensagem.config(text="")
    botao_proxima.place_forget()

    pergunta.config(text='quanto é 2+2?')
    botao1.config(text=respostas2[0],command=lambda:verificar_acerto(respostas2[0]))
    botao2.config(text=respostas2[1],command=lambda:verificar_acerto(respostas2[1]))
    botao3.config(text=respostas2[2],command=lambda:verificar_acerto(respostas2[2]))
    botao4.config(text=respostas2[3],command=lambda:verificar_acerto(respostas2[3]))

    resposta_certa=respostas2[1]

    botao_proxima.config(command=proxima_pergunta3)

botao_proxima.config(command=proxima_pergunta2)

respostas3=['itadori','saitama','reigen','naruto']
def proxima_pergunta3():
    global resposta_certa
    mensagem.config(text="")
    botao_proxima.place_forget()

    pergunta.config(text='qual desses exala mais aura?')
    botao1.config(text=respostas3[0], command=lambda: verificar_acerto(respostas3[0]))
    botao2.config(text=respostas3[1], command=lambda: verificar_acerto(respostas3[1]))
    botao3.config(text=respostas3[2], command=lambda: verificar_acerto(respostas3[2]))
    botao4.config(text=respostas3[3], command=lambda: verificar_acerto(respostas3[3]))

    resposta_certa = respostas3[2]

janela.mainloop()