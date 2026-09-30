"""
some formulas
"""

def fib(x:int):
	"""
	int x ->
	fib(x)
	"""
	if x < 0:
		return -1
	elif x in (0, 1):
		return x
	else:
		return fib(x - 1) + fib(x -2)

def BMI(w:int, h:int):
	"""
	w(weight kg):int ->
	h(hight m):int ->
	bmi(w / h ^ 2)
	"""
	return w / h ** 2
