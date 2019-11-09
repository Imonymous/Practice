from collections import deque

def get_neighbors(cell, lot, numRows, numColumns):

    nbrs = []
    moves = [[0,-1], [-1,0], [0,1], [1,0]]
    for move in moves:
        if cell[0]+move[0] in range(numRows) and cell[1]+move[1] in range(numColumns):
            if lot[cell[0]+move[0]][cell[1]+move[1]] != 0:
                nbrs.append((cell[0]+move[0], cell[1]+move[1]))
    return nbrs

def removeObstacle(numRows, numColumns, lot):
    # WRITE YOUR CODE HERE

    visited = []
    dist = dict()

    start = (0, 0)

    q = deque([start])
    visited.append(start)
    dist[start] = 0

    while q:
        curr = q.popleft()

        if lot[curr[0]][curr[1]] == 9:
            return dist[curr]

        neighbors = get_neighbors(curr, lot, numRows, numColumns)

        for nbor in neighbors:
            if nbor not in visited:
                q.append(nbor)
                visited.append(nbor)
                dist[nbor] = dist[curr] + 1

    return -1

print(removeObstacle(3, 3, [[1,0,0],[1,0,0],[1,9,0]]))
