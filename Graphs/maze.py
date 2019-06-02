#!/usr/bin/env python3

import sys
import os

from collections import deque

def find_mark(grid, mark):

	height = len(grid)
	width = len(grid[0])

	for row in range(height):
		for col in range(width):
			if grid[row][col] == mark:
				return (row, col)

def get_neighbors(coords, height, width):
	row = coords[0]
	col = coords[1]

	neighbors = []

	if row - 1 >= 0:
		neighbors.append((row-1, col))
	if row + 1 < height:
		neighbors.append((row+1, col))
	if col - 1 >= 0:
		neighbors.append((row, col-1))
	if col + 1 < width:
		neighbors.append((row, col+1))

	return neighbors

def build_path(prev, last):

	res = []
	i = last

	while prev[i] is not None:
		res.append(i)
		i = prev[i]

	res.append(i) # Add the start
	res.reverse()
	return res

def check_path(prev, curr, key_tuple):
	path = build_path(prev, curr)
	print(path)
	print(key_tuple)
	if key_tuple in path:
		return True
	else:
		return False


def fsp_sub(grid, start, stop):

	visited = []
	keys = dict()
	prev = dict()

	height = len(grid)
	width = len(grid[0])

	start = find_mark(grid, start)

	q = deque([start])
	prev[start] = None
	visited.append(start)

	while len(q) > 0:

		curr = q.popleft()

		curr_mark = grid[curr[0]][curr[1]]
		if curr_mark == '+':
			path = build_path(prev, curr)
			print(path)
			return path

		neighbors = get_neighbors(curr, height, width)

		for i in neighbors:
			if i not in visited:
				mark = grid[i[0]][i[1]]
				if mark == '#':
					visited.append(i)
					continue

				if mark == '.':
					q.append(i)
					prev[i] = curr
					visited.append(i)
				elif mark.isalpha():
					if mark.isupper():
						print("Found a door %s" % mark)
						if mark.lower() in keys.keys() and check_path(prev, curr, keys[mark.lower()]):
							q.append(i)
							prev[i] = curr
							visited.append(i)
						else:
							visited.append(i)
							continue
					else:
						print("Added a key %s" % mark)
						keys[mark] = (i[0], i[1])
						q.append(i)
						prev[i] = curr
						visited.append(i)
						break
				else:
					if mark == '+':
						prev[i] = curr
						visited.append(i)
						path = build_path(prev, i)
						return path
					else:
						print("Unexpected mark!")

def find_shortest_path(grid):
	path = fsp_sub(grid, '@', '+')
	return path

if __name__ == "__main__":
    f = sys.stdout

    grid_cnt = 0
    grid_cnt = int(input())
    grid_i = 0
    grid = []
    while grid_i < grid_cnt:
        try:
            grid_item = str(input())
        except:
            grid_item = None
        grid.append(grid_item)
        grid_i += 1


    res = find_shortest_path(grid);
    for res_x in res:
        for res_y in res_x:
            f.write(str(res_y) + " ")
        f.write("\n")


    f.close()
