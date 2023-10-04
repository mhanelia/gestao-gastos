from tabulate import tabulate

from usuarios.sessao import UsuarioLogado
from bd.bd_despesas import DespesaBD
from contas.conta import Conta
from contas.cartao import Cartao
from categorias.categoria import Categoria
from subcategorias.subcategoria import Subcategoria
import sistema

usuario_logado = UsuarioLogado()
conta = Conta()
despesa_bd = DespesaBD()
cartao = Cartao()
categoria = Categoria()
subcategoria = Subcategoria()


class DespesasUsuario:

    @staticmethod
    def criar():
        sistema.limpar_terminal()
        conta.ler()
        id_conta = sistema.input_obrigatorio("Atribuir a despesa a qual conta? ")
        sistema.limpar_terminal()
        cartao.ler()
        id_cartao = input("Atribuir a despesa a qual cartão? (opcional): ")

        descricao = sistema.input_obrigatorio("Descrição da despesa: ")
        data = sistema.input_obrigatorio("Data da despesa: (DD-MM-AAAA): ")

        categoria.ler()
        id_categoria = sistema.input_obrigatorio("ID da categoria da despesa: ")

        subcategoria.ler(id_categoria)
        id_subcategorias = sistema.input_obrigatorio("Subcategoria da despesa: ")

        valor = sistema.float_obrigatorio("Qual o valor da despesa: ")

        if not id_cartao:
            id_cartao = "NULL"

        if valor > 0:
            # TODO - Validar o criar a despesa, erro na linha 46
            if despesa_bd.criar(id_conta, id_cartao, descricao, valor, data, id_categoria, id_subcategorias):
                novo_saldo = conta.calcular_novo_saldo(id_conta, valor)
                conta.atualizar_saldo_conta(id_conta, novo_saldo)

            else:
                print("Não foi possível criar a despesa, tente novamente.")
        if valor <= 0:
            print("O valor da despesa precisa ser um número maior que 0")

        conta.ler(id_conta)
        print("Despesa cadastrada com sucesso")

    @staticmethod
    def listar():
        custos = despesa_bd.listar()
        cabecalho = ["ID da despesa", "A qual conta está vinculada", "A qual cartão está vinculada",
                     "Descrição da despesa", "Data da despesa", "Valor da despesa", "Categoria da despesa",
                     "Subcategoria da despesa", "Ativada"]
        print(tabulate(custos, headers=cabecalho, tablefmt="grid"))

    def atualizar(self):
        self.listar()
        id_despesa = sistema.input_obrigatorio("Qual a despesa que deseja atualizar? ")
        id_conta = sistema.input_obrigatorio("Atribuir a despesa a qual conta? ")
        id_cartao = input("Atribuir a despesa a qual cartão? (opcional) ")
        descricao = sistema.input_obrigatorio("Descrição da despesa: ")
        data = sistema.input_obrigatorio("Data da despesa: (DD-MM-AAAA) ")
        id_categoria = sistema.input_obrigatorio("Categoria da despesa: ")
        id_subcategoria = sistema.input_obrigatorio("Subcategoria da despesa: ")
        valor = sistema.float_obrigatorio("Qual o valor da despesa: ")

        if valor > 0:
            valor_despesa = despesa_bd.ler(id_despesa)[0][5]
            novo_saldo = conta.calcular_novo_saldo(id_conta, valor_despesa, valor)
            despesa_bd.atualizar2(id_despesa, id_conta, id_cartao, descricao, valor, data, id_categoria,
                                  id_subcategoria)
            conta.atualizar_saldo_conta(id_conta, novo_saldo)
        else:
            print("Não foi possível atualizar a despesa, tente novamente.")

        if valor <= 0:
            print("O valor da despesa precisa ser um número maior que 0")

    def excluir(self):
        while True:
            print(self.listar())
            id_despesa = sistema.input_obrigatorio("Qual a despesa que deseja excluir? [Digite 0 para cancelar] ")

            if int(id_despesa) in self.listar_id_despesa():
                despesa_bd.excluir(id_despesa)
                break
            elif id_despesa == "0":
                break
            else:
                print("Despesa não encontrada")

    @staticmethod
    def listar_id_despesa():
        id_despesas = []
        custos = despesa_bd.listar()

        for custo in custos:
            id_despesas.append(int(custo[0]))

        return id_despesas
