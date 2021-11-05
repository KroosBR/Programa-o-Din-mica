def moedas_dp(i):
    global tb, moedas, N
    if i > N:
        return 0
    if tb[i] != -1:
        return tb[i]

    tb[i] = max(moedas_dp(i + 1), moedas[i] + moedas_dp(i + 2)) # (caso quando não pega moeda, caso quando pega moeda)
    return tb[i]

while True:
    try:
        tb = [-1]*1005
        moedas = [int(i) for i in input().split()] 
        N = len(moedas) - 1 
        i = int(input())
        maior = moedas_dp(i)
        print("Maior valor possivel para o indice[{}]: {}".format(i,maior))
    except EOFError:
        break