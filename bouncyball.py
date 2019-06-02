#!/usr/bin/env python2
"""
Problem: Count the number of combinations that a bouncy ball takes to hit nth stair.
Constraint: Once it takes a bounce of size b, it has to take a bounce of size b or greater.

Recursion Basics:

States:
    f(state)
        N = Original Number of Stairs
        n = stair you are at currently
        b = size of bounce so far (taken to get here)
        return count
Base:
    n = 0:
        return 1 => no bounce
    n = 1:
        return 1
    n = 2:  # Does this have to be a base
            # or can this be constructed?
        return 2 # [1,1], [2]

Guard:
    n < 0:
        return 0
    # May not be needed

Transition:
    f(n, b):
        count = 0
        for i in range(b, N):  # N is original number of stairs # 1000?
            #  if i > n; then n-i will be negative
            count += f(N, n-i, i)

        return count

-- Fitting it all in --
"""

def bouncy_recursion(N, n, b):
    print 'Entry: n:', n, 'b:', b
    
    # Guard
    if n < 0:
        print 'Guard: 0'
        return 0

        
    # Base
    if n == 0: #or n == 1:
        print 'Base: 1'
        return 1

    # Transition
    count = 0
    for i in range(b, n+1):
        print 'Transitions: n:', n-i, 'b:', i
        result = bouncy_recursion(N, n-i, i)
        print 'Result:', result
        count += result

    return count

"""
N = 3
    [1, 1, 1]
    [1, 2]
    [3]
    
N = 1
    [1]
"""


result = bouncy_recursion(3, 3, 1)
print 'Result:', result
# for i in range(3):
    # result = bouncy_recursion(i, i, 1)
    # print 'N:', i, 'Result:', result
