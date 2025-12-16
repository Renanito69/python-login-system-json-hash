import os


def limpar_tela():
    os.system("cls")


def pausa():
    input("precione enter para continuar...")


# Menu de entrada


def menu_entrada():
    while True:
        limpar_tela()
        print("1 - Cadastro")
        print("2 - Entrar")
        print("0 - Sair")

        try:
            escolha = int(input("\nEscolha: "))

            if escolha == 1:
                cadastrar_usuario()
            elif escolha == 2:
                sucesso = entrar_usuario()
                if sucesso:
                    menu_principal()
            elif escolha == 0:
                print("Saindo")
                break

        except ValueError:
            print("\nERRO!!!")
            print("Coloque apenas numeros")
            pausa()

# Responsavel por cadastrar um usuario novo


def cadastrar_usuario():
    while True:
        limpar_tela()
        print("Cadastro de novo usuario\n")
        with open("Cadastros.txt", "a") as arquivo:
            usuario_novo_usuario = str(input("Nome de Usuario: "))
            senha_novo_usuario = str(input("Nova Senha: "))

            if len(senha_novo_usuario) >= 4:  # para verificar se a senha tem 4 ou mais caracter
                confirmacao_senha_usuario = str(input("Confirma Senha: "))

                if confirmacao_senha_usuario == senha_novo_usuario:  # para confirmar a senha
                    arquivo.write(
                        f"{usuario_novo_usuario};{senha_novo_usuario}" + '\n')
                    print("\nUsuario cadastrado com sucesso!")
                    pausa()
                    break
                else:
                    input("\nSenhas não parecidas")
            else:
                input("\nA senha precisa ter mais do que 4")


# Responsavel por realizar o login do usuario
def entrar_usuario():
    # verifica se o arquivo ("Cadastros.txt") existe
    if not os.path.exists("Cadastros.txt"):
        print("Arquivo não encontrado")
        pausa()
        return False

    tentativas = 3

    while tentativas > 0:
        limpar_tela()
        print("Entrar na conta")
        usuario_entrar = str(input("Usuario: "))
        senha_entrar = str(input("Senha: "))

        with open("Cadastros.txt", "r") as arquivo:
            for linha in arquivo:
                usuario, senha = linha.strip().split(";")

                # verificar se usuario e senha são igual do cadastro
                if usuario_entrar == usuario and senha_entrar == senha:
                    print("Login realizado com sucesso!")
                    pausa()

                    return True

        tentativas -= 1
        print("Usuario ou senha incorretos")
        input(f"Login incorreto. Tentativas restantes: {tentativas}")

    input("Limite de tentativas atingido!")
    return False

# Menu principal


def menu_principal():
    limpar_tela()
    print("Bem-vindo ao sistema!")
    print("0 - Desconectar")
    print("1 - Listar usuarios")
    print("2 - Alterar senha")
    print("3 - Deletar minha conta")
    print("4 - Sair")
    pausa()


# Programa inicial

menu_entrada()
