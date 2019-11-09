#!/usr/bin/env python3

def largest_sub_square_matrix(n, m, mat):

    table = [[None]*(m+1) for _ in range(n+1)]
    
    for i in range(n,-1,-1):
        for j in range(m,-1,-1):
            table[i][j] = (0, 0)

    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if mat[i][j]:
                if table[i][j+1][0] and table[i+1][j+1][0] and table[i+1][j][0]:
                    if table[i][j+1][0] == table[i+1][j+1][0] and table[i+1][j][0] == table[i+1][j+1][0]:
                        table[i][j] = (1+table[i+1][j+1][0], max(1+table[i+1][j+1][0], table[i][j+1][1], table[i+1][j+1][1], table[i+1][j][1]))
                    else:
                        table[i][j] = (1+min(table[i][j+1][0], table[i+1][j+1][0], table[i+1][j][0]), max(table[i][j+1][1], table[i+1][j+1][1], table[i+1][j][1]))
                else:
                    table[i][j] = (1, max(1, table[i][j+1][1], table[i+1][j+1][1], table[i+1][j][1]))
            else:
                table[i][j] = (0, max(table[i][j+1][1], table[i+1][j+1][1], table[i+1][j][1]))

    return table[0][0][1]

res = largest_sub_square_matrix(4,6,[[1,1,1,0,1,1],[1,1,1,0,1,1],[1,1,0,0,1,1],[1,1,0,0,0,0]])

print(res)