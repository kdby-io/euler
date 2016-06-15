def problem9():
	from math import sqrt

	a, b = 1, 2
	done = False
	while not done:
	    for a in range(1, b):
	        c = sqrt(pow(a,2) + pow(b,2))
	        if a+b+c == 1000:
	            # print('{} + {} = {}'.format(pow(a,2), pow(b,2), pow(c,2)))
	            # print('{} x {} x {} = {}'.format(a, b, c, a*b*c))
	            return a*b*c
	            done = True
	    else:
	        b += 1

if __name__ == '__main__':
	print(problem9())