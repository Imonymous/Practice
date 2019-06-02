#!/usr/bin/env python

from quick_sort import partition

# Quick Select
def kth_int(arr, k, start, end):
	if start == end:
		return start
	p = partition(arr, start, end, start)
	if p == k-1:
		return p
	elif p > k-1:
		p = kth_int(arr, k, start, p-1)
	elif p < k-1:
		p = kth_int(arr, k, p+1, end)
	else:
		print "Exception!"

	return p


def kth_int_main(arr, k):
	n = len(arr)
	if k <= n:
		p = kth_int(arr, k, 0, n-1)
		return arr[p]
		

print(kth_int_main([2,3,4,7,5,9,1], 7))