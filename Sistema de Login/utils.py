import time
import os


def limpar_tela():
    """Limpa a tela do terminal (Windows)."""
    os.system("cls")


def pausa():
    """Pausa o programa até o usuário pressionar Enter."""
    input("pressione enter para continuar...")


def barra_progresso(texto):
    for i in range(0, 11):
        time.sleep(0.2)
        print(f" {texto}:", end='')
        print(f"[{'#' * i}{'.' * (10 - i)}] {i*10}%", flush=True, end='\r')
    print()


def logs(tipo_log, log):
    if not os.path.exists("Logs.txt"):
        with open("Logs.txt", 'w') as arquivo_log:
            arquivo_log.write("Logs Sistema:")

    with open("Logs.txt", 'a', encoding="utf-8") as arquivo_log:
        arquivo_log.write("\n" + f"{tipo_log} - {log}")
