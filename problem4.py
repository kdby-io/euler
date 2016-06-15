def problem4():

	max_v = 0

	for first in range(1, 1000):
	    for second in range(1, 1000):
	        total = first * second
	        if str(total) == str(total)[::-1]:
	            if max_v < total:
	                max_v = total
	return max_v

if __name__ == '__main__':
	print(problem4())