# def hailstone(n):
# 	if n == 1:
# 		return str(n)
# 	elif n % 2 == 0:
# 		return str(n) + ", " + str(hailstone(n // 2))
# 	else:
# 		return str(n) + ", " + str(hailstone(3 * n + 1))

#Code provided by Dr Keith Mannock
def hailstone(n):
	"""Return the hailstone sequence starting at n as a list"""
	def helper(n, lst):
		lst.append(n)
		if n == 1:
			return lst
		elif n % 2 == 0:
			return helper(n // 2, lst)
		else:
			return helper(3 * n + 1, lst)
	return helper(n,[])

print(hailstone(5))
