import sistema
from tabulate import tabulate
from bd.bd_categorias import CategoriasBD
from usuarios.sessao import UsuarioLogado

usuario_logado = UsuarioLogado()
categoria = CategoriasBD()


class Categoria:

    @staticmethod
    def criar():
        nome = sistema.input_obrigatorio("Nome da categoria: ")
        categoria.criar(nome)

    def excluir(self):
        self.ler()
        id_categoria = sistema.input_obrigatorio("Qual o ID da categoria que deseja excluir? ")
        categoria.excluir(id_categoria)

    @staticmethod
    def ler():
        categorias = categoria.ler()

        print("Categorias:")
        for cat in categorias:
            id_categoria, nome = cat
            dados = [
                ["ID da categoria", id_categoria],
                ["Nome da categoria", nome]
            ]
            tabela_formatada = tabulate(dados, tablefmt="grid")
            print(tabela_formatada)
