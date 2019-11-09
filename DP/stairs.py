#!/usr/bin/env python3

def countWaysToClimb(steps, n):

	t = [0]*(n+1)

	t[0] = 1

	for i in range(1, n+1):
		for j in range(len(steps)):
			if i - steps[j] >= 0:
				t[i] += t[i-steps[j]]

	return t[n]
	
res = countWaysToClimb([2,3], 7)
print(res)