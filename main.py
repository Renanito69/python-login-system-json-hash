import os
import json
import hashlib

# ==============================
# FUNÇÕES AUXILIARES
# ==============================


def limpar_tela():
    """Limpa a tela do terminal (Windows)."""
    os.system("cls")


def pausa():
    """Pausa o programa até o usuário pressionar Enter."""
    input("pressione enter para continuar...")


# ==============================
# MENU DE ENTRADA
# ==============================

def menu_entrada():
    """Menu inicial do sistema (Cadastro / Login / Sair)."""
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
                # Se o login for bem-sucedido, entra no menu principal
                if sucesso:
                    menu_principal(usuario_logado=sucesso)
            elif escolha == 0:
                print("Saindo")
                exit()

        except ValueError:
            print("\nERRO!!!")
            print("Coloque apenas numeros")
            pausa()


# ==============================
# CADASTRO DE USUÁRIO
# ==============================

def cadastrar_usuario():
    """
    Cadastra um novo usuário no arquivo JSON.
    Estrutura do JSON:
    {
        "Usuarios cadastrados": [
            {"usuario": "...", "senha": "..."}
        ]
    }
    """
    login = dict()

    while True:
        limpar_tela()
        print("Cadastro de novo usuario\n")

        # Captura o nome do usuário
        login['usuario'] = input("Nome de Usuario: ").strip().lower()

        # Verifica se o campo está vazio
        if not login['usuario']:
            print("O Campo Usuario não pode esta vazia")
            pausa()
            return

        # Se o arquivo não existir, cria a estrutura inicial
        if not os.path.exists("Cadastros.json"):
            cadastrados = {'Usuarios cadastrados': []}
        else:
            # Caso exista, carrega os dados
            with open("Cadastros.json", 'r') as arquivo:
                cadastrados = json.load(arquivo)

            # Verifica se o usuário já existe
            for usuario in cadastrados['Usuarios cadastrados']:
                if login['usuario'] == usuario['usuario']:
                    print("Usuario ja existe")
                    pausa()
                    return

        # Captura a senha
        senha = input("Senha: ")

        # Verifica se a senha está vazia
        if not senha:
            print("O Campo Senha não pode esta vazia")
            pausa()
            return

        # Verifica tamanho mínimo da senha
        if len(senha) >= 4:
            confirmacao = input("Confirma Senha: ")

            # Confirma se as senhas são iguais
            if confirmacao == senha:
                hash_senha_confirmacao = hashlib.sha256(confirmacao.encode())
                login['senha'] = hash_senha_confirmacao.hexdigest()
                cadastrados["Usuarios cadastrados"].append(login)

                # Salva no arquivo JSON
                with open("Cadastros.json", "w") as arquivo:
                    json.dump(cadastrados, arquivo, indent=4)

                print("\nUsuario cadastrado com sucesso!")
                pausa()
                break
            else:
                print("\nSenhas não parecidas")
                pausa()
        else:
            print("\nA senha precisa ter mais do que 4")
            pausa()


# ==============================
# LOGIN DO USUÁRIO
# ==============================

def entrar_usuario():
    """Realiza o login do usuário verificando usuário e senha no JSON."""
    if not os.path.exists("Cadastros.json"):
        print("Arquivo não encontrado")
        pausa()
        return False

    tentativas = 3

    while tentativas > 0:
        limpar_tela()
        print("Entrar na conta")

        usuario_entrar = input("Usuario: ").strip().lower()
        senha_entrar = input("Senha: ")

        senha_hash = hashlib.sha256(senha_entrar.encode())
        verificar_senha_hash = senha_hash.hexdigest()
        with open("Cadastros.json", "r") as arquivo:
            cadastrados = json.load(arquivo)

            # Verifica cada usuário cadastrado
            for usuario in cadastrados['Usuarios cadastrados']:
                if usuario_entrar == usuario['usuario'] and verificar_senha_hash == usuario['senha']:
                    print("Login realizado com sucesso!")
                    pausa()
                    return usuario_entrar

        tentativas -= 1
        print("Usuario ou senha incorretos")
        input(f"Tentativas restantes: {tentativas}")

    input("Limite de tentativas atingido!")
    return False


# ==============================
# ALTERAR SENHA
# ==============================

def alterar_senha(usuario_logado):
    """Permite alterar a senha do usuário logado."""
    while True:
        limpar_tela()
        print(f"Alterar Senha do usuario {usuario_logado}\n")

        senha_atual = input("Senha Atual: ")
        hash_senha = hashlib.sha256(senha_atual.encode())
        verificar_hash_senha = hash_senha.hexdigest()
        with open("Cadastros.json", "r") as arquivo:
            cadastrados = json.load(arquivo)

        senha_correta = False

        # Procura o usuário logado
        for usuario in cadastrados['Usuarios cadastrados']:
            if usuario['usuario'] == usuario_logado and usuario['senha'] == verificar_hash_senha:
                senha_correta = True
                nova_senha = input("Nova senha: ")
                if len(nova_senha) >= 4:
                    confirma_nova_senha = input("Confirmar nova senha: ")
                    if confirma_nova_senha == nova_senha:
                        hash_senha = hashlib.sha256(nova_senha.encode())
                        usuario['senha'] = hash_senha.hexdigest()
                        break
                    else:
                        print("As senhas não sao iguais")
                        pausa()
                else:
                    print("Senha muito pequena")
                    pausa()
        if not senha_correta:
            print("Senha atual incorreta")
            pausa()
            continue

        # Salva a nova senha
        with open("Cadastros.json", "w") as arquivo:
            json.dump(cadastrados, arquivo, indent=4)

        print("Senha alterada com sucesso")
        pausa()
        return


# ==============================
# DELETAR CONTA
# ==============================

def deletar_conta(usuario_logado):
    """Remove definitivamente o usuário logado do sistema."""
    while True:
        limpar_tela()
        remover = input(
            f'Deseja remover o usuario "{usuario_logado}" [S/N]: ').upper().strip()

        if remover.startswith("S"):
            with open("Cadastros.json", "r") as arquivo:
                cadastrados = json.load(arquivo)

            # Remove o usuário da lista
            cadastrados['Usuarios cadastrados'] = [
                nome for nome in cadastrados['Usuarios cadastrados']
                if nome['usuario'] != usuario_logado
            ]

            with open("Cadastros.json", "w") as arquivo:
                json.dump(cadastrados, arquivo, indent=4)

            print("Conta removida com sucesso!")
            pausa()
            menu_entrada()

        elif remover.startswith("N"):
            print("Operação cancelada")
            pausa()
            break

        else:
            print('Digite "S" para sim ou "N" para não')
            pausa()

# ==============================
# LISTAR USUARIOS
# ==============================


def listar_usuarios():
    with open("Cadastros.json", 'r') as arquivo:
        cadastrados = json.load(arquivo)
        for posicao, usuario in enumerate(cadastrados["Usuarios cadastrados"]):
            print(f"{posicao+1} - {usuario['usuario']}")
        pausa()


# ==============================
# MENU PRINCIPAL
# ==============================

def menu_principal(usuario_logado):
    """Menu após login."""
    while True:
        limpar_tela()
        print("Bem-vindo ao sistema!")
        print(f"Usuario: {usuario_logado}")
        print("0 - Encerrar sistema")
        print("1 - Listar Usuarios")
        print("2 - Alterar senha")
        print("3 - Deletar minha conta")
        print("9 - Sair da conta")

        try:
            escolha = int(input("\nEscolha: "))

            if escolha == 1:
                listar_usuarios()
            elif escolha == 2:
                alterar_senha(usuario_logado)
            elif escolha == 3:
                deletar_conta(usuario_logado)
            elif escolha == 0:
                print("Fechando sistema")
                exit()
            elif escolha == 9:
                print("Desconectando")
                break

        except ValueError:
            print("Digite apenas numeros")
            pausa()


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

menu_entrada()
