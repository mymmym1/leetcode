def decode(encoded, first):
    result = [first]
    for i in range(len(encoded)):
        bitI = bin(encoded[i])
        bitNum = int(bin(result[i]), 2) ^ int(bitI, 2)
        result.append(bitNum)
    return result

encoded = [1,2,3]
first = 1
# encoded = [6, 2, 7, 3]
# first = 4
print(decode(encoded, first))