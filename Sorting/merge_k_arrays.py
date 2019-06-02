#!/usr/bin/env python
import sys

def heapifyUp(arr, i):
	if i//2 >= 1:
		if arr[i//2] > arr[i]:
			arr[i//2], arr[i] = arr[i], arr[i//2]
		heapifyUp(arr, i//2)


def heapifyDown(arr, i, last):
	if i*2+1 < last:
		if arr[i*2] < arr[i*2+1]:
			min_kid = i*2
		else:
			min_kid = i*2+1
		if arr[min_kid] < arr[i]:
			arr[min_kid], arr[i] = arr[i], arr[min_kid]
			heapifyDown(arr, min_kid, last)
	elif i*2 < last:
		min_kid = i*2
		if arr[min_kid] < arr[i]:
			arr[min_kid], arr[i] = arr[i], arr[min_kid]
			heapifyDown(arr, min_kid, last)


def deleteMin(heap, last):
	heap[1], heap[last] = heap[last], heap[1]
	heapifyDown(heap, 1, last)


def insert(heap, i):
	heap.append(i)
	size = len(heap)
	heapifyUp(heap, size-1)


def mergeArrays(arrays):
	heap = [0]
	prev = None
	increasing = None
	for array in arrays:
		for a in array:
			insert(heap, a)

			if prev is not None and prev != a and increasing is None:
				if prev > a:
					increasing = False
				else:
					increasing = True
			prev = a


	for i in range(len(heap)-1, 0, -1):
		deleteMin(heap, i)

	res = heap[1:]

	if increasing:
		res.reverse()

	return res


if __name__ == '__main__':
	f = sys.stdout

	arr_rows = int(input())
	arr_columns = int(input())

	arr = []

	for _ in range(arr_rows):
	    arr.append(list(map(int, input().rstrip().split())))

	res = mergeArrays(arr)

	f.write('\n'.join(map(str, res)))
	f.write('\n')

	f.close()