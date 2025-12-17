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
                    menu_principal(usuario_logado=sucesso)
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
        usuario_novo_usuario = str(input("Nome de Usuario: "))

        
        # Responsavel por verificar se ja existe um usuario utilizando aquele nome
        if os.path.exists("Cadastros.txt"):
            with open("Cadastros.txt", 'r') as arquivo:
                for linha in arquivo:
                    if usuario_novo_usuario in linha.strip().split(';'):
                        print("Usuario ja existe")
                        pausa()
                        return

        senha_novo_usuario = str(input("Nova Senha: "))

        if len(senha_novo_usuario) >= 4:  # para verificar se a senha tem 4 ou mais caracter
            confirmacao_senha_usuario = str(input("Confirma Senha: "))

            if confirmacao_senha_usuario == senha_novo_usuario:  # para confirmar a senha
                # Responsavel por adicionar o (usuario;senha) no .txt
                with open("Cadastros.txt", "a") as arquivo:
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

                    return usuario_entrar

        tentativas -= 1
        print("Usuario ou senha incorretos")
        input(f"Login incorreto. Tentativas restantes: {tentativas}")

    input("Limite de tentativas atingido!")
    return False

# Menu principal


def menu_principal(usuario_logado):
    while True:
        limpar_tela()
        print(f"Bem-vindo ao sistema!")
        print(f"Usuario: {usuario_logado}")
        print("0 - Desconectar")
        print("1 - Listar usuarios")
        print("2 - Alterar senha")
        print("3 - Deletar minha conta")
        print("4 - Sair do sistema")
        escolha = int(input("\nEscolha: "))
        if escolha == 1:
            pass
        if escolha == 2:
            pass
        if escolha == 3:
            pass
        if escolha == 4:
            print("Encerando do Sistema")
            exit()
        if escolha == 0:
            print("Desconectanto")
            pausa()
            break

        pausa()


# Programa inicial

menu_entrada()
