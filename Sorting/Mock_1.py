#!/usr/bin/env python3

# 1st Mock - sort(arr, k) where k=max distance of an element from its original position

# Actual attempt (Selection sort)
a = [2, 3, 1, 6, 5, 4]
k = 2

# def sel_sort(arr, k):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, i+k+1):
#             if j < len(arr):
#                 if arr[j] < arr[min_idx]:
#                     min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
                
# print(sel_sort(a, k))

def swap(a, b):
	a, b = b, a

def heapifyUp(h, i):
	smallest = i 
	l = 2*i+1
	r = 2*i+2

	if l < len(h) and h[l] < h[smallest]:
		smallest = l

	if r < len(h) and h[r] < h[smallest]:
		smallest = r

	if smallest != i:
		swap(h[i], h[smallest])
		heapifyUp(h, smallest)

def heapifyDown(h, i, last):
	l = i*2+1
	r = i*2+2
	if r < last:
		if h[l] < h[r]:
			min_kid = l
		else:
			min_kid = r
		if h[min_kid] < h[i]:
			swap(h[min_kid], h[i])
			heapifyDown(h, min_kid, last)
	elif l < last:
		min_kid = l
		if h[min_kid] < h[i]:
			swap(h[min_kid], h[i])
			heapifyDown(h, min_kid, last)

def delete_min(h, elem, last):
	min_val = h[0]
	del h[0]
	h.append(elem)
	print(h)
	heapifyDown(h, 0, last)
	print(h)
	return min_val

def heap_sort_k(a, k):
	
	out = []
	h = []
	for i in range(k, -1, -1):
		h.append(a[i])
		heapifyUp(h, i)

	#print(out)
	
	for j in range(len(a)-1, k, -1):
		out.append(delete_min(h, a[j], len(h)-1))
		#print(out)

	remaining = k

	while remaining >= 0:
		out.append(delete_min(h, None, remaining))
		remaining -= 1
		#print(out)

	return out
print(heap_sort_k(a, k))
		
