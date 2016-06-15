def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)

def problem25(length):
    f1 = 1
    f2 = 1
    count = 3
    while True:
        f3 = f1 + f2
        if len(str(f3)) >= length:
            print(count, f3)
            break
        f1 = f2
        f2 = f3
        count += 1
    return count

if __name__ == '__main__':
    print(problem25(1000))
