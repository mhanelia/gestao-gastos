from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()


class DespesaBD:

    @staticmethod
    def criar(id_conta, id_cartao, descricao, valor, data, id_categoria, id_subcategoria):
        try:
            criar_despesa = """
                INSERT INTO despesas 
                (id_usuario, id_conta, id_cartao, descricao, valor, data, id_categoria, id_subcategoria) 
                VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(criar_despesa, (
                usuario_logado.id, id_conta, id_cartao, descricao, valor, data, id_categoria, id_subcategoria))
            bd.commit()
            return True

        except Exception as error:
            print("Ocorreu uma falha: ", error)
            return False

    @staticmethod
    def listar():
        listar_despesas = '''SELECT 
                                  d.id,
                                  d.id_conta,
                                  d.id_cartao,
                                  d.descricao,
                                  d.valor,
                                  d.data,
                                  c.nome as nome_categoria,
                                  sc.nome as nome_subcategoria,
                                  d.ativa
                                FROM despesas d
                                JOIN categorias c on d.id_categoria = c.id 
                                JOIN subcategorias sc on d.id_subcategoria = sc.id
                                WHERE d.id_usuario = ? 
                                AND d.ativa = 1'''

        cursor.execute(listar_despesas, usuario_logado.id)
        despesas = cursor.fetchall()
        return despesas

    @staticmethod
    def atualizar(id_despesa, id_conta, id_cartao, descricao, valor, data, id_categoria, id_subcategoria):
        atualizar_despesa = """UPDATE despesas
                                   SET id_conta = ?,
                                       id_cartao = ?,
                                       descricao = ?,
                                       valor = ?,
                                       data = ?,
                                       id_categoria = ?,
                                       id_subcategoria = ?
                                   WHERE id = ? AND 
                                   id_usuario = ?"""
    valores = (id_conta, id_cartao, descricao, valor, data, id_categoria, id_subcategoria, id_despesa, usuario_logado.id)
    cursor.execute(atualizar_despesa, valores =)
        bd.commit()
        print("Despesa atualizada com sucesso")

    @staticmethod
    def excluir(id_despesa):
        excluir_despesa = f"UPDATE despesas SET ativa = 0 WHERE id = {id_despesa}"
        cursor.execute(excluir_despesa)
        bd.commit()
        print("Despesa excluída com sucesso")

    @staticmethod
    def atualizar2(id_despesa, id_conta=None, id_cartao=None, descricao=None, valor=None, data=None, id_categoria=None,
                   id_subcategoria=None):
        try:
            atualizar_despesa = 'UPDATE despesas SET '

            if id_conta is not None:
                atualizar_despesa += f'id_conta = {id_conta}, '
            if id_cartao != '':
                atualizar_despesa += f'id_cartao = {id_cartao} , '
            if descricao is not None:
                atualizar_despesa += f"descricao = '{descricao}', "
            if valor is not None:
                atualizar_despesa += f'valor = {valor}, '
            if data is not None:
                atualizar_despesa += f"data = '{data}', "
            if id_categoria is not None:
                atualizar_despesa += f'id_categoria = {id_categoria}, '
            if id_subcategoria is not None:
                atualizar_despesa += f'id_subcategoria = {id_subcategoria}, '

            atualizar_despesa = atualizar_despesa.rstrip(", ")
            atualizar_despesa += f" WHERE id = {id_despesa}"
            cursor.execute(atualizar_despesa)
            bd.commit()

        except error_bd as e:
            print("Erro no banco de dados:", e)
            bd.rollback()



    @staticmethod
    def ler(id_despesa):
        listar_despesa = f'SELECT * FROM despesas WHERE id = {id_despesa}'
        cursor.execute(listar_despesa)
        dados_despesa = cursor.fetchall()
        return dados_despesa

