from bd.bd_categorias import CategoriasBD
from bd.bd_subcategorias import SubcategoriasBD
from bd.conexao_bd import conectar_bd
from usuarios.sessao import UsuarioLogado

bd, cursor, error_bd = conectar_bd()
categoria = CategoriasBD()
subcategoria = SubcategoriasBD()
usuario_logado = UsuarioLogado()


class UsuarioBD:

    @staticmethod
    def criar(nome, email, senha):
        criar_usuarios = "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)"
        cursor.execute(criar_usuarios, (nome, email, senha))
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
    def excluir(id_usuario):
        excluir_usuario = "UPDATE usuarios SET ativo = 0 WHERE id = ?"

        if usuario_logado.perfil == 'admin':
            if usuario_logado.id != id_usuario:
                cursor.execute(excluir_usuario, (id_usuario,))
                bd.commit()
            else:
                return "Não é possível excluir o próprio administrador"
        elif usuario_logado.perfil == 'usuario' and usuario_logado.id != id_usuario:
            return "Usuário não tem permissão para excluir"
        else:
            cursor.execute(excluir_usuario, (id_usuario,))
            bd.commit()

    @staticmethod
    def verificar_login(email, senha):
        verificar_login = """
            SELECT id, nome, perfil 
            FROM usuarios 
            WHERE email = ? AND senha = ?
        """
        cursor.execute(verificar_login, (email, senha))
        resultado = cursor.fetchone()
        bd.commit()

        if resultado:
            usuario_logado.id, usuario_logado.nome, usuario_logado.perfil = resultado
        else:
            return "Usuário não encontrado"

