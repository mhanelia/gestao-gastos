import unittest
from unittest.mock import patch

from bd.bd_despesas import DespesaBD
from bd.conexao_bd import conectar_bd
from bd.criar_bd import CriarBanco
from usuarios.sessao import UsuarioLogado

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()
usuario_logado.id = 1


def util_insert():
    cursor.execute(
        "INSERT INTO despesas (id_usuario, id_conta, id_cartao, descricao, valor, data, id_categoria, id_subcategoria)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (1, 1, 1, "Teste Despesa", 100.00, "2022-01-01", 1, 1))
    bd.commit()


def util_select_all():
    cursor.execute("SELECT * FROM despesas WHERE id_usuario = 1 AND ativa = 1")
    bd.commit()
    registros = cursor.fetchall()
    return registros


class TestContasBD(unittest.TestCase):

    def setUp(self):
        CriarBanco.criar_tabela_categorias()
        CriarBanco.criar_tabela_subcategorias()
        CriarBanco.criar_tabela_despesas()
        cursor.execute('INSERT INTO categorias (nome) VALUES ("Categoria 1")')
        cursor.execute('INSERT INTO subcategorias (nome) VALUES ("Subcategoria 1")')
        bd.commit()

    def tearDown(self):
        # limpa tabela após cada teste
        cursor.execute("DROP TABLE IF EXISTS despesas")
        cursor.execute("DROP TABLE IF EXISTS categorias")
        cursor.execute("DROP TABLE IF EXISTS subcategorias")
        bd.commit()

    def test_criar_valida(self):
        id_conta = 1
        id_cartao = 2
        descricao = "Teste Despesa"
        valor = 100.00
        data = "2022-01-01"
        id_categoria = 3
        id_subcategoria = 4

        result = DespesaBD.criar(id_conta, id_cartao, descricao, valor, data, id_categoria, id_subcategoria)

        self.assertTrue(result)

    @patch('builtins.print')
    def test_criar_nulo(self, mock_print):
        id_conta = None
        id_cartao = 2
        descricao = "Teste Despesa"
        valor = 100.00
        data = "2022-01-01"
        id_categoria = 3
        id_subcategoria = 4
        with self.assertRaises(ValueError) as contexto:
            DespesaBD.criar(id_conta, id_cartao, descricao, valor, data, id_categoria, id_subcategoria)
        excecao = contexto.exception
        self.assertEqual(str(excecao), 'Todos os campos devem ser informados')

    @unittest.skip("Não implementado")
    def test_criar_database_error(self):
        # TODO - campo integer salvando string
        pass

    def test_listar(self):
        util_insert()
        result = DespesaBD.listar()
        self.assertNotEqual(result, [])

    def test_atualizar(self):
        util_insert()
        print(util_select_all())
        id_despesa = 1
        id_conta = 2
        id_cartao = 3
        descricao = "Teste Despesa atualizada"
        valor = 1100.00
        data = "2023-01-01"
        id_categoria = 4
        id_subcategoria = 5
        DespesaBD.atualizar(id_despesa, id_conta, id_cartao, descricao, valor, data, id_categoria, id_subcategoria)
        result = util_select_all()
        print(result)
        self.assertEqual(result[0][2], id_conta)
        self.assertEqual(result[0][3], id_cartao)
        self.assertEqual(result[0][4], descricao)
        self.assertEqual(result[0][5], valor)
        self.assertEqual(result[0][6], data)
        self.assertEqual(result[0][7], id_categoria)
        self.assertEqual(result[0][8], id_subcategoria)

    def test_atualizar_id_conta(self):
        util_insert()
        id_despesa = 1
        id_conta = 2

        DespesaBD.atualizar(id_despesa, id_conta=id_conta)
        result = util_select_all()
        self.assertEqual(result[0][2], id_conta)
        self.assertEqual(result[0][3], 1)
        self.assertEqual(result[0][4], "Teste Despesa")
        self.assertEqual(result[0][5], 100.00)
        self.assertEqual(result[0][6], "2022-01-01")
        self.assertEqual(result[0][7], 1)
        self.assertEqual(result[0][8], 1)

    def test_atualizar_id_cartao(self):
        util_insert()
        id_despesa = 1
        id_cartao = 2

        DespesaBD.atualizar(id_despesa, id_cartao=id_cartao)
        result = util_select_all()
        self.assertEqual(result[0][2], 1)
        self.assertEqual(result[0][3], id_cartao)
        self.assertEqual(result[0][4], "Teste Despesa")
        self.assertEqual(result[0][5], 100.00)
        self.assertEqual(result[0][6], "2022-01-01")
        self.assertEqual(result[0][7], 1)
        self.assertEqual(result[0][8], 1)

    def test_atualizar_descricao(self):
        util_insert()
        id_despesa = 1
        descricao = "Teste Despesa atualizada"
        DespesaBD.atualizar(id_despesa, descricao=descricao)
        result = util_select_all()
        self.assertEqual(result[0][2], 1)
        self.assertEqual(result[0][3], 1)
        self.assertEqual(result[0][4], descricao)
        self.assertEqual(result[0][5], 100.00)
        self.assertEqual(result[0][6], "2022-01-01")
        self.assertEqual(result[0][7], 1)
        self.assertEqual(result[0][8], 1)

    def test_atualizar_valor(self):
        util_insert()
        id_despesa = 1
        valor = 1100.00
        DespesaBD.atualizar(id_despesa, valor=valor)
        result = util_select_all()
        self.assertEqual(result[0][2], 1)
        self.assertEqual(result[0][3], 1)
        self.assertEqual(result[0][4], "Teste Despesa")
        self.assertEqual(result[0][5], valor)
        self.assertEqual(result[0][6], "2022-01-01")
        self.assertEqual(result[0][7], 1)
        self.assertEqual(result[0][8], 1)

    def test_atualizar_data(self):
        util_insert()
        id_despesa = 1
        data = "2023-01-01"
        DespesaBD.atualizar(id_despesa, data=data)
        result = util_select_all()
        self.assertEqual(result[0][2], 1)
        self.assertEqual(result[0][3], 1)
        self.assertEqual(result[0][4], "Teste Despesa")
        self.assertEqual(result[0][5], 100.00)
        self.assertEqual(result[0][6], data)
        self.assertEqual(result[0][7], 1)
        self.assertEqual(result[0][8], 1)

    def test_atualizar_id_categoria(self):
        util_insert()
        id_despesa = 1
        id_categoria = 2
        DespesaBD.atualizar(id_despesa, id_categoria=id_categoria)
        result = util_select_all()
        self.assertEqual(result[0][2], 1)
        self.assertEqual(result[0][3], 1)
        self.assertEqual(result[0][4], "Teste Despesa")
        self.assertEqual(result[0][5], 100.00)
        self.assertEqual(result[0][6], "2022-01-01")
        self.assertEqual(result[0][7], id_categoria)
        self.assertEqual(result[0][8], 1)



    @unittest.skip("Não implementado")
    def test_atualizar_invalid_expense(self):
        # TODO - criar testes para atualizar despesas invalidas
        pass

    @unittest.skip("Não implementado")
    def test_atualizar_missing_fields(self):
        # TODO - criar testes para atualizar despesas com campos obrigatórios faltando
        pass

    def test_excluir(self):
        util_insert()
        id_despesa = 1
        DespesaBD.excluir(id_despesa)
        result = util_select_all()
        self.assertEqual(result, [])

    def test_ler(self):
        util_insert()
        result = DespesaBD.ler(1)
        self.assertEqual(result[0][2], 1)
        self.assertEqual(result[0][3], 1)
        self.assertEqual(result[0][4], "Teste Despesa")
        self.assertEqual(result[0][5], 100.00)
        self.assertEqual(result[0][6], "2022-01-01")
        self.assertEqual(result[0][7], 1)
        self.assertEqual(result[0][8], 1)


if __name__ == '__main__':
    unittest.main()
