def max(lst):
	largest = lst[0]
	if len(lst) == 1: # Base case
		return lst[0]
	else:
		if max(lst[1:len(lst)]) > largest:
			return max(lst[1:len(lst)])
		else:
			return lst[0]
