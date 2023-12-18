#!/usr/bin/python3

def safe_print_division(a, b):
	try:
		rslt = a / b
	except ZeroDivisionError:
		rslt = None
		return (None)
	else:
		return (rslt)
	finally:
		print("Inside result: {:f}".format(rslt))
