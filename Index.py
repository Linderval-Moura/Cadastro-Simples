#Bibliotecas Importadas:
from tkinter import *
from tkinter.constants import END
import Banco
from tkinter import ttk
import os
from tkinter import messagebox

# Metodos da barra de menu 
pastaroot = os.path.dirname(__file__)

def semComando():
    print("")

def novaInstituicao():
    exec(open(pastaroot+"\\Doador_P.py").read())

def instituicoes():
    exec(open(pastaroot+"\\Doador_P.py").read())

def excluirInstituicao():
    exec(open(pastaroot+"\\Doador_P.py").read())

# \\\ Criação da Janela ///
janela = Tk() #Metodo para atribuir uma janela
janela.title("Cadastro & Login - Painel de Acesso") #Titulo da janela
janela.geometry("600x400") #Tamanho da janela
janela.configure(background="#dde") #Cor da janela
janela.resizable(width=False, height=False) #Não permite alterar tamanho ou maximizar...
janela.attributes("-alpha", 0.9) #Transparencia da janela

barraDeMenu = Menu(janela)
menuDoadores = Menu(barraDeMenu, tearoff=0)
menuDoadores.add_command(label="Nova",command=novaInstituicao)
menuDoadores.add_command(label="Cadastradas",command=instituicoes)
menuDoadores.add_command(label="Excluir Instituição",command=excluirInstituicao)
menuDoadores.add_separator()
#menuDoadores.add_command(label="Fechar",command=janela.quit)
barraDeMenu.add_cascade(label="Instituições", menu=menuDoadores)

menuManutencao = Menu(barraDeMenu, tearoff=0)
menuManutencao.add_command(label="Banco de Dados", command=semComando)
barraDeMenu.add_cascade(label="Manutenção", menu=menuManutencao)

menuSobre = Menu(barraDeMenu, tearoff=0)
menuSobre.add_command(label="Doar", command=semComando)
barraDeMenu.add_cascade(label="Sobre", menu=menuSobre)

janela.config(menu=barraDeMenu)

# \\\ Widgets ///
aesquerda = Frame(janela, width=221, height=400, bg="MIDNIGHTBLUE", relief="raise").pack(side=LEFT)

adireita = Frame(janela, width=370, height=400, bg="MIDNIGHTBLUE", relief="raise").pack(side=RIGHT)

menssagem = Label(janela, text="Cadastre sua Instituição \n caso já não o tenha jeito!", font=("Century Gothic",12), background="MIDNIGHTBLUE",foreground="white").place(x=250, y=160, width=350,height=50)

# O place determina manualmente o tamanho e altura

doadorLabel = Label(janela,text="Doador:", font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white").place(x=11, y=190, width=100,height=20)
doadorEntry = ttk.Entry(janela)
doadorEntry.place(x=90, y=190, width=100,height=20)

senhaLabel = Label(text="Senha:", font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white").place(x=16, y=220, width=100,height=20)
senhaEntry = ttk.Entry(janela)
senhaEntry.place(x=90, y=220, width=100,height=20)

def Login():
    nome = doadorEntry.get()
    senha = senhaEntry.get()

    Banco.dql("SELECT nome, senha FROM tb_doador")
    print("Selecionou")


# \\\ Botôes ///
entarButton = ttk.Button(janela,text="Entrar",width = 30, command = Login)
entarButton.place(x=30, y=250)

def Cadastro():
    # \\\ Esconde CadastroButton ///
    entarButton.place(x=5000)
    novocadastroButton.place(x=5000)
    
    # \\\ Inserindo Widgets de Cadastro ///
    nascimentoLabel = Label(janela,text="Nascimento:", font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    nascimentoLabel.place(x=0, y=10, width=100,height=20)

    nascimentoEntry = ttk.Entry(janela)
    nascimentoEntry.place(x=90, y=10, width=100,height=20)

    cpfLabel = Label(janela,text="CPF:", font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    cpfLabel.place(x=23, y=40, width=100,height=20)

    cpfEntry = ttk.Entry(janela)
    cpfEntry.place(x=90, y=40, width=100,height=20)

    emailLabel = Label(janela,text="E-mail:", font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    emailLabel.place(x=17, y=70, width=100,height=20)

    emailEntry = ttk.Entry(janela)
    emailEntry.place(x=90, y=70, width=100,height=20)

    telefoneLabel = Label(janela,text="Telefone:", font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    telefoneLabel.place(x=9, y=100, width=100,height=20)

    telefoneEntry = ttk.Entry(janela)
    telefoneEntry.place(x=90, y=100, width=100,height=20)

    cidadeLabel = Label(janela,text="Cidade:", font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    cidadeLabel.place(x=12, y=130, width=100,height=20)

    cidadeEntry = ttk.Entry(janela)
    cidadeEntry.place(x=90, y=130, width=100,height=20)

    estadoLabel = Label(janela,text="Estado:", font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    estadoLabel.place(x=14, y=160, width=100,height=20)

    estadoEntry = ttk.Entry(janela)
    estadoEntry.place(x=90, y=160, width=100,height=20)

    

    def gravarDados():
        if doadorEntry.get() != "":
            vnome = doadorEntry.get()
            vsenha = senhaEntry.get()
            vcpf = cpfEntry.get()
            vemail = emailEntry.get()
            vtelefone = telefoneEntry.get()
            vcidade = cidadeEntry.get()
            vestado = estadoEntry.get()
            vnascimento = nascimentoEntry.get()
            
            if (vnome=="" and vsenha=="" and vcpf=="" and vemail=="" and vtelefone=="" and vcidade=="" and vestado=="" and vnascimento==""):
                print (messagebox.showerror(title="Register Error", message="Preencha tudo!"))
            
            else:
                vquery = ("INSERT INTO tb_doador (nome, senha, cpf, email, telefone, cidade, estado, nascimento) VALUES ('"+vnome+"','"+vsenha+"','"+vcpf+"','"+vemail+"','"+vtelefone+"','"+vcidade+"','"+vestado+"','"+vnascimento+"')")
                Banco.dml(vquery)
                doadorEntry.delete(0, END)
                senhaEntry.delete(0, END)
                cpfEntry.delete(0, END)
                emailEntry.delete(0, END)
                telefoneEntry.delete(0, END)
                cidadeEntry.delete(0, END)
                estadoEntry.delete(0, END)
                nascimentoEntry.delete(0, END)
        
            print("Dados Gravados")
        else:
            print("ERRO")

    CadastroButton = ttk.Button(janela,text="Cadastrar",width = 30, command=gravarDados)
    CadastroButton.place(x=30, y=250)

    def voltarLogin():
        # \\\ Remove a parte do Cadastro
        nascimentoLabel.place(x=5000)
        nascimentoEntry.place(x=5000)
        cpfLabel.place(x=5000)
        cpfEntry.place(x=5000)
        emailLabel.place(x=5000)
        emailEntry.place(x=5000)
        telefoneLabel.place(x=5000)
        telefoneEntry.place(x=5000)
        cidadeLabel.place(x=5000)
        cidadeEntry.place(x=5000)
        estadoLabel.place(x=5000)
        estadoEntry.place(x=5000)

        CadastroButton.place(x=5000)
        VoltarButton.place(x=5000)

        # \\\ Voltando Widgets de Login ///
        entarButton.place(x=30, y=250)
        novocadastroButton.place(x=30, y=290)


    VoltarButton = ttk.Button(janela, text="Voltar",width = 30, command=voltarLogin)
    VoltarButton.place(x=30, y=290)

novocadastroButton = ttk.Button(janela,text="Novo Cadastro",width = 30, command=Cadastro)
novocadastroButton.place(x=30, y=290)


janela.mainloop() #Fim da criação da janela

