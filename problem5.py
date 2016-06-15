def problem5(LIMIT):

	primes = [1]
	for num in range(2, LIMIT+1):
	    for i in range(len(primes)):
	        if num%primes[i] == 0:
	            num //= primes[i]
	    if num is not 1:
	        primes.append(num)
	# print(primes)

	result = 1
	for p in primes:
	    result *= p
	return result

if __name__ == '__main__':
	print(problem5(20))