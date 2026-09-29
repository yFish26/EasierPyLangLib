"""
some formulas
"""
def fib(x:int):
	"""
	int x -> fib(x)
	"""
	if x < 0:
		return -1
	elif x in (0, 1):
		return x
	else:
		return fib(x - 1) + fib(x -2)
