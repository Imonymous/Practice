#!/usr/bin/env python3

def getGraph(arr):
	d = dict()

	rows = len(arr)
	cols = len(arr[0])

	# num_list = [j for row in arr for i in row if i > 0]
	moves = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]

	for i in range(rows):
		for j in range(cols):
			if arr[i][j] >= 0:
				d[arr[i][j]] = [arr[i+move[0]][j+move[1]] for move in moves if i+move[0] >= 0 and i+move[0] < rows and j+move[1] >= 0 and j+move[1] < cols and arr[i+move[0]][j+move[1]] >= 0] 

	return d	

# # Attempt 1, without memoization, exceeds time limits
# def numPhoneNumbers(s, n):
	
# 	table = [None]*(n-1)

# 	digitmap = getGraph([[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]])

# 	table[0] = digitmap[s]

# 	for i in range(1, n-1):
# 		table[i] = []
# 		options = table[i-1]
# 		for option in options:
# 			table[i] += digitmap[option]

# 	return len(table[n-2])

def numPhoneNumbers(s, n):
	
	table = [[0]*(10) for i in range(n)]

	# digitmap = getGraph([[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]])
	digitmap = {1: [6, 8], 2: [9, 7], 3: [4, 8], 4: [9, 3, 0], 5: [], 6: [7, 1, 0], 7: [6, 2], 8: [3, 1], 9: [4, 2], 0: [6, 4]}

	table[0][s] = 1

	for maxlen in range(1, n):
		for digit in range(10):
			for option in digitmap[digit]:
				table[maxlen][digit] += table[maxlen-1][option]

	res = 0
	for digit in range(10):
		res += table[n-1][digit]

	return res

def main():
	start = 4
	length = 6

	count = numPhoneNumbers(start, length)
	print(count)

if __name__ == '__main__':
	main()