#!/usr/bin/env python

'''
Consider 123456789
Then the possibilities look like 

 * * * * * * * *
1+2+3+4+5+6+7+8+9
 " " " " " " " "

string_arr = gen_all_possible_strings()
for string in string_arr:
	res = process_string(string)
	if res == target:
		add to answer list
'''

def try_to_fit(s, i, value_so_far, prev, output, answer, target):
	if i == len(s):
		if value_so_far == target:
			answer.append("".join(output))
		return

	curr_val = 0

	for idx in range(i, len(s)):

		curr_val = 10*curr_val + int(s[idx])

		if i == 0:
			try_to_fit(s, idx+1, curr_val, curr_val, output+[str(curr_val)], answer, target)
		else:
			v = value_so_far - prev

			try_to_fit(s, idx+1, v + (prev*curr_val), prev*curr_val, output+['*' + str(curr_val)], answer, target)
			try_to_fit(s, idx+1, value_so_far+curr_val, curr_val, output+['+' + str(curr_val)], answer, target)

		# if s[i] == '0':
		# 	break


def generate_all_expressions(s, target):
	answer = []
	try_to_fit(s, 0, 0, 0, [], answer, target)
	return answer

def main(s, target):
	res = generate_all_expressions(s, target)
	for i in res:
		print(i)

if __name__ == '__main__':
	main("050505", 5)