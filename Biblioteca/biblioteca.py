
# Equipe: Mauricio, Tiago, Cassio

class Biblioteca():
    def __init__(self):
        self._usuarios = []
        self._senhas = []
        self._livros = []
        self._locados = []


    @property
    def usuarios(self):
        return self._usuarios
    @property
    def senhas(self):
        return self._senhas
    @property
    def livros(self):
        return self._livros
    @property
    def locados(self):
        return self._locados


    #Cadastro de Usuario e remoção
    def cadastrar_usuario(self, usuario, senha):
        self.usuarios.append(usuario)
        self.senhas.append(senha)

    def remover_usuario(self, usuario, senha):
        self.usuarios.remove(usuario)
        self.senhas.remove(senha)


    #Cadastro de Livro e remoção
    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)


    #Metodos 
    def detalhe__do_livros(self, titulo, autor, ano_publicacao, preco):
        print('detalhes do livro: {}\n{}\n{}\n{}',.format(titulo, autor, ano_publicacao, preco))

    def pesquisar_livro(self, livro):
        for livro in self._livros:
            print('livro disponivel')
        else:
            print('livro nao disponivel')

    def registro_de_locacao(self, livro, usuario, senha):
        if usuario in self._usuarios:
            if senha in self._senhas:
                self._locados.append(livro)
            else:
                print('Senha invalida')
        else:
            print('Usuario invalido ou não encontrado')

    def registro_de_devolucao(self, livro, usuario, senha):
        if usuario in self._usuarios:
            if senha in self._senhas:
                self._locados.remove(livro)
            else:
                print('Senha invalida')
        else:
            print('Usuario invalido ou não encontrado')


    def total_livros(self):
        print('Ao todo são {} livros'.format(len(self.livros)))