#!/usr/bin/env python3

# # Attempt 1, using recursion
# def wordbreak(t, i, prefix, d):
# 	if i == len(t):
# 		if t in d:
# 			prefix.append(t)
# 			print(" ".join(prefix))
# 			del prefix[-1]

# 		return

# 	if t[:i] in d:
# 		wordbreak(t, i+1, prefix, d)

# 		prefix.append(t[:i])
# 		wordbreak(t[i:], 0, prefix, d)
# 		del prefix[-1]
# 	else:
# 		wordbreak(t, i+1, prefix, d)

def solver(dictionary, txt):
	# Write your code here
	n = len(txt)
	dp = [[] for _ in range(n+1)]
	for i in range(n-1, -1, -1):
		for k in range(i+1, n+1):
			prefix = txt[i:k]
			if prefix in dictionary:
				if k == n:
					dp[i].append(prefix)
				elif dp[k]:
					dp[i].extend([prefix + " " + entry for entry in dp[k]])
			print(dp)
	return dp[0]

def main():
	# d = ["kick", "start", "kickstart", "is", "awe", "some", "awesome"]

	# wordbreak("kickstartisawesome", 0, [], d)

	d = ["to", "do", "todo"]
	
	# wordbreak("totodo", 0, [], d)
	solver(d, "totodo")


if __name__ == '__main__':
	main()
