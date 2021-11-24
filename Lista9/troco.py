'''
PROBLEMA
2446: Troco

NOME - MATRICULA
Isaac Portela da Silva - 20192004900
Mateus Leal Sobreira - 20192020340
Mayara do Carmo Mendes - 20192004768

DESCRICAO
E usada programação dinâmica para resolver o problema, de modo que temos o vetor "tb" que ira memorizar as soluções dos subproblemas necessário para a resolução do
problema atual. Para solucionar problema, primeiro definimos a resposta base, que será primeira posição da tabela "tb" que estará iniciado com o valor 1 diferentes das
outras posições que terão valor iniciado igual a -1.
Esta resposta base e utilizada na função troco que recebera como parâmetro o valor da compra e a lista com as moedas. Primeiro verificamos se para o respectivo valor de
entrada já temos armazenado na tabela de memorização a resposta se é possível pagar este valor utilizando as apenas suas moedas. Caso contrario é percorrida uma faixa de
valores entre o preço total e o valor da moeda, no qual é buscado na tabela se algum endereço desta faixa no vetor tb, está com valor 1, positivo
para subtração do valor total pelo valor da moeda, atribuímos ao valor acumulado da "soma" das moedas e depois percorrida todos os valores e da moeda e suas respectivas faixas
como no processo dito anteriormente. Retornamos o valor de índice igual ao valor final da compra. Onde se este estiver com o valor igual a 1 ele a possível pagar o valor exato da conta.
Caso esteja ainda com o valor padrão de -1 não possível ser feito o pagamento com as moedas.
'''


def troco(valor_compra, moedas):
    global tb
    if tb[valor_compra] != -1:
        return tb[valor_compra]

    for valor in moedas:
        aux = valor_compra
        while aux >= valor:
            if tb[aux - valor] == 1:
                tb[aux] = 1
            aux = aux - 1
    return tb[valor_compra]


entrada = list(map(int, input().split()))
moedas = list(map(int, input().split()))
valor_compra, qtd_moedas = entrada
tb = [-1]*10007
tb[0] = 1   # caso base

resposta = troco(valor_compra, moedas)

if resposta == 1:
    print('S')
else:
    print('N')

