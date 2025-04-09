import time

def mochila_dinamica(pesos, valores, capacidade):
    n = len(pesos)
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    iteracoes = 0

    for i in range(n + 1):
        for w in range(capacidade + 1):
            iteracoes += 1
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade], iteracoes

tamanhos = [4, 8, 16, 32, 128, 1000, 10000]

for n in tamanhos:
    pesos = [(i % 10) + 1 for i in range(n)]
    valores = [(i * 2 % 20) + 1 for i in range(n)]
    capacidade = n * 5

    inicio = time.time()
    resultado, iteracoes = mochila_dinamica(pesos, valores, capacidade)
    fim = time.time()
    tempo = fim - inicio

    print(f"n = {n} | Valor maximo = {resultado} | Iteracoes = {iteracoes} | Tempo = {tempo:.5f} segundos")
