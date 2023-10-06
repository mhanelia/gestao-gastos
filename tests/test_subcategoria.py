import unittest
from bd.bd_subcategorias import SubcategoriasBD
from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()
usuario_logado.id = 1


def util_insert():
    cursor.execute("INSERT INTO subcategorias (id_usuario, nome, id_categoria) VALUES(1, 'Lazer', 1)")
    bd.commit()


def util_select_all():
    cursor.execute("SELECT * FROM subcategorias WHERE id_usuario = 1 AND ativa = 1")
    registros = cursor.fetchall()
    return registros


class TestCategoriasBD(unittest.TestCase):

    def setUp(self):
        # cria tabela de categorias em memória
        cursor.execute('''CREATE TABLE IF NOT EXISTS subcategorias(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_usuario INTEGER,
                        id_categoria INTEGER,
                        nome TEXT,
                        ativa BOOLEAN DEFAULT 1)''')
        bd.commit()

    def tearDown(self):
        # limpa tabela após cada teste
        cursor.execute("DROP TABLE IF EXISTS subcategorias")
        bd.commit()

    def test_excluir_(self):
        util_insert()
        SubcategoriasBD.excluir(1)
        self.assertEqual(len(util_select_all()), 0)

    def test_criar_(self):
        SubcategoriasBD.criar("Lazer", 1)
        self.assertEqual(len(util_select_all()), 1)

    def test_ler(self):
        util_insert()
        subcategorias = SubcategoriasBD.ler(1)
        self.assertEqual(len(subcategorias), 1)
        print("Categoria lida: ", subcategorias[0][1])

    def test_atualizar(self):
        util_insert()
        nova_categoria = "Alimentação"
        SubcategoriasBD.atualizar(nova_categoria, 1)
        resultado = util_select_all()
        nome_atual = str(resultado[0][3])
        self.assertEqual(nome_atual, nova_categoria)

    def test_inserir_categoria_padrao(self):
        SubcategoriasBD.inserir_subcateria_padrao(1)
        self.assertEqual(len(util_select_all()), 9)


if __name__ == '__main__':
    unittest.main()
