#!/usr/bin/env python3

import os
import sys

from collections import deque

# def get_adj(rows, cols, i, j):
# 	adj_list = [(i-2, j+1), (i-1, j+2), (i+1, j+2), (i+2, j+1), (i+2, j-1), (i+1, j-2), (i-1,j-2), (i-2, j-1)]

# 	adj_list = [x for x in adj_list if x[0] < rows and x[1] < cols and x[0] >= 0 and x[1] >= 0]

# 	return adj_list

def get_adj(rows, cols, i, j):
	adj_list = []

	if i-2 >= 0 and i-2 < rows and j+1 >= 0 and j+1 < cols:
		adj_list.append((i-2, j+1))
	if i-1 >= 0 and i-1 < rows and j+2 >= 0 and j+2 < cols:
		adj_list.append((i-1, j+2))
	if i+1 >= 0 and i+1 < rows and j+2 >= 0 and j+2 < cols:
		adj_list.append((i+1, j+2))
	if i+2 >= 0 and i+2 < rows and j+1 >= 0 and j+1 < cols:
		adj_list.append((i+2, j+1))
	if i+2 >= 0 and i+2 < rows and j-1 >= 0 and j-1 < cols:
		adj_list.append((i+2, j-1))
	if i+1 >= 0 and i+1 < rows and j-2 >= 0 and j-2 < cols:
		adj_list.append((i+1, j-2))
	if i-1 >= 0 and i-1 < rows and j-2 >= 0 and j-2 < cols:
		adj_list.append((i-1, j-2))
	if i-2 >= 0 and i-2 < rows and j-1 >= 0 and j-1 < cols:
		adj_list.append((i-2, j-1))

	return adj_list

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
	
	visited = []
	dist = dict()

	if (
		start_row >= rows or end_row >= rows or start_col >= cols or end_col >= cols or
		start_row < 0 or end_row < 0 or start_col < 0 or end_col < 0
		):
		return 0

	queue = deque([(start_row, start_col)])
	visited.append((start_row, start_col))
	dist[(start_row, start_col)] = 0

	while (len(queue) > 0):
		curr = queue.popleft()

		if curr == (end_row, end_col):
			return dist[curr]

		nbors = get_adj(rows, cols, curr[0], curr[1])
		for i in nbors:
			if i not in visited:
				visited.append(i)
				dist[i] = dist[curr] + 1
				queue.append(i)

	return -1

if __name__ == "__main__":
    f = sys.stdout

    rows = int(input())

    cols = int(input())

    start_row = int(input())

    start_col = int(input())

    end_row = int(input())

    end_col = int(input())

    res = find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col)

    f.write(str(res) + "\n")

    f.close()