#!/usr/bin/env python

# def recurse(a, subsets):
# 	res = []

# Contiguous subwords
# 	if subsets > 0:
# 		for i in range(subsets):
# 			end = i+(len(a)-subsets)+1
# 			# print(a[i:end])
# 			res.append(a[i:end])
# 		res += recurse(a, subsets-1)
# 	else:
# 		res.append("")

# 	return res

# Subwords
def generate_all_subsets(a, idx, res):
	if idx == len(a):
		res.append("")
		return res
	res = generate_all_subsets(a, idx+1, res)
	for i in range(len(res)):
		res.append(a[idx]+res[i])
	return res

def main(a):
	res = generate_all_subsets(a, 0, [])
	print res
# 	res = recurse(a, len(a))
# 	print(res)

if __name__ == '__main__':
	main("xyza")

