from utils import limpar_tela, pausa, barra_progresso, logs
import json
import hashlib
from colorama import Style, Fore


def deletar_conta(usuario_logado):
    """Remove definitivamente o usuário logado do sistema."""
    from menu import menu_entrada
    while True:
        limpar_tela()
        remover = input(
            Style.BRIGHT + Fore.BLUE + f'Deseja remover o usuario "{usuario_logado}" [S/N]: ').upper().strip()

        if remover.startswith("S"):
            with open("Cadastros.json", "r", encoding='utf-8') as arquivo:
                cadastrados = json.load(arquivo)

            # Remove o usuário da lista
            cadastrados['Usuarios cadastrados'] = [
                nome for nome in cadastrados['Usuarios cadastrados']
                if nome['usuario'] != usuario_logado
            ]

            with open("Cadastros.json", "w", encoding="utf-8") as arquivo:
                json.dump(cadastrados, arquivo, indent=4)
            barra_progresso("Deletando conta")
            print(Fore.GREEN + "Conta removida com sucesso!")
            logs("Deletando conta", usuario_logado)
            pausa()
            menu_entrada()

        elif remover.startswith("N"):
            print(Fore.RED + "Operação cancelada")
            pausa()
            break

        else:
            print(Fore.RED + 'Digite "S" para sim ou "N" para não')
            pausa()


def listar_usuarios():
    limpar_tela()
    print(Style.BRIGHT + Fore.BLUE + "Listar Usuarios")
    with open("Cadastros.json", 'r', encoding='utf-8') as arquivo:
        cadastrados = json.load(arquivo)
        for posicao, usuario in enumerate(cadastrados["Usuarios cadastrados"]):
            print(f"{posicao+1} - {usuario['usuario']}")
        pausa()
