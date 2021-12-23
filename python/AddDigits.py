def addDigits(num):
    while num > 9:
        sum = 0
        for i in range(len(str(num))):
            sum += int(str(num)[i])
        num = sum
    return num

num = 38
num = 0
print(addDigits(num))

