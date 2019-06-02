#!/usr/bin/env python3

def ldist(word1, word2):
	m = len(word1)
	n = len(word2)

	table = [[None]*(n+1) for i in range(m+1)]

	for i in range(m+1):
		table[i][n] = m - i

	for j in range(n+1):
		table[m][j] = n - j

	for i in range(m-1, -1, -1):
		for j in range(n-1, -1, -1):
			if word1[i] == word2[j]:
				table[i][j] = table[i+1][j+1]
			else:
				table[i][j] = 1 + min(table[i+1][j], table[i][j+1], table[i+1][j+1])

	return table[0][0]

def main():
	ans = ldist("kitten", "sitting")

	print(ans)

if __name__ == '__main__':
	main()