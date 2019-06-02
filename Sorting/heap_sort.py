#!/usr/bin/env python
#Note: this is a MIN heap, comments point to analogous steps to build a MAX heap

def heapify(arr, n, i):

	# For MAX heap replace smallest by largest and > by <

	smallest = i
	l = 2*i+1
	r = 2*i+2

	if l < n and arr[smallest] > arr[l]:
		smallest = l
	if r < n and arr[smallest] > arr[r]:
		smallest = r

	if smallest != i:
		arr[i], arr[smallest] = arr[smallest], arr[i]
		heapify(arr, n, smallest)

def heap_sort(arr):

	N = len(arr)

	for i in range(N//2, -1, -1):
		heapify(arr, N-1, i)

	for i in range(N-1, -1, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)

	print("Final: ", arr)

def main(arr):
	heap_sort(arr)

if __name__ == '__main__':
	main([4,10,2,3,1,5,2,2,5,7,9,10,11,23])