'''
PROBLEMA
1166: Torre de Hanoi, novamente!

NOME - MATRICULA
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768

DESCRICAO
E usada programacao dinamica para resolver o problema. A funcao contaBolas recebe
como parametro o numero da haste e o valor da bola.
* Se a posicao da haste e igual a quantidade maxima de hastes (num_hastes), essa
haste nao existe (a contagem comeca do zero) e e retornado zero.
* Se o valor da haste no jogo e igual a zero, essa haste nao recebeu nenhuma bola
e a bola atual e colocada nela. Entao a proxima bola e passada por parametro.
* Se nenhum dos casos acima e verdadeiro, e feita uma busca nas hastes para ver em
qual a bola pode ficar. Para verificar se a soma da bola atual com a ultima bola da
haste, e usada a funcao quadradoPerfeito. No fim da busca, a proxima bola e passada
por parametro.

'''

import math
import sys

sys.setrecursionlimit(1500)  # evitar estouro de pilha

quant_bolas = 0


def quadradoPerfeito(num):
    return num == int(math.sqrt(num) + 0.5) ** 2  # transformar o resultado da raiz em inteiro para comparar


def contaBolas(valor, haste):
    global quant_bolas

    if haste == num_hastes:  # verifica se o numero de hastes ultrapassa o valor maximo
        haste = 0
        return 0

    if jogo[haste] == 0:  # caso ainda nao foi colocada nenhuma bola na haste

        jogo[haste] = valor
        quant_bolas += 1

        return contaBolas(valor + 1, haste)

    else:
        for i in range(haste + 1):  # procura uma haste para colocar a bola
            if quadradoPerfeito(jogo[i] + valor):
                jogo[i] = valor
                quant_bolas += 1

                return contaBolas(valor + 1, haste)

        contaBolas(valor, haste + 1)  # usar uma nova haste


casos = int(input())

for i in range(casos):
    jogo = [0 for j in range(51)]

    num_hastes = int(input())

    quant_bolas = 0

    contaBolas(1, 0)

    print(quant_bolas)