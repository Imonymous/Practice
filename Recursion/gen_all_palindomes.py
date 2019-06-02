#!/usr/bin/env python

'''
Consider abracadabra
Then the possibilities look like 

a|b|r|a|c|a|d|a|b|r|a
a|b|r|aca|d|a|b|r|a
a|b|r|a|c|ada|b|r|a


Contract: 

f(s, start, end)
returns if s[start:end] is palindromic

True if start >= end (== Odd, > Even)
f(s, start+1, end-1) if s[start] == s[end]
False if s[start] != s[end]
'''

def check_palindrome(s, start, end): # end is exclusive

	if start > end:
		return True

	if s[start] == s[end-1]:
		return check_palindrome(s, start+1, end-1)
	else:
		return False

# Failed Attempt 1 (skips other possible palindromes with the stride)
# def gen_all_valid_subsets(s, start, end, stride): # end is exclusive

# 	if start+stride > end:
# 		return gen_all_valid_subsets(s, start, end, stride-1)

# 	if check_palindrome(s, start, start+stride):
# 		res = s[start:start+stride]

# 		if start+stride == end:
# 			return res
# 		else:
# 		 	return res+"|"+gen_all_valid_subsets(s, start+stride, end, stride)
# 	else:
# 		return s[start]+"|"+gen_all_valid_subsets(s, start+1, end, stride)


# def generate_all_palindromes(s):

# 	out = []
# 	for stride in range(1, len(s)+1):
# 		res = gen_all_valid_subsets(s, 0, len(s), stride)
# 		if res not in out:
# 			out.append(res)
# 	return out

# Failed attempt 2 (doesn't print all possible combinations)
'''
Stitch every possible combo and handle the individual letters at the end
'''
# def generate_all_palindromes(s):

# 	out = []
# 	for start in range(len(s)):
# 		for end in range(start+1,len(s)+1):
# 			if check_palindrome(s, start, end):
				
# 				res = ""

# 				if start > 0:
# 					if check_palindrome(s, 0, start):
# 						res = s[0:start]
# 					else:
# 						res = "|".join(s[0:start])
# 					res += "|"

# 				res += s[start:end]

# 				if end < len(s):
# 					res += "|"
# 					if check_palindrome(s, end, len(s)):
# 						res += s[end:len(s)]
# 					else:
# 						res += "|".join(s[end:len(s)])

# 				if res not in out:
# 					out.append(res)

# 	x = "|".join(s)
# 	if x not in out:
# 		out.append(x)

# 	return out

# Generate all possible palindromes first, then synthesize to match input
# def generate_all_palindromes(s):

# 	out = []
# 	for start in range(len(s)):
# 		for end in range(start+1,len(s)+1):
# 			if check_palindrome(s, start, end):
# 				res = s[start:end]
# 				if res not in out:
# 					out.append(res)
# 	return out

# Failed Attempt 3 
# def recurse1(s, start, end):
# 	if start >= end:
# 		return s[end]

# 	return s[start]+"|"+recurse1(s, start+1, end)

# def recurse2(s, start, end):
# 	if start >= end:
# 		return s[start]

# 	return recurse2(s, start, end-1)+"|"+s[end]
	

# def generate_all_palindromes(s):
# 	for i in range(1, len(s)):
# 		print(s[0:i] + "|" + recurse1(s, i, len(s)-1))

# 	for i in range(len(s)-2, -1, -1):
# 		print(recurse2(s, 0, i) + "|" + s[i+1:len(s)])

# Attempt 4
def find_all_palindromes(a, subsets):
	res = []

	if subsets > 0:
		for i in range(subsets):
			end = i+(len(a)-subsets)+1
			if check_palindrome(a,i,end):
				res.append(a[i:end])
		res += find_all_palindromes(a, subsets-1)
	else:
		res.append("")

	return res

def printPermutationsMain(inp):
	return printPermutations(inp, 0)

def printPermutations(array, i):
    if i == (len(array) - 1):
        print("".join(array))
        return
    for j in range(i, len(array)):
        array[i], array[j] = array[j], array[i]
        printPermutations(array, i + 1)
        array[i], array[j] = array[j], array[i]

def generate_all_palindromes(a):
	# res = find_all_palindromes(a, len(a))
	# print(res)
	printPermutations(list(a), 0)
	

generate_all_palindromes("tacocat")
# print(generate_all_palindromes("tacocat"))
# print(generate_all_palindromes("abracadabra"))
# print(generate_all_palindromes("tacocato"))
