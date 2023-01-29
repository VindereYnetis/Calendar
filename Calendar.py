def program(year):
    january = 31
    march = 31
    april = 30
    may = 31
    june = 30
    july = 31
    august = 31
    september = 30 
    october = 31
    november = 30
    december = 31
    if (year % 4 == 0):
        february = 29
    else: february = 28
    months = [january, february, march, april, may, june, july, august, september, october, november, december]
    i = 0
    result = 0
    for i in range(len(months)):
        result += sumMonth(months[i])
    return result

def sumMonth(month):
    i = 1
    month += 1
    result = 0
    for i in range(month):
        if (month < 10):
            result += i
        else: result += (i // 10) + (i % 10)
    return result

x = int(input("Введите год: "))
print(program(x))