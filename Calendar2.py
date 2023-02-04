year = int(input("Введите год: "))
if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 400 == 0) and (year % 100 == 0)): february = 29
else: february = 28
months = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i = 0
result = 0
for i in range(len(months)):
    months[i] += 1
    x = 1
    for x in range(months[i]):
        if (x < 10):
            result += x
        else: 
            result += (x // 10) + (x % 10)
print(result)