#!/usr/bin/env python
import heapq
def first_k(arr, k):
	output = []
	unique = list(set(arr))

	if len(unique) < k:
		return unique

	heapq._heapify_max(unique)

	while(len(output) < k):
		x = heapq._heappop_max(unique)
		if x is None:
			break
		else:
			output.append(x)
	return list(output)

print(first_k([4,5,6,7,2,5,9,89,78,67], 6))