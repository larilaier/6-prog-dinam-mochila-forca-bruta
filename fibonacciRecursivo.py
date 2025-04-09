import time

# Algoritmo 1: Recursivo puro
def fiboRec(n):
    if n <= 1:
        return n
    else:
        return fiboRec(n-1) + fiboRec(n-2)

# Algoritmo 2: Iterativo
def fiboRec2(n):
    f = [0] * (n + 1)
    f[0] = 0
    if n >= 1:
        f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

# Algoritmo 3: Recursivo com memoização
def lookup_fibo(f, n):
    if f[n] >= 0:
        return f[n]
    if n <= 1:
        f[n] = n
    else:
        f[n] = lookup_fibo(f, n - 1) + lookup_fibo(f, n - 2)
    return f[n]

def memoized_fibo(n):
    f = [-1] * (n + 1)
    return lookup_fibo(f, n)

# Lista de valores a testar
valores = [4, 8, 16, 32]

# Função para testar e medir tempo de execução
def testar_algoritmo(nome, func):
    print(f"\n=== Testando {nome} ===")
    for n in valores:
        inicio = time.time()
        resultado = func(n)
        fim = time.time()
        tempo = fim - inicio
        print(f"{nome}({n}) = {resultado} (tempo: {tempo:.6f} segundos)")

# Execução dos testes
testar_algoritmo("fiboRec", fiboRec)
testar_algoritmo("fiboRec2", fiboRec2)
testar_algoritmo("memoized_fibo", memoized_fibo)