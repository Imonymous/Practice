#!/usr/bin/env python
import sys

# Brute force
# def mergeArrays(array):
# 	K = len(array)
# 	N = len(array[0])

# 	print(K, N)

# 	out = []
# 	for i in range(N):
# 		for j in range(K):
# 			pos = len(out)-1
# 			if pos < 0:
# 				out.append(array[0][0])
# 			else:
# 				out.append(array[j][i])
# 				pos += 1 # Increment position
# 				while pos > 0 and (out[pos-1] > out[pos]):
# 					out[pos], out[pos-1] = out[pos-1], out[pos]
# 					pos -= 1
# 	return out

## Failed attempt
# def mergeArrays(arr):
# 	K = len(arr)
# 	N = len(arr[0])
# 	tracker = [0]*K
# 	out = []
# 	exhausted = []

# 	print(str(arr))

# 	while len(exhausted) < K:
# 		active_rows = [active_row for active_row in range(len(tracker)) if active_row not in exhausted]

# 		print(str(tracker[active_rows[0]]))
# 		print(str(arr[active_rows[:]][tracker[active_rows[0]]]))

# 		minimum = arr[active_rows[0]][tracker[active_rows[0]]]
# 		min_index = active_rows[0]
# 		for i in range(len(active_rows)):
# 			if arr[active_rows[i]][tracker[active_rows[i]]] < minimum:
# 				minimum = arr[active_rows[i]][tracker[active_rows[i]]]
# 				min_index = active_rows[i]
# 		out.append(minimum)
# 		print("O:"+str(out))
# 		tracker[min_index] += 1
# 		print("Tr:"+str(tracker))
# 		if tracker[min_index] == N:
# 			exhausted.append(min_index)
# 			print("Ex:"+str(exhausted))
# 	return out

## Using dictionaries
# def mergeArrays(arr):
# 	K = len(arr)
# 	N = len(arr[0])

# Mind=Blown!
def mergeArrays(arr):
    #
    # Write your code here.
    #
    arrays = arr
    return sorted([a for array in arrays for a in array])



if __name__ == '__main__':
	#array = {{2,3,4,5},{0,3,6,9},{-1,5,7,8}}
	#main(array)
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