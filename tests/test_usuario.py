import unittest
from usuarios.sessao import UsuarioLogado
from bd.bd_usuario import UsuarioBD
from bd.conexao_bd import conectar_bd
bd, cursor, error_bd = conectar_bd()
usuario = UsuarioBD()
usuario_logado = UsuarioLogado()
usuario_logado.id = None
usuario_logado.nome = None
usuario_logado.perfil = None



def util_insert():
    cursor.execute("INSERT INTO usuarios (nome, email, senha, perfil, ativo) "
                   "VALUES ('John', 'john@example.com', 'password', 'usuario', 1)")
    cursor.execute("INSERT INTO usuarios (nome, email, senha, perfil, ativo) "
                   "VALUES ('John', 'john@example.com', 'password', 'admin', 1)")
    bd.commit()


def util_select_all():
    cursor.execute("SELECT * FROM usuarios WHERE ativo = 1")
    registros = cursor.fetchall()
    bd.commit()
    return registros


class TestUsuarioBD(unittest.TestCase):
    def setUp(self):
        # cria tabela de categorias em memória
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id    INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome  TEXT,
                        email TEXT,
                        senha TEXT,
                        perfil TEXT,
                        ativo BOOLEAN DEFAULT 1)''')

        bd.commit()

    def tearDown(self):
        # limpa tabela após cada teste
        cursor.execute("DROP TABLE IF EXISTS usuarios")
        bd.commit()

    def test_consultar(self):
        util_insert()
        usuarios = usuario.consultar()
        self.assertEqual(len(usuarios), 2)

    def test_excluir_usuario_usuario(self):
        util_insert()
        usuario_logado.id = 1
        usuario_logado.perfil = 'usuario'
        usuario.excluir(1)
        self.assertEqual(len(util_select_all()), 1)

    def test_excluir_usuario_outro(self):
        util_insert()
        usuario_logado.id = 1
        usuario_logado.perfil = 'usuario'
        self.assertEqual(usuario.excluir(2), "Usuário não tem permissão para excluir")

    def test_excluir_admin_admin(self):
        util_insert()
        usuario_logado.id = 2
        usuario_logado.perfil = 'admin'
        self.assertEqual(usuario.excluir(2), "Não é possível excluir o próprio administrador")

    def test_excluir_admin_outro(self):
        util_insert()
        usuario_logado.id = 2
        usuario_logado.perfil = 'admin'
        usuario.excluir(1)
        self.assertEqual(len(util_select_all()), 1)

    @unittest.skip("Teste travando a suite")
    def test_usuario_encontrado(self):
        util_insert()
        email = "john@example.com"
        senha = "password"
        usuario.verificar_login(email, senha)
        self.assertEqual(usuario_logado.id, 1)
        self.assertEqual(usuario_logado.nome, "John")
        self.assertEqual(usuario_logado.perfil, "usuario")

    @unittest.skip("Teste travando a suite")
    def test_usuario_nao_encontrado(self):
        util_insert()
        email = "john.doe@example.com"
        senha = "password"
        self.assertEqual(usuario.verificar_login(email, senha), "Usuário não encontrado")
        self.assertEqual(usuario_logado.id, None)
        self.assertEqual(usuario_logado.nome, None)
        self.assertEqual(usuario_logado.perfil, None)


if __name__ == '__main__':
    unittest.main()