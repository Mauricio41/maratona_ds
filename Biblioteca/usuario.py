
# Equipe: Mauricio, Tiago, Cassio

from biblioteca import Biblioteca

class Usuario(Biblioteca):
    def __init__(self, nome, email, nome_de_usuario, senha):
        self._nome = nome
        self._email = email
        self._nome_de_usuario = nome_de_usuario
        self._senha = senha




    def adiciocar_usuario(self):
        Biblioteca.cadastrar_usuario(self._nome, self._senha)

    def remover_usuario(self):
        Biblioteca.remover_usuario(self._nome, self._senha)
