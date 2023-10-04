from categorias.categoria import Categoria
from subcategorias.subcategoria import Subcategoria

categorias = Categoria()
subcategoria = Subcategoria()

menu = {
    '1': categorias.ler,
    '2': subcategoria.ler,
    '3': categorias.criar,
    '7': categorias.excluir

}


def exibir_menu_despesas():

    print("Configurações:")
    print("1. Listar Categorias")
    print("2. Listar Subcategorias")
    print("3. Criar nova Categoria")
    print("4. Criar nova Subcategoria despesa")
    print("5. Adicionar nova Conta")
    print("6. Adicionar novo Cartão")
    print("7. Excluir Categoria")
    print("8. Excluir Subcategoria")
    print("9. Excluir Conta")
    print("10. Excluir Cartão")


def main_configuracoes():
    while True:
        exibir_menu_despesas()
        escolha = input("Escolha uma opção: ")
        if escolha in menu:
            menu[escolha]()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


