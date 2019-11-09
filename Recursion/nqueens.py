#!/usr/bin/env python3

import sys
import os

def checkDiagonals(a, row, col):

    for i in range(row):
        row_diff = row - i
        col_diff = col - a[i]
        if abs(row_diff) == abs(col_diff):
            return False

    return True

# def isValid(a, row, col):
#
# 	if col not in a.values():
# 		if checkDiagonals(a, row, col):
# 			return True
#
# 	return False

# Attempt 1
# def recursivePrintQueens(a, row, ans, res):
# 	N = len(a)
# 	if row == N:
# 		return
#
# 	for col in range(N):
# 		if isValid(a, row, col):
# 			a[row] = col
# 			row_str = ['-']*N
# 			row_str[col] = 'q'
# 			# print("Coords: {row_name}, {col_name}".format(row_name=row, col_name=col))
# 			ans.append(row_str)
# 			recursivePrintQueens(a, row+1, ans, res)
# 			if len(ans) == N:
# 				temp = ans.copy()
# 				res.append(temp)
# 				if a[row] is not None:
# 					a[row] = None
# 				if len(ans) > 0:
# 					del ans[-1]
#
# 	if a[row] is not None:
# 		a[row] = None
#
# 	if len(ans) > 0:
# 		del ans[-1]
#
# def nQueensMain(N):
# 	ans = []
# 	res = []
# 	a = dict()
# 	for i in range(N):
# 		a[i] = None
# 	recursivePrintQueens(a, 0, ans, res)
#
# 	for i in range(len(res)):
# 		for j in range(len(res[i])):
# 			res[i][j] = "".join(res[i][j])
#
# 	return res

# This O(N)
# def isValid(a, row, col):
#
#     if col not in a or row is None:
#         if checkDiagonals(a, row, col):
#             return True
#
#     return False

# This is O(1)
def isValid(row, col, col_occupied, slash_occupied, back_slash_occupied):
    return not (col_occupied[col] or slash_occupied[row+col] or back_slash_occupied[row-col+n-1])

def recursivePrintQueens(a, row, ans, res, n, col_occupied, slash_occupied, back_slash_occupied):
    if row == n:
        ans_str = []
        for i in range(n):
            tmp = []
            for j in range(n):
                 tmp += ans[i][j]
            ans_str.append("".join(tmp))

        res.append(ans_str)
        return

    for col in range(n):
        if isValid(row, col, col_occupied, slash_occupied, back_slash_occupied):
            a[row] = col
            ans[row][col] = 'q'
            col_occupied[col] = True
            slash_occupied[row+col] = True
            back_slash_occupied[row-col+n-1] = True
            recursivePrintQueens(a, row+1, ans, res, n, col_occupied, slash_occupied, back_slash_occupied)
            ans[row][col] = '-'
            a[row] = None
            col_occupied[col] = False
            slash_occupied[row+col] = False
            back_slash_occupied[row-col+n-1] = False

def nQueensMain(n):
    ans = [['-']*n for _ in range(n)]
    res = []
    a = [None]*n
    col_occupied = [False]*n
    slash_occupied = [False]*(2*n-1)
    back_slash_occupied = [False]*(2*n-1)
    recursivePrintQueens(a, 0, ans, res, n, col_occupied, slash_occupied, back_slash_occupied)

    return res

if __name__ == "__main__":
    f = sys.stdout

    n = int(input())

    res = nQueensMain(n);
    for res_x in res:
        for res_y in res_x:
            f.write(str(res_y) + " ")
        f.write("\n")

    f.close()
