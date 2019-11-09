#!/usr/bin/env python3
from collections import deque

def get_nbrs(grid, i, j):

    m = len(grid)
    n = len(grid[0])

    moves = [[1,0],[0,1],[-1,0],[0,-1]]

    nbrs = []
    for move in moves:
        if i+move[0] in range(m) and j+move[1] in range(n):
            nbrs.append((i+move[0], j+move[1]))

    return nbrs

def fill_path(prev, target, out):
    dist = 0

    cell = target
    out[cell[0]][cell[1]] = dist
    while prev[cell] is not None:
        dist += 1
        cell = prev[cell]
        if out[cell[0]][cell[1]] is None:
            out[cell[0]][cell[1]] = dist

    dist += 1
    if out[cell[0]][cell[1]] is None:
        out[cell[0]][cell[1]] = dist


def bfs(grid, i, j, out):

    visited = []
    prev = dict()
    curr = (i, j)
    visited.append(curr)
    q = deque([curr])
    prev[curr] = None

    while len(q) > 0:
        curr = q.popleft()
        if grid[curr[0]][curr[1]] == "G":
            fill_path(prev, curr, out)
            return

        nbrs = get_nbrs(grid, curr[0], curr[1])
        for nbr in nbrs:
            if grid[nbr[0]][nbr[1]] == "W":
                continue
            if nbr not in visited:
                visited.append(nbr)
                q.append(nbr)
                prev[nbr] = curr

    out[i][j] = -1

def find_shortest_distance_from_a_guard(grid):

    if grid is None:
        return

    m = len(grid)
    n = len(grid[0])

    out = [[None]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if out[i][j] is None:
                if grid[i][j] == "W":
                    out[i][j] = -1

                if grid[i][j] == "G":
                    out[i][j] = 0

                if grid[i][j] == "O":
                    bfs(grid, i, j, out)

    print(out)
    return out


# grid = ["GWOWG"]
# grid = ["OOOOG", "OWWOO", "OOOWO", "GWWWO", "OOOOG"]
grid = ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"]
find_shortest_distance_from_a_guard(grid)
