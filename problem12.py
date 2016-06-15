def problem12():

    from math import sqrt
    natural = 1

    while True:
        #삼각수 획득
        triNum = sum(n for n in range(1, natural+1))
        #print('TriNum : {}'.format(triNum))

        count = 1
        for tester in range(2, int(sqrt(triNum))+1):
            if triNum%tester == 0:
                count += 2
        #print('count : {}'.format(count))
        if count >=500:
            return triNum
        else:
            natural += 1

if __name__ == '__main__':
    print(problem12())