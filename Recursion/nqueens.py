#!/usr/bin/python

import sys
import os

def checkDiagonals(a, row, col):

	for i in range(row):
		row_diff = row - i
		col_diff = col - a[i]
		if abs(row_diff) == abs(col_diff):
			return False

	return True

def isValid(a, row, col):

	if col not in a.values():
		if checkDiagonals(a, row, col):
			return True

	return False

def recursivePrintQueens(a, row, ans, res):
	N = len(a)
	if row == N:
		return 
 
	for col in range(N):
		if isValid(a, row, col):
			a[row] = col
			row_str = ['-']*N
			row_str[col] = 'q'
			# print("Coords: {row_name}, {col_name}".format(row_name=row, col_name=col))
			ans.append(row_str)
			recursivePrintQueens(a, row+1, ans, res)
			if len(ans) == N:
				temp = ans.copy()
				res.append(temp)
				if a[row] is not None:
					a[row] = None
				if len(ans) > 0:
					del ans[-1]

	if a[row] is not None:
		a[row] = None

	if len(ans) > 0:
		del ans[-1]


def nQueensMain(N):
	ans = []
	res = []
	a = dict()
	for i in range(N):
		a[i] = None
	recursivePrintQueens(a, 0, ans, res)

	for i in range(len(res)):
		for j in range(len(res[i])):
			res[i][j] = "".join(res[i][j])

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
