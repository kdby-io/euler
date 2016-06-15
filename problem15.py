def problem15(size):
    field = []
    for y in range(0, size+1):
        field.append([])
        for x in range(0, size+1):
            
            if x is 0 or y is 0:
                field[y].append(1)
            else:
                field[y].append(field[y-1][x]+field[y][x-1])
 
    return field[size][size]

if __name__ == '__main__':
    print(problem15(20))
