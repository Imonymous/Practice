#!/usr/bin/env python

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

# Partition nuts pivoted on nuts[0], Partition bolts based on nuts[0]. 
# Then they pair up at their at appropriate position. Recurse on the partitions.
def swap(arr, i, j):
	arr[i], arr[j] == arr[j], arr[i]

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
	
	swap(arr[pivot], arr[end])

	for curr in range(start, end):
		if arr[curr] < arr[end]:
			swap(arr[i], arr[curr])
			i += 1

	swap(arr[i], arr[end])

	return i

def solve(nuts, bolts):
    #
    # Write your code here.
    #
	out = []
	for i in range(len(nuts)):
		pivot = nuts[i]
		print(bolts)
		pos = partition_bf(bolts, 0, len(nuts)-1, pivot)
		out.append((nuts[i], bolts[pos]))

	return out


print(solve([3,4,1,2,5],[4,3,5,1,2]))