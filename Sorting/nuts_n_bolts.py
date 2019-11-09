#!/usr/bin/env python3

# Brute force (16/24)
# def nuts_n_bolts(N, B):
# 	out = []
# 	for i in N:
# 		for j in B:
# 			if i == j:
# 				out.append(str(i)+" "+str(j))

# 	return out

# NUTS = [4, 32, 5, 7]
# BOLTS = [32, 7, 5, 4]
# print(nuts_n_bolts(NUTS, BOLTS))

# def solve(N, B): (20/24)
# 	out = []
# 	for i in range(len(N)):
# 		for j in range(i, len(N)):
# 			if N[i] == B[j]:
# 				B[i], B[j] = B[j], B[i]
# 				out.append(str(N[i])+" "+str(B[i]))
# 				break

# 	return out

# This is total BS!
# def solve(nuts, bolts):
# 	out = []
# 	bolts = set(bolts)
# 	for nut in nuts:
# 		if nut in bolts:
# 			out.append(str(nut)+" "+str(nut))
# 	return out

# My attempt after reading editorial:
# Partition nuts pivoted on nuts[0], Partition bolts based on nuts[0].
# Then they pair up at their at appropriate position. Recurse on the partitions.
def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]

def partition_bf(arr, start, end, pivot):

	out = [None]*len(arr)
	lt_count = 0

	for elem in arr[start:end+1]:
		if elem < pivot:
			lt_count += 1

	out[start+lt_count] = pivot

	lt = start
	gt = start+lt_count+1

	for elem in arr[start:end+1]:
		if elem < pivot:
			out[lt] = elem
			lt += 1
		elif elem > pivot:
			out[gt] = elem
			gt += 1

	arr[start:end+1] = out[start:end+1]

	return start+lt_count

def partition(arr, start, end, pivot):
	# Lomuto's
	i = start

	for curr in range(start, end):
		if arr[curr] < pivot:
			swap(arr, i, curr)
			i += 1
		if arr[curr] == pivot:
			swap(arr, curr, end)

	return i

def solve(nuts, bolts):
    #
    # Write your code here.
    #
	out = []
	for i in range(len(nuts)-1, 0, -1):
		pivot = nuts[i]
		# pos = partition_bf(bolts, 0, len(nuts)-1, pivot)
		partition(bolts, 0, i, pivot)
		print(bolts)

	return nuts, bolts

# From editorial
# from random import *
# from itertools import starmap
# def partition_rec(nuts, bolts, low, high):
#     if low >= high:
#         return
#
#     idx = randint(low, high)
#     pivot = partition(nuts, low, high, bolts[idx])
#
#     partition(bolts, low, high, nuts[pivot])
#
#     partition_rec(nuts, bolts, low, pivot-1)
#     partition_rec(nuts, bolts, pivot+1, high)
#
# def swap(a, i, j):
#     a[i], a[j] = a[j], a[i]
#
# def partition(a, low, high, pivot):
#
#     i, j = low, low
#
#     while j < high:
#         if a[j] < pivot:
#             swap(a, i, j)
#             i += 1
#             j += 1
#         elif a[j] == pivot:
#             swap(a, j, high)
#         else:
#             j += 1
#
#     swap(a, high, i)
#     return i
#
# def solve(nuts, bolts):
#     #
#     # Write your code here.
#     #
# 	# Initiate the recursion
# 	partition_rec(nuts, bolts, 0, len(nuts)-1)
#
# 	return list(starmap(lambda i, nut: '%s %s' % (nut, bolts[i]), enumerate(nuts)))

print(solve([3,4,1,2,5],[4,3,5,1,2]))
