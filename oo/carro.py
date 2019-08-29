"""Criar uma classe carro que deve possuir dois atributos compostos por outras duas classes:

1) motor
2) direção

O motor terá a respnsabilidade de controlar a velocidade.
ele fornece os seguintes atributos:
1) atributo de dado velocidade
2) metodo acelerar, que deverar incrementar a velocidade em uma unidade
3) metodo frear que devera decrementar a velocidade em 2 unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:

1) valor de direção com valores possiveis: Norte, Sul, Leste, Oeste.
2) Metodo girar_a_direita
3) Metodo girar_a_esquerda
 N
O L
 S

     Exemplo:
     >>> motor = Motor()
     >>> motor.velocidade
     0
     >>> motor.acelerar()
     1
     >>> motor.acelerar()
     2
     >>> motor.acelerar()
     3
     >>> motor.frear()
     1
     >>> motor.frear()
     0

     # testando direção
     >>> direcao = Direcao()
     >>> direcao.valor
     'NORTE'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'LESTE'
     >>> direcao.girar_a_direita()
     >>> direcao.valor
     'SUL'


     # testando carro
     >>> carro = Carro(direcao, motor)
     >>> carro.calcular_velocidade()
     0
     >>> carro.acelerar()
     1
     >>> carro.calcular_velocidade()
     1
"""


class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1
        print (self.velocidade)

    def frear(self):
        self.velocidade -= 2

        if self.velocidade < 0:
            self.velocidade = 0
        print(self.velocidade)


NORTE = 'NORTE'
SUL = 'SUL'
LESTE = 'LESTE'
OESTE = 'OESTE'

class Direcao:

    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}

    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self, valor=NORTE):
        self.valor = valor

    def girar_a_direita(self):

        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct_dct[self.valor]


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()


if __name__ == '__main__':
    direcao = Direcao()
    motor = Motor()

    carro = Carro(direcao, motor)
