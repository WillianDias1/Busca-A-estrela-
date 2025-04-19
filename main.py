import matplotlib.pyplot as plt
import numpy as np
from a_star import a_star_search
from heuristics import manhattan_heuristic

# Mapa com 0 (livre) e 1 (parede)
color_map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0],
    [1,1,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0],
    [1,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0],
    [1,0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0],
    [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
    [1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0],
    [1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
    [1,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1],
    [0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,1],
    [0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,1],
    [0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1],
    [0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0],
    [0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0],
    [0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
]

numbers = np.arange(1, 442).reshape((21, 21))

colors = {
    1: '#0066FF',
    0: '#FFE30C',
}

start_num = int(input("Digite o ponto inicial (1-441): "))
end_num = int(input("Digite o ponto final (1-441): "))

start = ((start_num - 1) // 21, (start_num - 1) % 21)
end = ((end_num - 1) // 21, (end_num - 1) % 21)

if color_map[start[0]][start[1]] == 1 or color_map[end[0]][end[1]] == 1:
    print("Início ou fim é uma parede. Escolha outro ponto.")
    exit()

from a_star import a_star_search
from heuristics import manhattan_heuristic

path = a_star_search(color_map, start, end, manhattan_heuristic)

if not path:
    print("Não foi possível encontrar um caminho entre os pontos informados.")
else:
    print("Caminho encontrado:")
    print([(x * 21 + y + 1) for x, y in path])

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_axis_off()

    cell_colors = [[colors[color_map[i][j]] for j in range(21)] for i in range(21)]

    for (i, j) in path:
        cell_colors[i][j] = '#FF5733'

    table = plt.table(
        cellText=numbers,
        cellLoc='center',
        loc='center',
        cellColours=cell_colors,
    )

    for i in range(21):
        for j in range(21):
            cell = table[i, j]
            cell.set_height(1/21)
            cell.set_width(1/21)
            cell.set_edgecolor('black')
            cell.set_fontsize(10)

    plt.title("Caminho Encontrado com A*", fontsize=16)
    plt.show()
