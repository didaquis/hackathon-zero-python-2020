import math

def sum(*arguments):
	'''
	# Alternative solution without import math

	result = 0
	for arg in arguments:
		result += arg
	
	return result
	'''
	return math.fsum(arguments)
