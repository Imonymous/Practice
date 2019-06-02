#!/usr/bin/env python

def topological_sort_helper(adj, key, stack, visited):
	visited.append(key)

	if key in adj.keys():
		for neighbor in adj[key]:
			if neighbor not in visited:
				topological_sort_helper(adj, neighbor, stack, visited)

	stack.append(key)

def topological_sort(adj):
	stack = []
	visited = []

	for key in adj.keys():
		if key not in visited:
			topological_sort_helper(adj, key, stack, visited)

	return stack


def build_graph(adj, one, two):
	n = min(len(one), len(two))
	for i in range(n):
		if one[i] == two[i]:
			continue
		else:
			if one[i] not in adj.keys():
				adj[one[i]] = [two[i]]
			elif two[i] not in adj[one[i]] :
				adj[one[i]].append(two[i])
			break

def main(arr):
	adj = dict()

	x = list(set(arr))

	if len(x) > 1:
		for one in arr[:-1]:
			for two in arr[arr.index(one)+1:]:
				build_graph(adj, one, two)

		res = topological_sort(adj)
	else:
		res = arr[0][0]

	print(res[::-1])

if __name__ == '__main__':
	# main(["but", "cat", "card"])
	# main(["baa", "abcd", "abca", "cab", "cad"])
	main(["g","g","g", "g"])