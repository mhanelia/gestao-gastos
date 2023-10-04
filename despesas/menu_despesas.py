from despesas.despesa import DespesasUsuario
from configuracoes.configuracoes import main_configuracoes
import sistema

menu = {
    '1': DespesasUsuario.criar,
    '2': DespesasUsuario.listar,
    '3': DespesasUsuario.atualizar,
    '4': DespesasUsuario.excluir,
    '5': main_configuracoes,
    '6': sistema.sair

}


def exibir_menu_despesas():

    print("Menu:")
    print("1. Criar despesa")
    print("2. Listar despesa")
    print("3. Atualizar despesa")
    print("4. Excluir despesa")
    print("5. Configurações")
    print("6. Sair")


def menu_despesas():
    while True:
        exibir_menu_despesas()
        escolha = input("Escolha uma opção: ")
        if escolha in menu:
            menu[escolha]()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
