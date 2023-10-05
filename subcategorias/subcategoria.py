import sistema
from tabulate import tabulate
from bd.bd_subcategorias import Subcategorias
from usuarios.sessao import UsuarioLogado
from categorias.categoria import Categoria

usuario_logado = UsuarioLogado()
subcategoria = Subcategorias()
categoria = Categoria()


class Subcategoria:

    @staticmethod
    def criar():
        nome = sistema.input_obrigatorio("Nome da subcategoria: ")
        categoria.ler()
        id_categoria = sistema.input_obrigatorio("ID da categoria na qual a subcategoria pertence: ")

        subcategoria.criar(nome, id_categoria)


    def excluir(self):
        self.ler()
        id_subcategoria = sistema.input_obrigatorio("Qual o ID da subcategoria que deseja excluir? ")
        subcategoria.excluir(id_subcategoria)

    @staticmethod
    def ler(id_categoria=None):
        sistema.limpar_terminal()
        if not id_categoria:
            id_categoria = sistema.input_obrigatorio("Você gostaria de ler as subcategorias de qual categoria?\n" +
                                                 str(categoria.ler()) + "\n ?")
        subcategorias = subcategoria.ler(id_categoria)

        print("Subcategorias:")
        for sub in subcategorias:
            id_subcategoria, nome = sub
            dados = [
                ["ID da subcategoria", id_subcategoria],
                ["Nome da subcategoria", nome]
            ]
            tabela_formatada = tabulate(dados, tablefmt="grid")
            print(tabela_formatada)
