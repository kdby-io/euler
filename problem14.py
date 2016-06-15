def problem14():

    max_count = 0
    thatNum = 0
    for n in range(1, 1000000+1):
        n_cpy = n
        count = 0
        while n_cpy is not 1:
            if n_cpy%2 is 0:
                n_cpy = n_cpy // 2
            else:
                n_cpy = 3*n_cpy + 1
            count += 1
        if count > max_count:
            max_count = count
            thatNum = n

    return thatNum

if __name__ == '__main__':
    print(problem14())