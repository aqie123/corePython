def multi_isinstance(a, b, c):
	z = [False for i in (a,b,c) if not isinstance(i, (int, float))]
	if z:
		return False
	else:
		return True