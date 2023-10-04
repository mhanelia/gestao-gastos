import sqlite3
from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()


class CategoriasBD:
    @staticmethod
    def criar(nome):
        criar_categoria = f"INSERT INTO categorias (id_usuario, nome) VALUES ({usuario_logado.id}, '{nome}')"
        cursor.execute(criar_categoria)
        bd.commit()
        print("Categoria cadastrada com sucesso")

    @staticmethod
    def ler():
        ler_categorias = f"SELECT id, nome FROM categorias WHERE id_usuario = {usuario_logado.id} AND ativa = 1"
        cursor.execute(ler_categorias)
        categorias = cursor.fetchall()
        return categorias

    @staticmethod
    def atualizar_categoria(nome):
        atualizar_categoria = f"UPDATE categorias SET nome = '{nome}' WHERE id_usuario = {usuario_logado.id}"
        cursor.execute(atualizar_categoria)
        bd.commit()
        print("Categoria atualizada com sucesso")

    @staticmethod
    def excluir(id_categoria):
        excluir_categoria = f"UPDATE categorias SET ativa = 0 WHERE id = {id_categoria} AND id_usuario = {usuario_logado.id}"
        cursor.execute(excluir_categoria)
        bd.commit()
        print("Categoria excluída com sucesso")

    @staticmethod
    def inserir_categoria_padrao():
        campos = ["Alimentação", "Moradia", "Transporte", "Educação", "Saúde", "Lazer", "Outros"]

        for campo in campos:
            inserir_categoria_padrao = f"INSERT INTO categorias (id_usuario, nome) VALUES ({usuario_logado.id}, '{campo}')"
            cursor.execute(inserir_categoria_padrao)
            bd.commit()
        print('Categoria padrão inserida com sucesso')
