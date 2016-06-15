def problem6(LIMIT):


	sum_of_pow = sum(pow(num, 2) for num in range(1, LIMIT+1))
	pow_of_sum = pow(sum(num for num in range(1, LIMIT+1)), 2)

	return pow_of_sum - sum_of_pow

if __name__ == '__main__':
	print(problem6(100))