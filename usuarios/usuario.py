from contas.menu_conta import criar_conta
from bd.bd_usuario import UsuarioBD
from usuarios.sessao import UsuarioLogado
from despesas.menu_despesas import menu_despesas
from contas.conta import Conta
from bd.conexao_bd import conectar_bd

bd, cursor, error_bd = conectar_bd()
usuarios = UsuarioBD()
usuario_logado = UsuarioLogado()
dados_conta = Conta()


class Usuarios:
    @staticmethod
    def exibir_informacoes():
        print("Olá, ", usuario_logado.nome)
        dados_conta.informacoes()

    @staticmethod
    def logar():
        usuario = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        usuarios.verificar_login(usuario, senha)
        if usuario_logado.id is not None:
            criar_conta()
            Usuarios.exibir_informacoes()



        else:
            print("Email ou senha inválidos")

    @staticmethod
    def cadastrar():
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        usuarios.criar(nome, email, senha)

    @staticmethod
    def excluir():
        del_usuario = input("Digite o id do usuario que deseja excluir: ")
        usuarios.excluir(del_usuario)

    @staticmethod
    def consultar():
        usuarios_cadastrados = usuarios.consultar()
        for usuario in usuarios_cadastrados:
            print(usuario)
