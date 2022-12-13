
# Equipe: Mauricio, Tiago, Cassio

class Agenda:
    def __int__(self, nome, telefone, email, data_de_nascimento, data_criacao):
        self._contatos = []

        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._data_de_nascimento = data_de_nascimento
        self._data_criacao = data_criacao
        

    #Get e Setter dos Atributos 
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def data_de_nascimento(self):
        return self._data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        self._data_de_nascimento = data_de_nascimento




    #Metodos: adicionar, remover, ordenar, pesquisar entre os contatos

    def adicionar_contato(self, nome, telefone, email, data_de_nascimento):
        contato = []
        contato.append(nome)
        contato.append(telefone)
        contato.append(email)
        contato.append(data_de_nascimento)
        return self._contatos.append(contato)


    def pesquisar(self, contato):
        if contato in self._contatos:
            print('{} esta na lista'.format(contato))
        else:
            print('Não esta na lista')


    def ordenar(self, key="alfabetico"):
        return self._contatos.sort(key)


    def remover_contato(self, contato):
        return self._contatos.remove(contato)

    

