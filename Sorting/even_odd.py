#!/usr/bin/env python

# Brute force
# def solve(arr):
# 	start = 0
# 	end = len(arr) - 1
# 	out = [None]*len(arr)
# 	for i in arr:
# 		if i % 2 == 0:
# 			out[start] = i
# 			start += 1
# 		else:
# 			out[end] = i
# 			end -= 1
# 	return out

# O(1) space complexity
def solve(arr):
	counter = len(arr)
	for i in range(len(arr)):
		if arr[i] % 2 != 0:
			while(counter > i):
				counter -= 1
				if arr[counter] % 2 == 0:
					break
			arr[i], arr[counter] = arr[counter], arr[i]
	return arr

print(solve([1,2,3,4,5,6,7,8]))