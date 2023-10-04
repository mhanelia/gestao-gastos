from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()


class CartaoUsuario:

    @staticmethod
    def criar(id_conta, nome, limite, bandeira, cartao_padrao, ultimos_digitos, ativo, vencimento_fatura, fechamento_fatura):
        criar_cartao= f'''INSERT INTO cartao (
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
                       {usuario_logado.id},
                       {id_conta},
                       '{nome}',
                       {limite},
                       '{bandeira}',
                       {cartao_padrao},
                       {ultimos_digitos},
                       {ativo},
                       '{vencimento_fatura}',
                       '{fechamento_fatura}'
                       
                   )'''

        cursor.execute(criar_cartao)
        bd.commit()
        

    @staticmethod
    def ler():
        ler_cartao = f'''SELECT id,
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
                        WHERE id_usuario = {usuario_logado.id}
                        AND ativo = 1'''

        cursor.execute(ler_cartao)
        cartao = cursor.fetchall()

        if cartao:
            return cartao
        else:
            print("Usuário não possui cartões cadastrados")

    @staticmethod
    def atualizar_limite(limite, id_cartao):
        atualizar_saldo = f"UPDATE cartao SET limite = {limite} WHERE id = {id_cartao}"
        cursor.execute(atualizar_saldo)
        bd.commit()


    @staticmethod
    def excluir(id_cartao):
        excluir_conta = f'UPDATE cartao SET ativo = 0 WHERE id_usuario = {usuario_logado.id} AND id = {id_cartao}'
        cursor.execute(excluir_conta)
        bd.commit()

