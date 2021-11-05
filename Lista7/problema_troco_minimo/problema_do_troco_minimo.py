import math
def trocominimo_dp(k):
    global tabela, valores, N
    if k == 0:
        return 0
    if tabela[k] != -1:
        return tabela[k]

    melhor = 1e9

    for i in range(N):
        if valores[i] <= k:
            melhor = min(melhor, 1 + trocominimo_dp(k - valores[i]))

    tabela[k] = melhor
    return tabela[k]

while True:
    try:
        valores = [int(i) for i in input().split()]
        N = len(valores)
        tabela = [-1]*1005

        k = int(input())
        troco_minimo = trocominimo_dp(k)
        if troco_minimo!= 1e9:
            print("Precisamos de no minimo {} moedas para R${} de troco.".format(troco_minimo, k))
        else:
            print("E impossivel calcular o numero minimo de moedas para R${} de troco!".format(k))
    except EOFError:
        break