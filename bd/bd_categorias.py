from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()
usuario_logado.id = 1


class CategoriasBD:
    @staticmethod
    def criar(nome):
        criar_categoria = "INSERT INTO categorias (id_usuario, nome) VALUES (?, ?)"
        cursor.execute(criar_categoria, (usuario_logado.id, nome))
        bd.commit()
        print("Categoria cadastrada com sucesso")

    @staticmethod
    def ler():
        ler_categorias = "SELECT id, nome FROM categorias WHERE id_usuario = ? AND ativa = 1"
        cursor.execute(ler_categorias, (usuario_logado.id,))
        categorias = cursor.fetchall()
        return categorias

    @staticmethod
    def atualizar(nome, id_categoria):
        atualizar_categoria = "UPDATE categorias SET nome = ? WHERE id = ? AND id_usuario = ?"
        cursor.execute(atualizar_categoria, (nome, id_categoria, usuario_logado.id))
        bd.commit()
        print("Categoria atualizada com sucesso")

    @staticmethod
    def excluir(id_categoria):
        excluir_categoria = "UPDATE categorias SET ativa = 0 WHERE id = ? AND id_usuario = ?"
        cursor.execute(excluir_categoria, (id_categoria, usuario_logado.id))
        bd.commit()
        print("Categoria excluída com sucesso")

    @staticmethod
    def inserir_categoria_padrao():
        campos = ["Alimentação", "Moradia", "Transporte", "Educação", "Saúde", "Lazer", "Outros"]

        for campo in campos:
            inserir_categoria_padrao = "INSERT INTO categorias (id_usuario, nome) VALUES (?, ?)"
            cursor.execute(inserir_categoria_padrao, (usuario_logado.id, campo))
            bd.commit()
        print('Categoria padrão inserida com sucesso')
