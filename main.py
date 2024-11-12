import customtkinter
import pickle
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def criar_janela_vazia():
    nova_janela = customtkinter.CTk()
    nova_janela.geometry("500x300")
    nova_janela.withdraw()  # Iniciar a janela oculta
    return nova_janela

def esconder_janela_atual():
    janela.withdraw()  # Esconder a janela principal

def exibir_janela_vazia(nova_janela):
    nova_janela.deiconify()  # Exibir a nova janela

def login():
    email_value = email.get()
    senha_value = senha.get()

    if email_value == "matheus@gmail.com" and senha_value == "1234":
        print("Login efetuado com sucesso!")

        if checkbox.get():
            salvar_informacoes_usuario(email_value, senha_value)
        else:
            remover_informacoes_usuario()

        # Esconder a janela atual
        esconder_janela_atual()

        #configurar a nova janela antes de exibi-la
        configurar_nova_janela(nova_janela)

        # Exibir a nova janela vazia
        exibir_janela_vazia(nova_janela)

    else:
        print("Login e/ou senha inválido")

def salvar_informacoes_usuario(email, senha):
    informacoes_usuario = {"email": email, "senha": senha}
    with open("informacoes_usuario.pkl", "wb") as arquivo:
        pickle.dump(informacoes_usuario, arquivo)

def remover_informacoes_usuario():
    try:
        os.remove("informacoes_usuario.pkl")
    except FileNotFoundError:
        pass

def carregar_informacoes_usuario():
    try:
        with open("informacoes_usuario.pkl", "rb") as arquivo:
            informacoes_usuario = pickle.load(arquivo)
        return informacoes_usuario
    except FileNotFoundError:
        return None

def configurar_nova_janela(nova_janela):
    # Adicione a configuração da nova janela aqui, se necessário
    nova_janela.title("Bem-vindo ao Chat, Matheus!")

    global chat_box
    chat_box = customtkinter.CTkTextbox(nova_janela, width=400, height=250)
    chat_box.pack(pady=10)
    chat_box.configure(state="disabled")

    # entrada de mensagem e botão de envio
    global mensagem_entry
    mensagem_entry = customtkinter.CTkEntry(nova_janela, placeholder_text="Digite sua mensagem")
    mensagem_entry.pack(pady=5)

    enviar_botao = customtkinter.CTkButton(nova_janela, text="Enviar", command=enviar_mensagem)
    enviar_botao.pack(pady=5)


def enviar_mensagem():
    mensagem = mensagem_entry.get() # pega o texto digitado

    if mensagem.strip(): #verifica se a msg nao esta vazia
        # ativar caixa de texto para inserir a msg
        chat_box.configure(state="normal")
        chat_box.insert("end", f"Você: {mensagem}\n") # insere a mensagem na caixa de texto
        chat_box.configure(state="disabled") #desativa novamente
        chat_box.yview("end") # faz o scroll para a ultima mensagem

        mensagem_entry.delete(0,"end") # limpa o campo de entrada





janela = customtkinter.CTk()
janela.geometry("500x450")


email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

# Carregar as informações do usuário ao iniciar o programa
informacoes_salvas = carregar_informacoes_usuario()
if informacoes_salvas:
    email.insert(0, informacoes_salvas.get("email", ""))
    senha.insert(0, informacoes_salvas.get("senha", ""))

botao = customtkinter.CTkButton(janela, text="Login", command=login)
botao.pack(padx=10, pady=10)

# Criar a nova janela vazia e ocultá-la
nova_janela = criar_janela_vazia()

janela.mainloop()
