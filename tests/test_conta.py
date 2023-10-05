import unittest
from unittest.mock import patch

from bd.bd_conta import ContaDB
from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()
usuario_logado.id = 1


def util_insert():
    cursor.execute(
        "INSERT INTO contas (id_usuario, nome, banco, categoria, saldo, conta_padrao) "
        "VALUES(1, 'Conta Teste', 'Banco Teste', 'Alimentação', 1000, 1)")
    bd.commit()


def util_select_all():
    cursor.execute("SELECT * FROM contas WHERE id_usuario = 1 AND ativa = 1")
    bd.commit()
    registros = cursor.fetchall()
    return registros


class TestContasBD(unittest.TestCase):

    def setUp(self):
        # cria tabela de categorias em memória
        cursor.execute('''CREATE TABLE IF NOT EXISTS contas (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario   INTEGER,
            nome         TEXT,
            banco        TEXT,
            categoria    TEXT,
            saldo        REAL,
            ativa        BOOLEAN DEFAULT 1,
            conta_padrao BOOLEAN DEFAULT 0
        )''')
        bd.commit()

    def tearDown(self):
        # limpa tabela após cada teste
        cursor.execute("DROP TABLE IF EXISTS contas")
        bd.commit()

    def test_excluir(self):
        util_insert()
        ContaDB.excluir(1)
        self.assertEqual(len(util_select_all()), 0)

    def test_criar(self):
        # cria a categoria
        ContaDB.criar("Conta Teste", "Banco Teste", "Conta Corrente", 1000, 1)
        self.assertEqual(len(util_select_all()), 1)
        self.assertEqual(util_select_all()[0][2], "Conta Teste")
        self.assertEqual(util_select_all()[0][3], "Banco Teste")
        self.assertEqual(util_select_all()[0][4], "Conta Corrente")
        self.assertEqual(util_select_all()[0][5], 1000)
        self.assertEqual(util_select_all()[0][6], 1)

    def test_ler(self):
        util_insert()
        conta = ContaDB.ler()
        self.assertEqual(len(conta), 1)
        print("Conta lida: ", conta[0][2])

    def test_ler_saldo(self):
        util_insert()
        saldo = ContaDB.ler_saldo(1)
        self.assertEqual(saldo[0][0], 1000)
        print("Saldo lido: ", saldo[0][0])

    def test_atualizar_saldo_conta_with_id_conta_none(self):
        novo_saldo = 1500
        util_insert()
        ContaDB.atualizar_saldo_conta(novo_saldo, id_conta=None)
        saldo = ContaDB.ler_saldo(1)
        self.assertEqual(saldo[0][0], novo_saldo)
        print("Saldo lido: ", saldo[0][0])

    def test_atualizar_saldo_conta_with_valid_id_conta(self):
        novo_saldo = 2000
        util_insert()
        ContaDB.atualizar_saldo_conta(novo_saldo, 1)
        saldo = ContaDB.ler_saldo(1)
        self.assertEqual(saldo[0][0], novo_saldo)
        print("Saldo lido: ", saldo[0][0])

    @patch('builtins.print')
    def test_atualizar_saldo_id_invalido(self, mock_print):
        util_insert()
        novo_saldo = 2500
        ContaDB.atualizar_saldo_conta(novo_saldo, 2)
        mock_print.assert_called_once_with("Conta não encontrada para o usuário especificado.")


if __name__ == '__main__':
    unittest.main()
