import sqlite3
from usuarios.sessao import UsuarioLogado
import sistema
from bd.bd_conta import ContaUsuario
from tabulate import tabulate

bd = sqlite3.connect("./bd/bancodedados.db", check_same_thread=False)
cursor = bd.cursor()
usuario_logado = UsuarioLogado()
conta = ContaUsuario()



class Conta:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Conta, cls).__new__(cls)
            cls._instance.id = None
            cls._instance.saldo = None
            cls._instance.banco = None
            cls._instance.categoria = None
        return cls._instance

    @staticmethod
    def criar(nome, banco, categoria, saldo, conta_padrao):
        # TODO - Se a nova conta for padrão, precisa tirar o padrão da outro conta
        # TODO - Toda primeira conta tem que ser padrão
        # TODO - A partir da segunda conta, não pode haver mais de uma conta com o mesmo nome
        # TODO - A partir da segunda conta, o conta padrão é falso por padrão

        if not (nome and banco and categoria and saldo and conta_padrao):
            nome = sistema.input_obrigatorio("Nome da conta: ")
            banco = sistema.input_obrigatorio("Nome do banco: ")
            categoria = sistema.input_obrigatorio("Nome da categoria: ")
            saldo = sistema.float_obrigatorio("Saldo inicial: ")
            conta_padrao = sistema.input_obrigatorio("Conta padrão: ")

        conta.criar(nome, banco, categoria, saldo, conta_padrao)

        print("Conta cadastrada com sucesso")

    @staticmethod
    def ler(id_conta=None):
        dados = conta.ler(id_conta)
        cabecalho = ["ID", "Nome da conta", "Banco", "Tipo de conta", "Saldo da conta", "Conta padrão"]
        print(tabulate(dados, headers=cabecalho, tablefmt="grid"))

    @staticmethod
    def calcular_novo_saldo(id_conta, valor_despesa, novo_valor_despesa=None):
        if novo_valor_despesa is not None:
            saldo_atual = conta.ler_saldo(id_conta)[0][0]
            diferenca = novo_valor_despesa - valor_despesa
            novo_saldo = saldo_atual - diferenca
            return novo_saldo

        else:
            saldo_atual = conta.ler_saldo(id_conta)[0][0]
            novo_saldo = saldo_atual - valor_despesa
            return novo_saldo



    @staticmethod
    def atualizar(nome, banco, categoria, saldo, conta_padrao):
        # TODO - atualizar função
        atualizar_conta = f"UPDATE contas SET nome = '{nome}', banco = '{banco}', categoria = '{categoria}', saldo = {saldo}, conta_padrao = {conta_padrao} WHERE id_usuario = {usuario_logado.id}"
        cursor.execute(atualizar_conta)
        bd.commit()
        print("Conta atualizada com sucesso")

    def excluir(self):
        self.ler()
        id_conta = sistema.input_obrigatorio("Qual o ID da conta que deseja excluir?")
        conta.excluir(id_conta)
        print("Conta excluída com sucesso")

    @staticmethod
    def verificar_existencia():
        # TODO - atualizar função

        if usuario_logado.id is None:
            return False

        validar_conta = f"SELECT * FROM contas WHERE id_usuario = {usuario_logado.id}"
        cursor.execute(validar_conta)
        conta_existe = cursor.fetchall()

        if conta_existe:
            return True
        else:
            return False

    @staticmethod
    def informacoes():
        consulta = f'''
        SELECT c.id, c.banco, c.saldo, c.categoria
        FROM contas AS c
        INNER JOIN usuarios AS u ON c.id_usuario = u.id
        WHERE u.id = {usuario_logado.id}
        AND c.ativa = 1
        '''

        cursor.execute(consulta)
        resultados = cursor.fetchall()

        for resultado in resultados:
            id_conta, banco, saldo, categoria = resultado
            dados = [
                ["ID da conta padrão", id_conta],
                ["Banco padrão", banco],
                ["Saldo atual", saldo],
                ["Categoria da conta", categoria]
            ]
            formato_tabela = "grid"
            tabela_formatada = tabulate(dados, headers=["Descrição", "Valor"], tablefmt=formato_tabela)
            print(tabela_formatada)

    @staticmethod
    def ler_saldo(id_conta):
        return conta.ler_saldo(id_conta)

    @staticmethod
    def atualizar_saldo_conta(id_conta, novo_saldo):
        return conta.atualizar_saldo_conta(novo_saldo, id_conta)

    @staticmethod
    def atualizar_saldo(saldo, id_conta):
        # TODO - atualizar função
        atualizar_saldo = f"UPDATE contas SET saldo = {saldo} WHERE id = {id_conta} AND id_usuario = {usuario_logado.id}"
        cursor.execute(atualizar_saldo)
        bd.commit()
        print("Saldo atualizado com sucesso")
