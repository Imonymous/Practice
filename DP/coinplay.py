#!/usr/bin/env python3

def solve(arr, s, e):

	n = len(arr)
	table = [[0]*(n) for i in range(n)]

	for i in range(n):
		table[i][i] = arr[i]

	for s in range(n-1):
		for e in range(n):
			if s == e-1:
				table[s][e] = max(arr[s], arr[e])

	for s in range(n-3,-1,-1):
		for e in range(s, n):
			table[s][e] = max((arr[s] + min(table[s+2][e], table[s+1][e-1])), (arr[e] + min(table[s+1][e-1], table[s][e-2])))

	return table[0][n-1]

def main():
	arr = [8,15,3,7]
	res = solve(arr, 0, len(arr)-1)

	print(res)

if __name__ == '__main__':
	main()