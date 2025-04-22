import heapq

# Verifica se uma posição é válida: Quando, grid[x][y] == 0 significa "livre", e 1 seria parede.
def is_valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

# Regra de bloqueio de movimento diagonal quando há parede. Pegando a posição atual e calcula o vizinho 
def can_move_diagonally(grid, curr, dx, dy):
    x, y = curr
    nx, ny = x + dx, y + dy

    # Verifica se ponto destino está livre
    if not is_valid(grid, nx, ny):
        return False

    # Verifica se os dois vizinhos ortogonais estão livres
    if dx != 0 and dy != 0:
        if grid[x + dx][y] == 1 or grid[x][y + dy] == 1:
            return False

    return True

# Função principal
def a_star_search(grid, start, end, heuristic):
    open_set = [] #Fila de prioridade com nós a explorar.
    heapq.heappush(open_set, (0, start)) # Começamos com o nó inicial e custo f=0
    
    # Custo estimado total (G + H)
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    directions = [  # 8 direções
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    while open_set:
        _, current = heapq.heappop(open_set)

        # Verifica se chegou ao destino
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        # Verifica vizinhos, gerando todas as posições vizinhas (ortogonais e diagonais).
        #Verifica se é possivel se ove nas diagonais. 
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if (dx == 0 or dy == 0):  # ortogonal
                    if not is_valid(grid, neighbor[0], neighbor[1]):
                        continue
                else:  # diagonal
                    if not can_move_diagonally(grid, current, dx, dy):
                        continue

                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None
