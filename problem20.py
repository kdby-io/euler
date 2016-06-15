def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def problem20(n):
    number = factorial(n)
    l = list(str(number))
    result = 0
    for s in l:
        result += int(s)
    return result

if __name__ == '__main__':
    print(problem20(100))    
