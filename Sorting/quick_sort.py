#!/usr/bin/env python

def choose_pivot(arr, start, end):
	return start

def partition_bf(arr, start, end, pivot):

	out = [None]*len(arr)

	le_count = 0

	for i in arr[start:end+1]:
		if i < arr[pivot]:
			le_count += 1

	out[start+le_count] = arr[pivot]

	lt = start
	gt = start+le_count+1

	for j in range(start, end+1):
		if arr[j] < arr[pivot]:
			out[lt] = arr[j]
			lt += 1
		elif arr[j] > arr[pivot]:
			out[gt] = arr[j]
			gt += 1

	arr[start:end+1] = out[start:end+1]

	return start+le_count

def swap(a, b):
	a, b = b, a

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

def quick_sort(arr, start, end):

	if start >= end:
		return

	if start < end:
		
		pivot = choose_pivot(arr, start, end)

		idx = partition_bf(arr, start, end, pivot)

		quick_sort(arr, start, idx-1)
		quick_sort(arr, idx+1, end)

def main():
	a = [18,2,11,7,12,45,6,9,3,4,5,1]
	quick_sort(a, 0, len(a) - 1)
	print(a)
	

if __name__ == '__main__':
	main()
