
# Equipe: Mauricio, Tiago, Cassio

class Cliente:
    def __init__(self, nome, telefone, endereco):
        self._nome = nome
        self._telefone = telefone
        self._endereco = endereco


    #Get e Setter dos Atributos 
    @property
    def nome(self, nome):
        return self._nome

    @nome.setter
        def nome(self):
            self._nome = nome
    @property
    def telefone(self, telefone):
        return self._telefone

    @telefone.setter
        def telefone(self):
            self._telefone = telefone

    @property
    def endereco(self, endereco):
        return self._endereco

    @endereco.setter
        def endereco(self):
            self._endereco = endereco






class Pedido:
    def __init__(self, numero_pedido, data, hora, cliente, itens, quantidade, situacao_do_pedido):
        self._numero_pedido = numero_pedido
        self._data = data
        self._hora = hora
        self._cliente = cliente
        self._itens = itens
        self._quantidade = quantidade
        self._situacao_do_pedido = situacao_do_pedido

    @property
    def numero_pedido(self, numero_pedido):
        return self._numero_pedido

    @numero_pedido.setter
        def numero_pedido(self):
            self._n_pedido = numero_pedido

    @property
    def data(self, data):
        return self._data

    @data.setter
        def data(self):
            self._data = data

    @property
    def hora(self, hora):
        return self._hora

    @hora.setter
        def hora(self):
            self._hora = hora

    @property
    def cliente(self, cliente):
        return self._cliente

    @cliente.setter
        def cliente(self):
            self._cliente = cliente

    @property
    def itens(self, itens):
        return self._itens

    @itens.setter
        def itens(self):
            self._itens = itens

    @property
    def quantidade(self, quantidade):
        return self._quanti

    @quantidade.setter
        def quantidade(self):
            self._quantidade = quantidade

    @property
    def situacao_do_pedido(self, situacao_do_pedido):
        return self._situacao_do_pedido

    @situacao_do_pedido.setter
        def situacao_do_pedido(self):
        self._situacao_do_pedido= situacao_do_pedido



    #Metodos para a lista de pedidos:Organizar, adicionar, remover quando concluido

    def add_pedidos(self, pedido):
        if isinstance(pedido, pedido):
            self._pedido.append(pedido)

    def remove_pedidos(self, pedido);
        if isinstance(pedido, pedido):
            self._pedido.remove(pedido)

    def organiza(self, key="alfabetica"):
        return self._ordem.sort(key)

    def concluir(self, pedido):
        if isinstance(pedido, pedido):
            self._pedido.remove(pedido)