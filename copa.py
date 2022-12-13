
# Equipe: Mauricio, Tiago, Cassio


from random import random

class Copa:
    def __init__(self, pais, numero_jogadores, nota):
        self._pais = pais
        self._numero_jogadores = numero_jogadores
        self._nota = nota



    #Get e Setter dos Atributos 
    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, pais):
        self._pais = pais

    @property
    def numero_jogadores(self):
        return self._numero_jogadores

    @numero_jogadores.setter
    def numero_jogadores(self, numero_jogadores):
        self._numero_jogadores = numero_jogadores

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota



#Comparando a nota dos times para a escolha
    def compara_nota(self, nota_t1, nota_t2):
        point_t1 = nota_t1 * 0.05
        point_t1 = nota_t2 * 0.05

        if point_t1 < point_t1:
            nota_t1 += 1
            n = sorted(0, 1)
            
            
            if n == 0:
                nota_t1 += 1
                return nota_t1

        elif point_t1 < point_t1:
            nota_t2 += 1
            n = sorted(0, 1)
            
            if n == 1:
                nota_t2 += 1
                return nota_t2

        else:
            