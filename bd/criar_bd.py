from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()


class CriarBanco:

    @staticmethod
    def criar_tabela_usuarios():
        criar_tabela_usuarios = '''CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            senha TEXT,
            perfil TEXT (30) NOT NULL DEFAULT usuario,
            ativo BOOLEAN DEFAULT 1
            )'''
        cursor.execute(criar_tabela_usuarios)
        bd.commit()
        print("Tabela usuarios criada com sucesso")

    @staticmethod
    def criar_tabela_contas():
        criar_tabela_contas = '''CREATE TABLE IF NOT EXISTS contas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                nome TEXT,
                banco TEXT,
                categoria TEXT,
                saldo REAL,
                ativa BOOLEAN DEFAULT 1,
                conta_padrao BOOLEAN DEFAULT 0
                )'''
        cursor.execute(criar_tabela_contas)
        bd.commit()
        print("Tabela contas criada com sucesso")

    @staticmethod
    def criar_tabela_cartao():
        criar_tabela_cartao = '''CREATE TABLE IF NOT EXISTS cartao(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                id_conta INTEGER,
                nome TEXT,
                limite REAL,
                bandeira TEXT,
                cartao_padrao BOOLEAN DEFAULT 0,
                ultimos_digitos INTEGER,
                ativo BOOLEAN DEFAULT 1,
                vencimento_fatura TEXT,
                fechamento_fatura TEXT
                )'''
        cursor.execute(criar_tabela_cartao)
        bd.commit()
        print("Tabela cartao criada com sucesso")

    @staticmethod
    def criar_tabela_despesas():
        criar_tabela_despesa = '''CREATE TABLE IF NOT EXISTS despesas(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario      INTEGER,
                    id_conta        INTEGER,
                    id_cartao       INTEGER,
                    descricao       TEXT,
                    valor           REAL,
                    data            TEXT,
                    id_categoria    INTEGER,
                    id_subcategoria INTEGER,
                    ativa           BOOLEAN DEFAULT 1,
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id),
                    FOREIGN KEY(id_categoria) REFERENCES categorias(id),
                    FOREIGN KEY(id_subcategoria) REFERENCES subcategorias(id)
                )'''
        cursor.execute(criar_tabela_despesa)
        bd.commit()
        print('Tabela despesas criada com sucesso')

    @staticmethod
    def criar_tabela_categorias():
        criar_tabela_categorias = '''CREATE TABLE IF NOT EXISTS categorias(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                nome TEXT,
                ativa BOOLEAN DEFAULT 1,
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
                )'''
        cursor.execute(criar_tabela_categorias)
        bd.commit()
        print('Tabela categorias criada com sucesso')

    @staticmethod
    def criar_tabela_subcategorias():
        criar_tabela_subcategorias = '''CREATE TABLE IF NOT EXISTS subcategorias(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                id_categoria INTEGER,
                nome TEXT,
                ativa BOOLEAN DEFAULT 1,
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id),  
                FOREIGN KEY(id_categoria) REFERENCES categorias(id)
                )'''
        cursor.execute(criar_tabela_subcategorias)
        bd.commit()
        print('Tabela subcategorias criada com sucesso')
