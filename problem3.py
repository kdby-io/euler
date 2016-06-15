def problem3(num):

	div = 2

	while div < num:
	    if num%div == 0:
	        num = num // div
	        div = 2
	    else:
	        div += 1

	return num

if __name__ == '__main__':
	print(problem3(600851475143))