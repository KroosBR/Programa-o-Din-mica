def mochila_dp():
    global valor, peso, N, C, tb

    for i in range(N):
        for j in range(C+1):
            tb[i].append(0)

    for i in range(1, N):
        for c in range(1, C+1):
            if peso[i] <= c:
                tb[i][c] = max(tb[i-1][c - peso[i]] + valor[i], tb[i-1][c])
            else:
                tb[i][c] = tb[i-1][c]

    return tb[N-1][C]

while True:
  try:
    aux1 = [int(i) for i in input().split()]
    aux2 = [int(i) for i in input().split()]
    valor = []
    peso = []
    valor.append(0)
    peso.append(0)
    for i in range(len(aux1)):
            valor.append(aux1[i])
            peso.append(aux2[i])
    C = int(input())
    N = len(valor)
    tb = [[]*101 for i in range(101)]
    capacidade_ult_mochila = mochila_dp()
    print("Para capacidade igual a {}, o valor maximo da mochila é: {}".format(C,capacidade_ult_mochila))
  except EOFError:
      break