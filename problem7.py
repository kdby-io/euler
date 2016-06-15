def problem7(COUNT):

from math import sqrt

	num = 2
	while COUNT > 0:
	    for p in range(2, int(sqrt(num))+1):
	        if num != p and num % p == 0:
	            num += 1
	            break
	    else:
	        if COUNT == 1:
	            return num
	        COUNT -= 1
	        num += 1

if __name__ == '__main__':
	print(problem6(10001))