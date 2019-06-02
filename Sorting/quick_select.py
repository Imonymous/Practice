#!/usr/bin/env python3

def swap(a, b):
	a, b = b, a

def partition(arr, lo, hi):
	pivot = lo
	p = lo
	swap(arr[pivot], arr[hi])

	for i in range(lo, hi):
		if arr[i] < arr[hi]:
			swap(arr[i], arr[p])
			p += 1

	swap(arr[hi], arr[pivot])


def quick_select(arr, k, lo, hi):
	
	if lo == hi:
		return arr[lo]

	p = partition(arr, lo, hi)

	p_rank = p+1

	if k == p_rank:
		return arr[p]
	elif k < p_rank:
		return quick_select(arr, k, lo, p-1)
	elif k > p_rank:
		return quick_select(arr, k-p_rank, p+1, hi)

def main(arr, k):
	if k == 0 or len(arr) == 0 or len(arr) < k:
		raise ValueError
	res = quick_select(arr, k, 0, len(arr)-1)

	print(res)
