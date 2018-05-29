def digitalRoot(n):
	t = str(digitalSum(n))
	if len(t) == 1:
		return int(t)
	else:
		return digitalRoot(t)

def digitalSum(n):
	s = str(n)
	if len(s) == 0:
		return 0
	else:
		return int(s[0]) + digitalSum(str(s[1:len(s)]))
