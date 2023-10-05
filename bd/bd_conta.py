import sqlite3
from usuarios.sessao import UsuarioLogado
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuario_logado = UsuarioLogado()


class ContaDB:

    @staticmethod
    def criar(nome, banco, categoria, saldo, conta_padrao):
        criar_conta = "INSERT INTO contas (id_usuario, nome, banco, categoria, saldo, conta_padrao) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(criar_conta, (usuario_logado.id, nome, banco, categoria, saldo, conta_padrao))
        bd.commit()

    @staticmethod
    def ler(id_conta=None):
        if id_conta:
            ler_conta = "SELECT id, nome, banco, categoria, saldo, conta_padrao FROM contas WHERE id_usuario = ? AND id = ? AND ativa = 1"
            cursor.execute(ler_conta, (id_conta, usuario_logado.id))
        else:
            ler_conta = "SELECT id, nome, banco, categoria, saldo, conta_padrao FROM contas WHERE id_usuario = ? AND ativa = 1"
            cursor.execute(ler_conta, (usuario_logado.id,))
        bd.commit()
        conta = cursor.fetchall()
        if conta:
            return conta
        else:
            print("Usuário não possui contas")

    @staticmethod
    def excluir(id_conta):
        excluir_conta = "UPDATE contas SET ativa = 0 WHERE id_usuario = ? AND id = ?"
        cursor.execute(excluir_conta, (usuario_logado.id, id_conta))
        bd.commit()
        print("Conta excluída com sucesso")

    @staticmethod
    def ler_saldo(id_conta):
        ler_saldo = "SELECT saldo FROM contas WHERE id_usuario = ? AND id = ?"
        cursor.execute(ler_saldo, (usuario_logado.id, id_conta))
        bd.commit()
        saldo = cursor.fetchall()
        return saldo

    import sqlite3

    @staticmethod
    def atualizar_saldo_conta(novo_saldo, id_conta=None):
        try:

            if id_conta is None:
                cursor.execute("UPDATE contas SET saldo = ? WHERE conta_padrao = 1 AND id_usuario = ?",
                               (novo_saldo, usuario_logado.id))
            else:
                cursor.execute("SELECT id FROM contas WHERE id = ? AND id_usuario = ?",
                               (id_conta, usuario_logado.id))
                resultado = cursor.fetchone()

                if resultado:
                    cursor.execute("UPDATE contas SET saldo = ? WHERE id = ? AND id_usuario = ?",
                                   (novo_saldo, id_conta, usuario_logado.id))
                    bd.commit()
                else:
                    print("Conta não encontrada para o usuário especificado.")

        except error_bd as e:
            print("Erro no banco de dados:", e)
            bd.rollback()
