tb = [-1]*1005

def fib_dp(n):
    global tb
    if n == 0:
        return 0
    if n == 1:
        return 1
    if tb[n] != -1:
        return tb[n]

    tb[n] = (fib_dp(n - 1) + fib_dp(n - 2)) % 1000000007
    return tb[n]


while True:
    try:
        n = int(input())
        f = fib_dp(n)
        print("fib({})= {}".format(n, f))
    except EOFError:
        break

