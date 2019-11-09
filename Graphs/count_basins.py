#!/usr/bin/env python3

# Incomplete!

# Tried using DFS - not the right approach
# def get_nbrs(matrix, cell):
#     m = len(matrix)
#     n = len(matrix[0])
#     moves = [[0,-1], [-1,0], [0,1], [1,0]]
#
#     nbrs = []
#
#     for move in moves:
#         if cell[0]+move[0] in range(m) and cell[1]+move[1] in range(n):
#             nbrs.append([cell[0]+move[0], cell[1]+move[1]])
#
#     return nbrs
#
# def check_sink(matrix, cell):
#     nbrs = get_nbrs(matrix, cell)
#     for nbr in nbrs:
#         if matrix[cell[0]][cell[1]] > matrix[nbr[0]][nbr[1]]:
#             return False
#
#     return True
#
# def explore(matrix, cell, visited, comp):
#     visited.append(cell)
#     comp.append(cell)
#     nbrs = get_nbrs(matrix, cell)
#
#     for nbr in nbrs:
#         if nbr not in visited:
#             sink = check_sink(matrix, nbr)
#             print(nbr, sink)
#             if not sink and matrix[cell[0]][cell[1]] < matrix[nbr[0]][nbr[1]]:
#                 explore(matrix, nbr, visited, comp)
#
# def find_basins(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     count = 0
#     visited = []
#     for i in range(m):
#         for j in range(n):
#             cell = [i,j]
#             if cell not in visited:
#                 sink = check_sink(matrix, cell)
#                 if sink:
#                     comp = []
#                     explore(matrix, cell, visited, comp)
#                     print(comp)


def get_sink(matrix, cell, seen, path_so_far):
    m = len(matrix)
    n = len(matrix[0])
    moves = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    path_so_far.append(cell)

    if cell in seen.keys():
        return seen[cell]

    min_nbr_cell_x = cell[0]
    min_nbr_cell_y = cell[1]

    for move in moves:
        if cell[0]+move[0] in range(m) and cell[1]+move[1] in range(n):
            if matrix[cell[0]+move[0]][cell[1]+move[1]] < matrix[min_nbr_cell_x][min_nbr_cell_y]:
                min_nbr_cell_x = cell[0]+move[0]
                min_nbr_cell_y = cell[1]+move[1]

    if matrix[cell[0]][cell[1]] == matrix[min_nbr_cell_x][min_nbr_cell_y]:
        return cell
    else:
        if (min_nbr_cell_x, min_nbr_cell_y) in seen.keys():
            return seen[(min_nbr_cell_x, min_nbr_cell_y)]
        else:
            return get_sink(matrix, (min_nbr_cell_x, min_nbr_cell_y), seen, path_so_far)

def build_graph(matrix, m, n):

    seen = dict()
    for i in range(m):
        for j in range(n):
            if (i,j) not in seen.keys():
                path_so_far = []
                sink = get_sink(matrix, (i,j), seen, path_so_far)

                for item in path_so_far:
                    if item not in seen.keys():
                        seen[item] = sink

    return seen

def find_basins(matrix):
    m = len(matrix)
    n = len(matrix[0])

    seen = build_graph(matrix, m, n)

    ans = []
    count_map = dict()

    for i in seen.values():
        if i in count_map.keys():
            count_map[i] += 1
        else:
            count_map[i] = 1

    return list(sorted(count_map.values()))

print(find_basins([[1,5,2],[2,4,7],[3,6,9]]))
