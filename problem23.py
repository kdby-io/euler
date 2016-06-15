from math import sqrt

SMALLEST_ABUNDANT = 12

def isAbundant(n):
    sum = 0
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0:
            if i != n//i:
                sum += i + n//i
            else:
                sum += i
    sum -= n
    return sum > n

def isSumOfAbundant(n):
    for n1 in range(SMALLEST_ABUNDANT, n//2+1):
        n2 = n - n1
        if isAbundant(n1) and isAbundant(n2):
            return True
    return False

def problem23():
    result = 0
    for n in range(1, 28124):
        if n%500 == 0:
            print(n)
        if not isSumOfAbundant(n):
            result += n
    return result

if __name__ == '__main__':
    print(problem23())
