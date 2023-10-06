from bd.conexao_bd import conectar_bd
from usuarios.sessao import UsuarioLogado

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()


class SubcategoriasBD:

    @staticmethod
    def criar(nome, categoria):
        criar_subcategoria = "INSERT INTO subcategorias (id_usuario, nome, id_categoria) VALUES (?, ?, ?)"
        cursor.execute(criar_subcategoria, (usuario_logado.id, nome, categoria))
        bd.commit()
        print("Subcategoria cadastrada com sucesso")

    @staticmethod
    def ler(id_categoria):
        ler_subcategorias = "SELECT id, nome FROM subcategorias WHERE id_usuario = ? AND id_categoria = ? AND ativa = 1"
        cursor.execute(ler_subcategorias, (usuario_logado.id, id_categoria))
        bd.commit()
        subcategorias = cursor.fetchall()
        return subcategorias

    @staticmethod
    def atualizar(nome, id_subcategoria):
        atualizar_subcategoria = "UPDATE subcategorias SET nome = ? WHERE id = ? AND id_usuario = ?"
        cursor.execute(atualizar_subcategoria, (nome, id_subcategoria, usuario_logado.id))
        bd.commit()
        print("Subcategoria atualizada com sucesso")

    @staticmethod
    def excluir(id_subcategoria):
        excluir_subcategoria = "UPDATE subcategorias SET ativa = 0 WHERE id = ?"
        cursor.execute(excluir_subcategoria, (id_subcategoria,))
        bd.commit()
        print("Subcategoria excluída com sucesso")

    @staticmethod
    def inserir_subcateria_padrao(id_novo_usuario):
        campos = ["Restaurant", "Supermercado", "Lanches", "Aluguel", "Hipoteca", "Serviços de Utilidades",
                  "Combustível", "Transporte Público", "Manutenção de Veículos"]

        id_categoria = 1

        for i, campo in enumerate(campos):

            inserir_subcategoria_padrao = ("INSERT INTO subcategorias (id_usuario, nome, id_categoria) "
                                           "VALUES (?, ?, ?)")
            cursor.execute(inserir_subcategoria_padrao, (id_novo_usuario, campo, id_categoria))
            bd.commit()

            if i > 0 and i % 3 == 0:
                id_categoria += 1
