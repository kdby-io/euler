def problem21(limit):
    def getSum(n):
        sum = 0
        for i in range(1, n):
            if n%i == 0 and n!=i:
                sum += i
        return sum

    result = 0
    for n in range(1, limit+1):
        candidate = getSum(n)
        if n == getSum(candidate) and n != candidate:
            print(n, candidate)
            result += n
    return result

if __name__ == '__main__':
    print(problem21(10000))
