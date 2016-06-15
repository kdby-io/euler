def problem10(LIMIT):
	from math import sqrt

	total = 0
	for num in range(2, LIMIT+1):
	    for tester in range(2, int(sqrt(num))+1):
	        if num % tester == 0:
	            break
	    else:
	        total += num

	return total

if __name__ == '__main__':
	print(problem10(2000000))