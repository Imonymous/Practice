#!/usr/bin/env python

def selection_sort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_idx]:
				min_idx = j
		if min_idx != i:
			arr[i], arr[min_idx] = arr[min_idx], arr[i]

	return arr

print selection_sort([2,3,4,9,5,1])