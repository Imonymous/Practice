#!/usr/bin/env python

# Brute force
# def three_sum(arr):
# 	for i in arr:
# 		for j in arr:
# 			for k in arr:
# 				if k == (i + j)*(-1):
# 					print(i, j, k)

import os
import sys

def findZeroSum(arr):
	unique_set = set()
	for i in range(len(arr)-1):
		for j in range(i+1, len(arr)):
			target = -1*(arr[i]+arr[j])
			try:
				idx = arr.index(target)	
				if idx != i and idx != j:
					unique_set.add(tuple(sorted(arr[i], arr[j], target)))
			except ValueError:
				idx = -1
	out = []
	for u in unique_set:
		out.append(str(u)[1:-1])

	return out

# print(three_sum([1,2,3,4,5,6,7,8,-9,-11,-13,-17]))

if __name__ == "__main__":
    f = sys.stdout

    arr_size = int(input())

    arr = []
    for _ in range(arr_size):
        arr_item = int(input())
        arr.append(arr_item)

    res = findZeroSum(arr)

    f.write("\n".join(res))

    f.write('\n')

    f.close()