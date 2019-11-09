#!/usr/bin/env python

def russian_dolls(arr):
	sba = sorted(arr, key=lambda tup: tup[0]*tup[1], reverse=True)

	envelops = len(sba)

	print(sba[0])
	
	dp = [1]*envelops

	ans = 1
	for i in range(envelops):
		for j in range(i):
			if sba[i][0] < sba[j][0] and sba[i][1] < sba[j][1]:
				dp[i] = max(dp[i], dp[j]+1)

		ans = max(ans, dp[i])

	return ans


 
arr = [[5,4],[6,4],[6,7],[2,3]]
print(russian_dolls(arr))

