#!/usr/bin/env python3
import sys

def minimum_coins(coins, value):
	t = [sys.maxsize]*(value+1)

	t[0] = 0

	for val in range(1, value+1):
		for coin in coins:
			if val >= coin:
				t[val] = min(t[val], t[val - coin])
		if t[val] != sys.maxsize:
			t[val] += 1

	return t[value]

print(minimum_coins([1,3,5], 9))
