# Start Time: 18:04pm | 35mins
# Manav: BRB

# 6:43
n = 11

def factorial_recursive(n):
    # Base
    if n == 0:
        return 1

    else:
        return factorial_recursive(n-1) * n


# Factorial memo
memo = [None]*(n+1)

# Mechanical Steps: Memo from Recursive
# 1. init memo
# 2. If memo exists, use it
# 3. Else, compute and add to memo
# 4. Return memo[n]

def factorial_memo(n):
    # Use memo[n] if available
    if memo[n] is not None:
        return memo[n]
    
    # Compute memo[n]
    # Base
    if n == 0:
        memo[n] = 1
        # return 1

    else:
        memo[n] = factorial_memo(n-1) * n
        # return factorial(n-1) * n

    return memo[n]



# Mechanical Steps: DP from Memo
# 1. Init memo
# 2. n -> i
# 3. fn(x) -> memo[x]
# 4. Return memo[n] outside the loop

def factorial_dp(n):
    # Init
    mem = [-1] * (n+1)
    
    # N+1
    for i in range(n+1):
        if memo[i] is not None:
            return memo[i]

        # Base
        # Step: Change `n` -> `i`
        if i == 0:
            memo[i] = 1

        else:
            # Step: Change `n` -> `i`
            # Step: fn(x) call -> memo[x]
            memo[i] = memo[i-1] * i

        # Step: Do not return
        # return memo[i]
    
    # Step return memo[n] in the end
    return memo[n]

print factorial_dp(10)



def factorial_iterative(n):
    # Init
    memory = [-1] * (n+1)
    
    # Base
    memory[0] = 1
    
    # Work your way up
    for i in range(1, n+1):
        memory[i] = memory[i-1] * i
    
    # print memory
    return memory[n]
            

# for i in range(n, -1, -1):
#     # just for fun; reverse computation
#     print 'N:', '%d! = ' % i, factorial(i)


# print memo
