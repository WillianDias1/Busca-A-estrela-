# Ela calcula quantos passos ainda faltam, ignorando muros e obstáculos, só considerando a distância em linha reta (mas sem diagonal direta).
# A heurística ajuda oao algoritmo a "preferir caminhos que parecem estar indo na direção certa".

def manhattan_heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
