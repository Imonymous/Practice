#!/usr/bin/env python3

def maxStolenValue(values):

	n = len(values)
	t = [0]*n

	t[n-1] = values[n-1]
	t[n-2] = max(values[n-1], values[n-2])

	for i in range(n-3,-1,-1):
		t[i] = max(values[i]+t[i+2], t[i+1])

	return t[0]


res = maxStolenValue([6,1,2,7])

print(res)