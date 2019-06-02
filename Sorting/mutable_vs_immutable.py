#!/usr/bin/python

def fun2(tup):
	tup += (4,) 

	print 'In Function:', tup

def fun(arr):
	arr += [4]

def fun3(a, b):
	a, b = b, a

def main():
	a = [1, 2, 3]
	b = (1, 2, 3)
	fun(a)
	fun2(b)
	print a
	print b

	fun3(a[1], a[2])
	print a
	a[1], a[2] = a[2], a[1]
	print a

if __name__ == '__main__':
	main()