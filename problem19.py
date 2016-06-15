import itertools

def problem19():
    count = 0

    week = ['MON','TUE','WED','THU','FRE','SAT','SUN']
    today = {'year':1900, 'mon':1, 'day':1}

    for date in itertools.cycle(week):
        #print(today['year'], today['mon'], today['day'])
        if today['year'] >= 2001:
            break

        if today['day'] == 1 and date == 'SUN' and today['year'] >= 1901:
            print(today['year'], today['mon'], today['day'])
            count += 1

        isLeapYear = (today['year']%400 == 0) or (today['year']%100 != 0 and today['year']%4 == 0)
        if today['day'] == 31 and today['mon'] == 12:
            today['year'] += 1
            today['mon'] = 1
            today['day'] = 1
        elif today['day'] == 30 and today['mon'] in (4,6,9,11):
            today['mon'] += 1
            today['day'] = 1
        elif today['day'] == 31 and today['mon'] in (1,3,5,7,8,10):
            today['mon'] += 1
            today['day'] = 1
        elif today['day'] == 28 and today['mon'] == 2 and not isLeapYear:
            today['mon'] += 1
            today['day'] = 1
        elif today['day'] == 29 and today['mon'] == 2 and isLeapYear:
            today['mon'] += 1
            today['day'] = 1
        else:
            today['day'] += 1

    return count

if __name__ == '__main__':
    print(problem19())
