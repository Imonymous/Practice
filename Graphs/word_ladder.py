#!/usr/bin/env python3
import os
import sys

from collections import deque

def hasOneDiff(one, two):
	assert(len(one) == len(two))
	count = 0

	for i in range(len(one)):
		if one[i] != two[i]:
			count += 1
		if count > 1:
			return False

	if count == 1:
		return True
	else:
		return False

def build_path(prev, stop, last):

	res = []
	i = last

	while prev[i] is not None:
		res.append(i)
		i = prev[i]

	res.append(i) # Add the start
	res.reverse() 
	res.append(stop) # Add the stop
	return res

def string_transformation(words, start, stop):

	prev = dict()
	res = []
	visited = []
	q = deque([])
	visited.append(start)

	prev[start] = None
    
	if hasOneDiff(start, stop):
		return [start, stop]

	if len(words) > 0:

		for word in words:
			if hasOneDiff(start, word):
				visited.append(word)
				q.append(word)
				prev[word] = start

		while len(q) > 0:
			curr = q.popleft()

			if hasOneDiff(curr, stop):
				return build_path(prev, stop, curr)

			for word in words:
				if word not in visited:
					if hasOneDiff(curr, word):
						visited.append(word)
						q.append(word)
						prev[word] = curr
	
	return ["-1"]

if __name__ == "__main__":
    f = sys.stdout

    words_size = int(input())

    words = []
    for _ in range(words_size):
        words_item = input()
        words.append(words_item)


    start = input()

    stop = input()

    res = string_transformation(words, start, stop)

    f.write('\n'.join(res))
    f.write('\n')
    f.close()
