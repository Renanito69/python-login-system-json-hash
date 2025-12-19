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
                exit()

        except ValueError:
            print("\nERRO!!!")
            print("Coloque apenas numeros")
            pausa()

# Responsavel por cadastrar um usuario novo


def cadastrar_usuario():
    while True:
        limpar_tela()
        print("Cadastro de novo usuario\n")
        usuario_novo_usuario = input("Nome de Usuario: ").strip().lower()
        if not usuario_novo_usuario:
            print("O Campo Usuario não pode esta vazia")
            pausa()
            return

        # Responsavel por verificar se ja existe um usuario utilizando aquele nome
        if os.path.exists("Cadastros.txt"):
            with open("Cadastros.txt", 'r') as arquivo:
                for linha in arquivo:
                    if usuario_novo_usuario in linha.strip().split(';'):
                        print("Usuario ja existe")
                        pausa()
                        return

        senha_novo_usuario = str(input("Nova Senha: "))
        if not usuario_novo_usuario:
            print("O Campo Senha não pode esta vazia")
            pausa()
            return

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
                print("\nSenhas não parecidas")
                pausa()
                continue
        else:
            input("\nA senha precisa ter mais do que 4")
            continue


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
        usuario_entrar = str(input("Usuario: ").strip().lower())

        if not usuario_entrar:
            print("O Campo Usuario não pode esta vazia")
            pausa()
            return
        senha_entrar = str(input("Senha: "))

        if not senha_entrar:
            print("O Campo Senha não pode esta vazia")
            pausa()
            return

        with open("Cadastros.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) != 2:
                    continue
                usuario, senha = partes

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


def alterar_senha(usuario_logado):
    while True:
        limpar_tela()
        print(f"Alterar Senha do usuario {usuario_logado}\n") # Informa de qual usuario ira alterar a senha
        senha_atual = input("Senha Atual: ") # Pergunta a senha atual do usuario

        usuarios = list()
        senha_correta = False
        with open("Cadastros.txt", 'r') as arquivo: # abre o arquivo em modo leitura (read) e para cada linha do arquivo ele tira os espaços e separa por ";"
            for linha in arquivo:
                usuario, senha = linha.strip().split(";")
                # Depois separa por usuario e senha e compara se o "usuario_logado" e igual o "usuario" do arquivo e compara se a "senha" e igual a "senha_atual"
                if usuario == usuario_logado and senha == senha_atual:
                    # Se for verdade a "senha_correta" passa a ser True e pergunta qual sera a nova senha com "nova_senha"
                    senha_correta = True
                    nova_senha = input("Nova senha: ")
                    # Depois adiciona na lista "usuarios"
                    usuarios.append(f"{usuario};{nova_senha}" + '\n')

                else:
                    usuarios.append(linha)

        if not senha_correta: # Se a "senha_correta" for False retornara "Senha atual incorreta"
            print("Senha atual incorreta")
            pausa()
            continue

        with open("Cadastros.txt", 'w') as arquivo: # Agora ira abrir o arquivo como escrita (write) e ira adicionar a lista "usuarios" no arquivo
            arquivo.writelines(usuarios)

        print("Senha alterada com sucesso")
        return
# Menu principal


def deletar_conta(usuario_logado):  # Responsavel por deletar uma conta do arquivo
    while True:
        limpar_tela()
        print("Deletar conta!!!")
        remover_usuario = input(
            f'Deseja remover o usuario "{usuario_logado}" [S/N]: ').upper().strip()  # Deixa todas as letrar em maiuscula utilizando o .upper() e retira os espaços utilizando o .strip()
        if remover_usuario[0] == "S":  # Verifica se a primeira letra e "S"
            linha_temporario = list()  # Cria uma lista temporaria
            # Abre o arquivo em modo leitura(read) e verifica em cada linha do arquivo se o "usuarui_logado" esta la, se não estiver adiciona na "linha_temporario"
            with open("Cadastros.txt", 'r') as arquivo:
                for linha in arquivo:
                    if usuario_logado not in linha:
                        linha_temporario.append(linha)

            # Agora abre o arquivo em modo de escrita(write) e adiciona a "linha_temporario" em cada linha do arquivo removendo o usuario
            with open("Cadastros.txt", 'w') as arquivo:
                arquivo.writelines(linha_temporario)
            print(f"O Usuario {usuario_logado} Foi deletado com sucesso!!!")
            print("Desconectado")
            pausa()
            menu_entrada()  # Logo apos remover o usuario ele carrega a tela de loguin novamente

        # Se o "remover_usuario[0]" for igual a "N" ele cancela a operação e volta para o menu principal
        elif remover_usuario[0] == "N":
            print("Operação cancelada")
            print("Voltando para o menu principal")
            break

        else:  # Se for qualquer outra letra aparece um "print" pedindo para digitar "S" ou "N" e joga no inicio do loot denovo
            print('Digite "S" para sim e "N" para não')
            pausa()
            continue


def menu_principal(usuario_logado):  # ainda e o basico
    while True:
        limpar_tela()
        print(f"Bem-vindo ao sistema!")
        print(f"Usuario: {usuario_logado}")
        print("0 - Encerar sistema")
        print("1 - Listar usuarios")
        print("2 - Alterar senha")
        print("3 - Deletar minha conta")
        print("9 - Sair da conta")
        try:
            escolha = int(input("\nEscolha: "))
            if escolha == 1:
                pass
            if escolha == 2:
                alterar_senha(usuario_logado)
            if escolha == 3:
                deletar_conta(usuario_logado)
                pass
            if escolha == 0:
                print("Encerando do Sistema")
                exit()
            if escolha == 9:
                print("Desconectanto")
                pausa()
                break

            pausa()
        except ValueError:
            print("\nERRO!!!")
            print("Coloque apenas numeros")
            pausa()


# Programa inicial
menu_entrada()
