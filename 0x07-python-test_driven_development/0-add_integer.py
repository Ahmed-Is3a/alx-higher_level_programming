#!/usr/bin/python3

def add_integer(a, b=98):
	"""
	adds two integers.

	cast a and b to integers

	Parameters:
	- a (int or float): the first number
	- b (int or float): the second number

	Reurns:
	int: sum of a + b

	Raises:
	TypeError: If a or b is not integer or float
	"""
	if not (isinstance(a, int) or isinstance(a, float)):
		raise TypeError("a must be an integer or float")
	if not (isinstance(b, int) or isinstance(b, float)):
		raise TypeError("b must be an integer or float")
	
	# cast a and b to int
	a = int(a)
	b = int(b)

	return (a + b)
