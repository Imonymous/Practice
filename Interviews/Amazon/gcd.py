#!/usr/bin/env python

def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    min_val = min(arr)
    gcd = 1

    for i in range(min_val,1,-1):
        count = 0
        for j in range(num):
            if arr[j] % i == 0:
                count += 1
                continue
            else:
                break
        if count == num:
            gcd = i
            break

    print gcd

generalizedGCD(5, [2,4,6,8,10])
