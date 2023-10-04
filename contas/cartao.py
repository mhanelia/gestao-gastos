from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd
from bd.bd_cartao import CartaoUsuario
import sistema
from tabulate import tabulate

usuario_logado = UsuarioLogado()
cartao = CartaoUsuario()
bd, cursor, error_bd = conectar_bd()


class Cartao:

    @staticmethod
    def criar():
        id_conta = sistema.input_obrigatorio("ID da conta: ")
        nome = sistema.input_obrigatorio("Nome do cartão: ")
        limite = sistema.float_obrigatorio("Limite do cartão: ")
        bandeira = sistema.input_obrigatorio("Bandeira do cartão: ")
        cartao_padrao = sistema.input_obrigatorio("Cartão padrão: ")
        ultimos_digitos = input("Últimos dígitos do cartão: ")
        ativo = sistema.input_obrigatorio("Ativo: ")
        vencimento_fatura = sistema.input_obrigatorio("Vencimento da fatura: ")
        fechamento_fatura = sistema.input_obrigatorio("Fechamento da fatura: ")

        cartao.criar(id_conta, nome, limite, bandeira, cartao_padrao, ultimos_digitos, ativo, vencimento_fatura,
                     fechamento_fatura)

    @staticmethod
    def ler():
        dados = cartao.ler()
        cabecalho = ["ID", "Conta vínculada", "Nome", "Limite", "Bandeira", "Cartão padrão", "Ultimos dígitos",
                     "Ativa", "Vencimento da fatura", "Fechamento da fatura"]

        print(tabulate(dados, headers=cabecalho, tablefmt="grid"))

        # @staticmethod

    # def atualizar(nome, banco, categoria, saldo, conta_padrao):
    #     atualizar_conta = f"UPDATE contas SET nome = '{nome}', banco = '{banco}', categoria = '{categoria}', saldo = {saldo}, conta_padrao = {conta_padrao} WHERE id_usuario = {usuario_logado.id}"
    #     cursor.execute(atualizar_conta)
    #     bd.commit()
    #     print("Conta atualizada com sucesso")

    def excluir(self):
        self.ler()
        id_cartao = sistema.input_obrigatorio("ID do cartão a ser excluído: ")
        cartao.excluir(id_cartao)
        print("Conta excluída com sucesso")
