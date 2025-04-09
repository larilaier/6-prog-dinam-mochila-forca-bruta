from itertools import combinations

# Definição dos itens como tuplas: (nome, peso, valor)
itens = [
    ("A", 2, 3),
    ("B", 3, 4),
    ("C", 4, 5),
    ("D", 5, 8)
]

capacidade = 5
num_iteracoes = 0  # contador global de iterações

def mochila_forca_bruta(itens, capacidade):
    global num_iteracoes
    melhor_valor = 0
    melhor_comb = []

    # Gerar todas as combinações possíveis (2^n)
    for i in range(1, len(itens)+1):
        for combinacao in combinations(itens, i):
            num_iteracoes += 1
            peso_total = sum(item[1] for item in combinacao)
            valor_total = sum(item[2] for item in combinacao)

            if peso_total <= capacidade and valor_total > melhor_valor:
                melhor_valor = valor_total
                melhor_comb = combinacao

    return melhor_comb, melhor_valor

# Executar o teste
solucao, valor_max = mochila_forca_bruta(itens, capacidade)

# Mostrar resultados
print("\nMelhor combinacao:")
for item in solucao:
    print(f"Item {item[0]} (peso {item[1]}, valor {item[2]})")

print(f"Valor total: {valor_max}")
print(f"Numero de combinacoes testadas: {num_iteracoes}")