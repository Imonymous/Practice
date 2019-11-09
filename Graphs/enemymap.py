'''
n * n matrix

enemies
walls

up down left right, until hits the wall or end

[[1,1,0],
 [1,0,0],
 [-1,-1,-1]]

'''
# Proper attempt
# def find_max_enemies(arr):
#
#     dp_table = [[None]*len(arr) for i in range(len(arr[0]))]

# Interview attempt
def count_ones(arr, i, j, m, direction):

    if direction == 0:
        row_count = 0

        left = i
        while left >= 0 and arr[left][j] != -1:
            if (left, j, 0) in m.keys():
                return m[(left, j, 0)]

            if arr[left][j] == 1:
                row_count += 1
            left -= 1

        right = i
        while right < len(arr[0]) and arr[right][j] != -1:
            if (right, j, 0) in m.keys():
                return m[(right, j, 0)]
            if arr[right][j] == 1:
                row_count += 1
            right += 1

        m[(i, j, 0)] = row_count

        return row_count

    else:
        col_count = 0

        up = j
        while up >= 0 and arr[i][up] != -1:
            if (i, up, 1) in m.keys():
                return m[(i, up, 1)]

            if arr[i][up] == 1:
                col_count += 1
            up -= 1


        down = j
        while down < len(arr) and arr[i][down] != -1:
            if (i, down, 1) in m.keys():
                return m[(i, down, 1)]
            if arr[i][down] == 1:
                col_count += 1
            down += 1

        m[(i, j, 1)] = col_count

        return col_count

    return 0

def max_enemies(arr):

    m = dict()

    max_so_far = 0

    for i in range(len(arr[0])):
        for j in range(len(arr)):

            if arr[i][j] == 0:
                enemy_count_rows = count_ones(arr, i, j, m, 0)
                enemy_count_cols = count_ones(arr, i, j, m, 1)
                total = enemy_count_rows + enemy_count_cols
                if total > max_so_far:
                    max_so_far = total

    return max_so_far

arr = [[1,0,0,1],
 [-1,0,-1,0],
 [1,1,1,0],
 [-1,-1,-1,-1]]

print(max_enemies(arr))
