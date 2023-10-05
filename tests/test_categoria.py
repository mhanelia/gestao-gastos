import unittest
from bd.bd_categorias import CategoriasBD
from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()
usuario_logado.id = 1


def util_insert():
    cursor.execute("INSERT INTO categorias VALUES(1, 1, 'Lazer',  1)")
    bd.commit()


def util_select_all():
    cursor.execute("SELECT * FROM categorias WHERE id_usuario = 1 AND ativa = 1")
    registros = cursor.fetchall()
    return registros


class TestCategoriasBD(unittest.TestCase):

    def setUp(self):
        # cria tabela de categorias em memória
        cursor.execute("CREATE TABLE IF NOT EXISTS categorias ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                       "id_usuario INTEGER, "
                       "nome TEXT, "
                       "ativa BOOLEAN DEFAULT 1)")

    def tearDown(self):
        # limpa tabela após cada teste
        cursor.execute("DROP TABLE IF EXISTS categorias")
        bd.commit()

    def test_excluir_categoria(self):
        util_insert()
        CategoriasBD.excluir(1)
        self.assertEqual(len(util_select_all()), 0)

    def test_criar_categoria(self):
        # cria a categoria
        categoria = CategoriasBD.criar("Lazer")
        self.assertEqual(len(util_select_all()), 1)

    def test_ler_categorias(self):
        util_insert()
        categorias = CategoriasBD.ler()
        self.assertEqual(len(categorias), 1)
        print("Categoria lida: ", categorias[0][1])

    def test_atualizar_categoria(self):
        util_insert()
        nova_categoria = "Alimentação"
        CategoriasBD.atualizar(nova_categoria, 1)
        resultado = util_select_all()
        nome_atual: str = resultado[0][2]
        self.assertEqual(nome_atual, nova_categoria)

    def test_inserir_categoria_padrao(self):
        CategoriasBD.inserir_categoria_padrao()
        self.assertEqual(len(util_select_all()), 7)


if __name__ == '__main__':
    unittest.main()
