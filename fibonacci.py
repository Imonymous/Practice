def fibonacci_recursive(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

memo = [None]*11
def fibonacci_memo(n):
	if memo[n] is not None:
		return memo[n]

	if n == 0:
		memo[n] = 0
	elif n == 1:
		memo[n] = 1
	else:
		memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)

	return memo[n]

def fibonacci_dp(n):
	memo = [None]*(n+1)

	for i in range(n+1):
		if memo[i] is not None:
			return memo[i]

		if i == 0:
			memo[i] = 0
		elif i == 1:
			memo[i] = 1
		else:
			memo[i] = memo[i-1] + memo[i-2]

	return memo[i]

def fibonacci_iterative(n):
	memo = [None]*(n+1)

	memo[0] = 0
	memo[1] = 1

	for i in range(2, n+1):
		memo[i] = memo[i-1] + memo[i-2]

	return memo[n]

print fibonacci_recursive(10)
print fibonacci_memo(10)
print fibonacci_dp(10)
print fibonacci_iterative(10)
