def DecimalToBinary(m):
    temp = ""
    if m == 0:
        return "0"
    while m >= 1:
        digit = m % 2
        temp += str(digit)
        m = m // 2
    binary = temp[::-1]
    return binary

def countBits(n):
    result = list()
    for i in range(n+1):
        binary = DecimalToBinary(i)
        count = 0
        for j in range(len(binary)):
            if binary[j] == '1':
                count += 1
        result.append(count)
    return result

n = 5
print(countBits(n))

