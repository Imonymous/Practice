#!/usr/bin/env python3
'''
Mock 10

Marmelade Citizens need protection from chocolate monsters! They decide to build a strong sugar wall.

A wall is considered strong if it has a subsegment where height increases from l to t by 1 (for example 2, 3, 4) and then decreases from t to r by 1 (for example 6, 5, 4).
Thereby, a wall of height (t-l+1) + (t-r+1) . "1 2 3 3 2 1" is a strong wall, if l = 1, t = 3, r = 1, and "2 1 2 3 2 1" is not a strong wall with the same l,t , r.
Marmelade Citizens have a wall of length n and they can only increase the height of some pieces of the wall. Help them make a wall strong and waste as little sugar as possible! An increase in height of one piece of wall by 1 costs 1. A decrease in height is prohibited.

e.g
0 2 2 1 2 1

l=1 t=3 r=1

o/p
1 0 1 2 0 0

4

e.g 2) 0 2 2 1 4 1
l=1 t=3 r=1

-1

e.g 3)
0 4 2 1 2 1 0 0 0 0
l=1 t=3 r=1

0 0 0 0 0 2 3 2 1 0 --- cost


1 1 1 1 1 1 1 1 1 1 1
l=1 t=3 r=1
0 1 2 2 1 0 0 0 0 0 0

- look for elem <= l
- add 0 to l to that elem, update cost
- next in the list, l+1, l+2... t, keep updating cost
- try going from t to r, but if next is greater than curr, try another subsequence

'''

import sys
def find_cost(arr, l, t, r):

    min_cost_so_far = sys.maxsize
    x = [i for i in range(l, t+1)]
    y = [i for i in range(t, r-1, -1)]
    x.extend(y)
    ref = x

    start_idx = 0
    end_idx = len(ref)

    while end_idx <= len(arr):
        cost = 0
        check_cost = True
        for i in range(len(ref)):
            diff = ref[i] - arr[start_idx + i]
            if diff >= 0:
                cost += diff
            else:
                check_cost = False
                break

        if cost < min_cost_so_far and check_cost:
            min_cost_so_far = cost

        start_idx += 1
        end_idx += 1

    if min_cost_so_far == sys.maxsize:
        min_cost_so_far = -1

    return min_cost_so_far


print(find_cost([1, 2, 3, 3, 2, 1,1,1,1,1,1,1], 1, 3, 1))
