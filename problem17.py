def problem17(limit):
    total = 0
    for n in range(1, limit+1):
        total += counter(n)
    return total


def counter(n):
    cc_1to19 = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8)
    cc_10 = (0, 0, 6, 6, 5, 5, 5, 7, 6, 6, 7)
    cc_1000 = len('thousand')

    count = 0
    # is last two number under 20?
    last_two = n%100
    if last_two < 20:
        count += cc_1to19[last_two]
    else:
        count += cc_1to19[last_two%10]
        count += cc_10[last_two//10]

    # 백의자리
    if n//100%10 is not 0:
        if last_two is not 0:
            count += len('and')
        count += cc_1to19[n//100%10] + cc_10[10]

    # 천의자리
    if n//1000 is not 0:
        count += cc_1to19[1] + cc_1000
    
    return count


if __name__ == '__main__':
    print(problem17(1000))
