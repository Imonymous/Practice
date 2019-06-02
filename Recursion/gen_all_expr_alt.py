#!/usr/bin/env python3

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
from my_eval import my_eval

def try_to_fit(s, i, output, answer, target):
	if i == len(s):
		out_str = "".join(output)
		value = my_eval(out_str)
		if value == target:
			answer.append(out_str)
		return

	if i == 0:
		try_to_fit(s, i+1, output+[s[i]], answer, target)
	else:
		try_to_fit(s, i+1, output+['*' + s[i]], answer, target)
		try_to_fit(s, i+1, output+['+' + s[i]], answer, target)
		try_to_fit(s, i+1, output+[s[i]], answer, target)


def generate_all_expressions(s, target):
	answer = []
	try_to_fit(s, 0, [], answer, target)
	return answer

def main(s, target):
	res = generate_all_expressions(s, target)
	for i in res:
		print(i)

if __name__ == '__main__':
	main("050505", 5)