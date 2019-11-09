#!/usr/bin/env python3

import os
import sys

from collections import deque

def get_adj(rows, cols, i, j):
	adj_list = [(i-2, j+1), (i-1, j+2), (i+1, j+2), (i+2, j+1), (i+2, j-1), (i+1, j-2), (i-1,j-2), (i-2, j-1)]

	adj_list = [x for x in adj_list if x[0] in range(0, rows) and x[1] in range(0, cols)]

	return adj_list

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):

	dist = dict()

	if (
		start_row not in range(0, rows) or end_row not in range(0, rows) or
		start_col not in range(0, cols) or end_col not in range(0, cols)
		):
		return 0

	q = deque([(start_row, start_col)])
	visited = {(start_row, start_col)} # THIS NEEDS TO BE A SET, OTHERWISE A LIST (for e.g.) GROWS HUGE FOR REPEATED VISITS TO NODES!!!
	dist[(start_row, start_col)] = 0

	while len(q) > 0:
		curr = q.popleft()

		if curr == (end_row, end_col):
			return dist[curr]

		nbors = get_adj(rows, cols, curr[0], curr[1])
		for i in nbors:
			if i not in visited:
				visited.add(i)
				dist[i] = dist[curr] + 1
				q.append(i)

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
