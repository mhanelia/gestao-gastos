import unittest
from bd.bd_cartao import CartaoBD
from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()
usuario_logado.id = 1


def util_insert():
    cursor.execute(
        "INSERT INTO cartao (id_usuario, id_conta, nome, cartao_padrao, ativo) VALUES(1, 1, 'Cartão Teste', 1, 1)")
    bd.commit()


def util_select_all():
    cursor.execute("SELECT * FROM cartao WHERE id_usuario = 1 AND ativo = 1")
    registros = cursor.fetchall()
    return registros


class TestCategoriasBD(unittest.TestCase):

    def setUp(self):
        cursor.execute('''CREATE TABLE IF NOT EXISTS cartao (
                        id                INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_usuario        INTEGER,
                        id_conta          INTEGER,
                        nome              TEXT,
                        limite            REAL,
                        bandeira          TEXT,
                        cartao_padrao     BOOLEAN DEFAULT 0,
                        ultimos_digitos   INTEGER,
                        ativo             BOOLEAN DEFAULT 1,
                        vencimento_fatura TEXT,
                        fechamento_fatura TEXT
                    )''')
        bd.commit()

    def tearDown(self):
        cursor.execute("DROP TABLE IF EXISTS cartao")
        bd.commit()

    def test_criar(self):
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
