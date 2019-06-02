#!/usr/bin/env python

def lex_order(arr):
	d = dict()
	for i in arr:
		key, value = i.split()
		if key not in d:
			d[key] = [value]
			d[key].append(1) # Init count
		else:
			current_top = d[key][0]
			if value > current_top:
				d[key][0] = value
			d[key][1] += 1

	out = []
	for key, value in d.items():
		out.append(key+":"+str(value[1])+","+value[0])

	return out



arr = ["key1 abcd", "key2 zzz", "key1 hello", "key3 world", "key1 hello"]
print(lex_order(arr))
