
# Equipe: Mauricio, Tiago, Cassio

from biblioteca import Biblioteca
from livro import Livro

class Locacao(Livro):
    def __init__(id_livro, titulo, autor, paginas, ano_publicacao, numero_exemplares, aluguel_diario,usuario, livro_locado, data_locacao, prazo_devolucao, data_devolucao, multa_atraso):
        super().__init__(id_livro, titulo, autor, paginas, ano_publicacao, numero_exemplares, aluguel_diario)
        self._pendentes = []
        self._usuario = usuario
        self._livro_locado = livro_locado
        self._data_locacao= data_locacao
        self._prazo_devolucao= prazo_devolucao
        self._data_devolucao = data_devolucao
        self._multa_atraso= multa_atraso
        


        if self.npendente():
            print("nao è possivel locar livro pois você esta com pendencias")
            return 0
        if self.sobrando():
            print("nao è possivel locar livro pois nao tem mais exemplares")
            return 0
    

    @property
    def usuario(self):
        return self._usuario

    def pendentes(self, usuario):
        self._pendentes.append(usuario)





    def npendente(self, usuario):
        if usuario in self._pendentes:
            return True
        else:
            return False

    def sobrando(self):
        if self._numero_exemplares == 0:
            return True
        else:
            return False



    def mostrar_detalhes(self):
        Biblioteca.mostrar_detalhes_livros(self._titulo, self._autor, self._ano_publicacao, self._aluguel_diario)