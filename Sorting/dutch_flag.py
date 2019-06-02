#!/usr//bin/env python3

def swap(arr, a, b):
	arr[a], arr[b] = arr[b], arr[a]

def dutch_partition(arr, lo, hi): 
	# Hoare's
	i = lo
	j = lo
	k = hi

	pivot = arr[lo]

	while j <= k:
		if arr[j] < pivot:
			swap(arr, i, j)
			i += 1
			j += 1
		elif arr[j] == pivot:
			j += 1
		elif arr[j] > pivot:
			swap(arr, j, k)
			k -= 1
	
	return i, j

def quick_sort(arr, start, end):

	if start >= end:
		return

	if start < end:

		p_lo, p_hi = dutch_partition(arr, start, end)

		quick_sort(arr, start, p_lo-1)
		quick_sort(arr, p_hi, end)


arr = [1,3,4,3,5,6,3,9,8,6,3,5,1,3,4,5,6]

quick_sort(arr, 0, len(arr)-1)

print(arr)
