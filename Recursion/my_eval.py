#!/usr/bin/env python3

def my_eval(exp):
	res = 0
	if '*' in exp and '+' in exp:
		mults = exp.split('+')
		products = []
		for mult in mults:
			ops = mult.split('*')
			res = 1
			for op in ops:
				res *= int(op)
			products.append(res)
		return sum(products)

	elif '*' in exp and '+' not in exp:
		ops = exp.split('*')
		res = 1
		for op in ops:
			res *= int(op)
		return res

	elif '*' not in exp and '+' in exp:
		ops = exp.split('+')
		res = 0
		for op in ops:
			res += int(op)
		return res

	elif '*' not in exp and '+' not in exp:
		return int(exp)

my_eval("0+5+0*5*05")