import os
import platform
import subprocess


def limpar_terminal():
    sistema_operacional = platform.system()

    if sistema_operacional == "Windows":
        subprocess.check_call('cls', shell=True)
    else:
        os.system("clear")


def input_obrigatorio(mensagem):
    while True:
        entrada = input(mensagem)
        if not entrada:
            print("Campo obrigatório, digite novamente")
        else:
            return entrada


def float_obrigatorio(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            break
        except ValueError:
            print("Saldo precisa ser numérico. Digite novamente")
    return valor


def validar_conta_padrao():
    while True:
        conta_padrao = input("É sua conta padrão? [S/N]: ").upper()
        if conta_padrao in ["S", "N"]:
            break
        else:
            print("Resposta inválida. Digite S ou N")
    return conta_padrao


def sair():
    print("Saindo do programa.")
    quit()