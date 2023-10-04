import sistema
from bd.criar_bd import CriarBanco
from despesas.despesa import DespesasUsuario
from usuarios.usuario import Usuarios
from usuarios.sessao import UsuarioLogado
from categorias.categoria import Categoria
from subcategorias.subcategoria import Subcategoria
from contas.conta import Conta
from contas.cartao import Cartao

criar_banco = CriarBanco()

categorias = Categoria()
subcategoria = Subcategoria()
conta = Conta()
cartao = Cartao()
despesas = DespesasUsuario()


def menu(titulo, opcoes):
    while True:
        print("=" * len(titulo), titulo, "=" * len(titulo), sep="\n")
        for i, (opcao, funcao) in enumerate(opcoes, 1):
            print("[{}] - {}".format(i, opcao))
        if "Sair" not in (opcao[0] for opcao in opcoes):
            print("[{}] - Voltar".format(i + 1))
        op = input("Opção: ")
        if op.isdigit():
            sistema.limpar_terminal()
            if int(op) == i + 1:
                # Encerra este menu e retorna a função anterior
                break
            if int(op) <= len(opcoes):
                # Chama a função do menu:
                opcoes[int(op) - 1][1]()
                continue
        print("Opção inválida. \n\n")


def principal():
    opcoes = [
        ("Criar despesa", despesas.criar),
        ("Listar despesa", despesas.listar),
        ("Atualizar despesa", despesas.atualizar),
        ("Excluir despesa", despesas.excluir),
        ("Listar IDs das despesas", despesas.listar_id_despesa),
        ("Configurações", configuracoes),
        ("Sair", sistema.sair)

    ]
    return menu("Menu principal", opcoes)


def configuracoes():
    opcoes = [
        ("Listar Categorias", categorias.ler),
        ("Listar Subcategorias", subcategoria.ler),
        ("Listar Contas", conta.ler),
        ("Listar Cartões", cartao.ler),
        ("Criar nova Categoria", categorias.criar),
        ("Criar nova Subcategoria despesa", subcategoria.criar),
        ("Adicionar nova Conta", conta.criar),
        ("Adicionar novo Cartão", cartao.criar),
        ("Excluir Categoria", categorias.excluir),
        ("Excluir Subcategoria", subcategoria.excluir),
        ("Excluir Conta", conta.excluir),
        ("Excluir Cartão", cartao.excluir)
    ]
    return menu("Configurações", opcoes)


def login():
    opcoes = {
        '1': Usuarios.logar,
        '2': Usuarios.cadastrar,
        '3': sistema.sair

    }

    print("Menu inicial:")
    print("1. Entrar:")
    print("2. Criar conta:")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha in opcoes:
        sistema.limpar_terminal()
        opcoes[escolha]()

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


def main():
    if UsuarioLogado().id is not None:
        principal()
    else:
        login()


while True:
    main()
