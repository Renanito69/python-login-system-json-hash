from utils import limpar_tela, pausa, barra_progresso, logs
import json
import os
import hashlib
from pwinput import pwinput
from colorama import Fore, init, Style

init(autoreset=True)


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
        print(Style.BRIGHT + Fore.BLUE + "Cadastro de novo usuario\n")

        # Captura o nome do usuário
        login['usuario'] = input("Nome de Usuario: ").strip().lower()

        # Verifica se o campo está vazio
        if not login['usuario']:
            print(Fore.RED + "O Campo Usuario não pode esta vazia")
            pausa()
            return

        # Se o arquivo não existir, cria a estrutura inicial
        if not os.path.exists("Cadastros.json"):
            cadastrados = {'Usuarios cadastrados': []}
        else:
            # Caso exista, carrega os dados
            with open("Cadastros.json", 'r', encoding='utf-8') as arquivo:
                cadastrados = json.load(arquivo)

            # Verifica se o usuário já existe
            for usuario in cadastrados['Usuarios cadastrados']:
                if login['usuario'] == usuario['usuario']:
                    print(Fore.RED + "Usuario ja existe")
                    pausa()
                    return

        # Captura a senha
        senha = pwinput("Senha: ")

        # Verifica se a senha está vazia
        if not senha:
            print( Fore.RED + "O Campo Senha não pode esta vazia")
            pausa()
            return

        # Verifica tamanho mínimo da senha
        if len(senha) >= 4:
            confirmacao = pwinput("Confirma Senha: ")

            # Confirma se as senhas são iguais
            if confirmacao == senha:
                hash_senha_confirmacao = hashlib.sha256(confirmacao.encode())
                login['senha'] = hash_senha_confirmacao.hexdigest()
                cadastrados["Usuarios cadastrados"].append(login)

                # Salva no arquivo JSON
                barra_progresso("Cadastrando usuario")
                with open("Cadastros.json", "w", encoding='utf-8') as arquivo:
                    json.dump(cadastrados, arquivo, indent=4)

                print(Fore.GREEN + "\nUsuario cadastrado com sucesso!")
                logs("Cadastro usuario", login['usuario'])
                pausa()
                break
            else:
                print(Fore.RED + "\nSenhas não parecidas")
                pausa()
        else:
            print(Fore.RED + "\nA senha precisa ter mais do que 4")
            pausa()


def entrar_usuario():
    """Realiza o login do usuário verificando usuário e senha no JSON."""
    if not os.path.exists("Cadastros.json"):
        print("Arquivo não encontrado")
        pausa()
        return False

    tentativas = 3

    while tentativas > 0:
        limpar_tela()
        print(Style.BRIGHT  + Fore.BLUE + "Entrar na conta")

        usuario_entrar = input("Usuario: ").strip().lower()
        senha_entrar = pwinput("Senha: ")

        senha_hash = hashlib.sha256(senha_entrar.encode())
        verificar_senha_hash = senha_hash.hexdigest()
        with open("Cadastros.json", "r", encoding='utf-8') as arquivo:
            cadastrados = json.load(arquivo)

            # Verifica cada usuário cadastrado
            for usuario in cadastrados['Usuarios cadastrados']:
                if usuario_entrar == usuario['usuario'] and verificar_senha_hash == usuario['senha']:
                    barra_progresso("Entrando na conta")
                    print(Fore.GREEN + "Login realizado com sucesso!")
                    logs("Login Usuario", usuario_entrar)
                    pausa()
                    return usuario_entrar

        tentativas -= 1
        print(Fore.RED + "Usuario ou senha incorretos")
        input( Fore.RED + f"Tentativas restantes: {tentativas}")

    input(Fore.RED + "Limite de tentativas atingido!")
    return False


def alterar_senha(usuario_logado):
    """Permite alterar a senha do usuário logado."""
    while True:
        limpar_tela()
        print(Style.BRIGHT + Fore.BLUE + f"Alterar Senha do usuario {usuario_logado}\n")

        senha_atual = pwinput("Senha Atual: ")
        hash_senha = hashlib.sha256(senha_atual.encode())
        verificar_hash_senha = hash_senha.hexdigest()
        with open("Cadastros.json", "r", encoding='utf-8') as arquivo:
            cadastrados = json.load(arquivo)

        senha_correta = False

        # Procura o usuário logado
        for usuario in cadastrados['Usuarios cadastrados']:
            if usuario['usuario'] == usuario_logado and usuario['senha'] == verificar_hash_senha:
                senha_correta = True
                nova_senha = pwinput("Nova senha: ")
                if len(nova_senha) >= 4:
                    confirma_nova_senha = pwinput("Confirmar nova senha: ")
                    if confirma_nova_senha == nova_senha:
                        hash_senha = hashlib.sha256(nova_senha.encode())
                        usuario['senha'] = hash_senha.hexdigest()
                        break
                    else:
                        print(Fore.RED + "As senhas não sao iguais")
                        pausa()
                else:
                    print(Fore.RED + "Senha muito pequena")
                    pausa()
        if not senha_correta:
            print(Fore.RED + "Senha atual incorreta")
            pausa()
            continue

        # Salva a nova senha
        with open("Cadastros.json", "w", encoding='utf-8') as arquivo:
            json.dump(cadastrados, arquivo, indent=4)

        barra_progresso("Alterando senha")
        print(Fore.GREEN + "Senha alterada com sucesso")
        logs("Alteração de senha", usuario_logado)
        pausa()
        return
