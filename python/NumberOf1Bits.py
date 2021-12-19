def hammingWeight(n):
    count = 0
    for number in n:
        if number == '1':
            count += 1
    return count

n = "00000000000000000000000000001011"
n = "00000000000000000000000010000000"
n = "11111111111111111111111111111101"
print(hammingWeight(n))