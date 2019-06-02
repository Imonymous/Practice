#!/usr/bin/env python

def merge(arr, start, mid, end):
	n1 = mid - start + 1
	n2 = end - mid

	L = []
	R = []

	for i in range(start, end+1):
		if i <= mid:
			L.append(arr[i])
		else:
			R.append(arr[i])

	i = 0 # track the Left array
	j = 0 # track the Right array
	k = start # track the output array

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
			k += 1
		else:
			arr[k] = R[j]
			j += 1
			k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def merge_sort(arr, start, end):
	if start >= end:
		return

	mid = start + (end - start)//2

	merge_sort(arr, start, mid)

	merge_sort(arr, mid+1, end)

	merge(arr, start, mid, end)

	return arr

print(merge_sort([2,3,4,9,5,1], 0, 5))