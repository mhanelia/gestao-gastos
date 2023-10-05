from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()


class CartaoBD:

    @staticmethod
    def criar(id_conta, nome, limite, bandeira, cartao_padrao, ultimos_digitos, ativo, vencimento_fatura,
              fechamento_fatura):
        criar_cartao = '''INSERT INTO cartao (
                       id_usuario,
                       id_conta,
                       nome,
                       limite,
                       bandeira,
                       cartao_padrao,
                       ultimos_digitos,
                       ativo,
                       vencimento_fatura,
                       fechamento_fatura
                   )
                   VALUES (
                       ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                   )'''

        cursor.execute(criar_cartao, (usuario_logado.id, id_conta, nome, limite, bandeira, cartao_padrao,
                                      ultimos_digitos, ativo, vencimento_fatura, fechamento_fatura))
        bd.commit()
        print("Cartão criado com sucesso")

    @staticmethod
    def ler():
        ler_cartao = '''SELECT id,
                            id_conta,
                            nome,
                            limite,
                            bandeira,
                            cartao_padrao,
                            ultimos_digitos,
                            ativo,
                            vencimento_fatura,
                            fechamento_fatura
                        FROM cartao
                        WHERE id_usuario = ?
                        AND ativo = 1'''

        cursor.execute(ler_cartao, (usuario_logado.id,))
        cartao = cursor.fetchall()

        if cartao:
            return cartao
        else:
            print("Usuário não possui cartões cadastrados")

    @staticmethod
    def atualizar_limite(limite, id_cartao):
        atualizar_saldo = "UPDATE cartao SET limite = ? WHERE id = ?"
        cursor.execute(atualizar_saldo, (limite, id_cartao))
        bd.commit()
        print("Limite atualizado com sucesso")

    @staticmethod
    def excluir(id_cartao):
        excluir_conta = "UPDATE cartao SET ativo = 0 WHERE id_usuario = ? AND id = ?"
        cursor.execute(excluir_conta, (usuario_logado.id, id_cartao))
        bd.commit()
        print("Cartão excluído com sucesso")
