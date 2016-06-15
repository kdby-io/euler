def problem22():
    f = open('names.txt', 'rt')
    names = f.read().split(',')
    for name in names:
        names[names.index(name)] = name.strip('\"')
    names.sort()

    result = 0

    for name in names:
        sum = 0
        for c in name:
            sum += ord(c) - 64	# ord(A) = 65
        result += (names.index(name)+1) * sum
    return result

if __name__ == '__main__':
    print(problem22())
