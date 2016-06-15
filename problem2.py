def problem2(LIMIT):

	first, second, third = 1, 1, 0

	total = 0

	while third < LIMIT:
	    third = first + second
	    if third%2 == 0:
	        total += third
	    first, second = second, third

	return total

if __name__ == '__main__':
	print(problem2(4000000))