#ex 5

import time
from itertools import combinations

def mochila_bruta(itens, capacidade):
    melhor_valor = 0
    melhor_comb = []
    iteracoes = 0

    for i in range(1, len(itens) + 1):
        for combinacao in combinations(itens, i):
            iteracoes += 1
            peso_total = sum(item[1] for item in combinacao)
            valor_total = sum(item[2] for item in combinacao)
            if peso_total <= capacidade and valor_total > melhor_valor:
                melhor_valor = valor_total
                melhor_comb = combinacao

    return melhor_valor, iteracoes

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

    print(f"n = {n}")

    if n <= 16:
        itens = [(f"I{i}", pesos[i], valores[i]) for i in range(n)]
        start = time.time()
        valor_bruta, iter_bruta = mochila_bruta(itens, capacidade)
        end = time.time()
        tempo_bruta = end - start
        print(f"Bruta ->     Valor: {valor_bruta} | Iteracoes: {iter_bruta} | Tempo: {tempo_bruta:.5f} s")
    else:
        print(f"Bruta ->     nao testado (muito lento)")

    start = time.time()
    valor_pd, iter_pd = mochila_dinamica(pesos, valores, capacidade)
    end = time.time()
    tempo_pd = end - start
    print(f"Dinamica ->     Valor: {valor_pd} | Iteracoes: {iter_pd} | Tempo: {tempo_pd:.5f} s\n")
