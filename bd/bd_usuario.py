from bd.bd_categorias import CategoriasBD
from bd.bd_subcategorias import SubcategoriasBD
from bd.conexao_bd import conectar_bd
from usuarios.sessao import UsuarioLogado

bd, cursor, error_bd = conectar_bd()
categoria = CategoriasBD()
subcategoria = SubcategoriasBD()
usuario_logado = UsuarioLogado()


class CriarUsuarios:

    @staticmethod
    def criar(nome, email, senha):
        criar_usuarios = f"INSERT INTO usuarios (nome, email, senha) VALUES ('{nome}', '{email}', '{senha}')"
        cursor.execute(criar_usuarios)
        bd.commit()
        id_novo_usuario = cursor.lastrowid
        categoria.inserir_categoria_padrao()
        subcategoria.inserir_subcateria_padrao(id_novo_usuario)
        print("Usuário cadastrado com sucesso")

    @staticmethod
    def consultar():
        consulta_usuarios = "SELECT nome FROM usuarios"
        cursor.execute(consulta_usuarios)
        usuarios = cursor.fetchall()
        return usuarios

    @staticmethod
    def excluir(del_usuario):
        excluir_usuario = f'UPDATE contas SET ativa = 0 WHERE id_usuario = {del_usuario}'
        cursor.execute(excluir_usuario)
        bd.commit()

    @staticmethod
    def verificar_login(email, senha):
        verificar_login = f"SELECT * FROM usuarios WHERE email = '{email}' AND senha = '{senha}'"
        cursor.execute(verificar_login)
        resultado = cursor.fetchall()

        if resultado:
            usuario_logado.id = resultado[0][0]
            usuario_logado.nome = resultado[0][1]
        else:
            print("Usuário não encontrado")
