
# Equipe: Mauricio, Tiago, Cassio

from biblioteca import Biblioteca

class Livro(Biblioteca):
    def __init__(self, id_livro, titulo, autor, paginas, ano_publicacao, numero_exemplares, aluguel_diario):
        self._id_livro = id_livro
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas
        self._ano_publicacao = ano_publicacao
        self._numero_exemplares = numero_exemplares
        self._aluguel_diario = aluguel_diario


    def cadastrar(self):
        Biblioteca.cadastrar_livro(self._titulo)

    def remover(self):
        Biblioteca.remover_livro(self._titulo)