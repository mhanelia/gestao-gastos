import sistema
from usuarios.usuario import Usuarios
from sistema import sair


menu = {
    '1': Usuarios.logar,
    '2': Usuarios.cadastrar,
    '3': sair

}


def exibir_menu():
    sistema.limpar_terminal()
    print("Menu:")
    print("1. Entrar:")
    print("2. Criar contas:")
    print("3. Voltar")


def main_usuario():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha in menu:
            menu[escolha]()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
