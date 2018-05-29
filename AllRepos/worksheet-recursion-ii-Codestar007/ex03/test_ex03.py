from digitalSum import digitalSum

def test_one():
	assert digitalSum(2019) == 12

def test_two():
	assert digitalSum(9) == 9

def test_three():
	assert digitalSum(100000) == 1
