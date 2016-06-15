def problem16():
	number = pow(2, 1000)
	result = sum(int(num) for num in str(number))
	return result

if __name__ == '__main__':
	print(problem16())