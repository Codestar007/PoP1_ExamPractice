def nestedListContains(NL, target):
	if len(NL) == 0:
		return False
	else:
		if type(NL[0]) == list:
			return nestedListContains(NL[0], target)
		else:
			if NL[0] == target:  return True #pass
			else: return nestedListContains(NL[1:], target)


