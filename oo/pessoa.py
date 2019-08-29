class Pessoa:

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    p = Pessoa()
    p.nome = 'Renzo'