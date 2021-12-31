def hammingDistance(x, y):
    binaryX = bin(x).replace("0b", "").zfill(4)
    binaryY = bin(y).replace("0b", "").zfill(4)
    count = 0
    for i in range(4):
        if str(binaryX)[i] != str(binaryY)[i]:
            count += 1
    return count

#x = 1
#y = 4
x = 3
y = 1
print(hammingDistance(x, y))