from calculator import addition
from calculator import substraction
from calculator import division

def test_addition():
	assert addition(1,1) == 2
	
def test_substraction():
	assert substraction(2,1) == 1
	
def test_division():
	assert division(2,1) == 1