import unittest

from bd.bd_cartao import CartaoBD
from bd.conexao_bd import conectar_bd
from bd.criar_bd import CriarBanco
from usuarios.sessao import UsuarioLogado

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()


def util_insert():
    cursor.execute(
        "INSERT INTO cartao (id_usuario, id_conta, nome, cartao_padrao, ativo) VALUES(1, 1, 'Cartão Teste', 1, 1)")
    bd.commit()


def util_select_all():
    cursor.execute("SELECT * FROM cartao WHERE id_usuario = 1 AND ativo = 1")
    registros = cursor.fetchall()
    return registros


class TestCartaoBD(unittest.TestCase):
    def setUp(self):
        CriarBanco.criar_tabela_cartao()

    def tearDown(self):
        cursor.execute("DROP TABLE IF EXISTS cartao")
        bd.commit()

    def test_criar(self):
        usuario_logado.id = 1
        CartaoBD.criar(1, "Cartão 1", 1000, "Visa", 0, 1234, 1, "12/12/2021", "12/12/2021")
        self.assertEqual(len(util_select_all()), 1)

    def test_ler(self):
        util_insert()
        cartao = CartaoBD.ler()
        self.assertEqual(len(cartao), 1)
        print("Cartão lido: ", cartao[0][2])

    def test_ler_erro(self):
        self.assertEqual(CartaoBD.ler(), "Usuário não possui cartões cadastrados")

    def test_atualizar_limite(self):
        util_insert()
        CartaoBD.atualizar_limite(1000, 1)
        self.assertEqual(len(util_select_all()), 1)
        self.assertEqual(util_select_all()[0][4], 1000)

    def test_excluir(self):
        util_insert()
        CartaoBD.excluir(1)
        self.assertEqual(len(util_select_all()), 0)


if __name__ == '__main__':
    unittest.main()
