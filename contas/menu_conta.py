from contas.conta import Conta
from usuarios.sessao import UsuarioLogado
import sistema


usuario_logado = UsuarioLogado()


def exibir_menu():
    if Conta.verificar_existencia():
        print("Menu:")
        print("1. Criar contas:")
        print("2. Ver informações da contas:")
        print("3. Atualizar dados da contas:")
        print("4. Atualizar saldo da contas:")
        print("5. Excluir contas:")
        print("6. Sair")
    else:
        criar_conta()


def criar_conta():
    if not Conta.verificar_existencia():

        print("Você não possui nenhuma conta atrelada a sua conta")
        print("Vamos criar uma em poucos passos:")

        nome = sistema.input_obrigatorio("Digite um nome para a conta: ")
        banco = sistema.input_obrigatorio("Digite seu banco: ")
        categoria = sistema.input_obrigatorio(
            "Digite uma categoria para sua conta (exemplo: Conta corrente, poupança, investimentos, etc.): ")

        saldo = sistema.float_obrigatorio("Digite seu saldo inicial: ")

        conta_padrao = sistema.validar_conta_padrao()

        Conta.criar(nome, banco, categoria, saldo, conta_padrao)
        print("Conta criada com sucesso!")


def main_conta():
    while True:

        exibir_menu()
        escolha = input("Escolha uma opção: ")
        if Conta.verificar_existencia():
            if escolha in menu:
                menu[escolha]()
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")


menu = {
    '1': criar_conta,

}
