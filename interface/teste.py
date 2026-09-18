#teste com github
#arrocha
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
    quiz.pack()
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

def verificar_acerto(escolhido):
    global pontos
    if escolhido==resposta_certa:
        mensagem['text']="acertou,farmou aura 67"
        pontos = pontos + 1
    else:
        mensagem['text']="errou ai beta"

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


janela.mainloop()