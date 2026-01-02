from utils import limpar_tela, pausa
from auth import cadastrar_usuario, entrar_usuario, alterar_senha
from usuarios import listar_usuarios, deletar_conta
from colorama import Fore, Style, init
from time import sleep


init(autoreset=True)
def menu_entrada(): 
    """Menu inicial do sistema (Cadastro / Login / Sair)."""
    while True:
        limpar_tela()
        print(Style.BRIGHT + Fore.BLUE + "=== MENU PRINCIPAL ===\n")
        print(Fore.CYAN + "1 - Cadastro")
        print(Fore.CYAN + "2 - Entrar")
        print(Fore.CYAN + "0 - Sair")

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
                sleep(1)
                exit()

        except ValueError:
            print(Fore.RED + "\nERRO!!!")
            print(Fore.RED + "Coloque apenas numeros")
            pausa()


def menu_principal(usuario_logado):
    """Menu após login."""
    while True:
        limpar_tela()
        print(Style.BRIGHT + Fore.BLUE + "Bem-vindo ao sistema!")
        print(Style.BRIGHT + Fore.BLUE + f"Usuario: {usuario_logado}")
        print(Fore.CYAN + "0 - Encerrar sistema")
        print(Fore.CYAN + "1 - Listar Usuarios")
        print(Fore.CYAN + "2 - Alterar senha")
        print(Fore.CYAN + "3 - Deletar minha conta")
        print(Fore.CYAN + "9 - Sair da conta")

        try:
            escolha = int(input("\nEscolha: "))

            if escolha == 1:
                listar_usuarios()
            elif escolha == 2:
                alterar_senha(usuario_logado)
            elif escolha == 3:
                deletar_conta(usuario_logado)
            elif escolha == 0:
                print(Fore.RED + "Fechando sistema")
                sleep(1)
                exit()
            elif escolha == 9:
                print(Fore.RED + "Desconectando")
                sleep(0.5)
                break

        except ValueError:
            print(Fore.RED + "Digite apenas numeros")
            pausa()
