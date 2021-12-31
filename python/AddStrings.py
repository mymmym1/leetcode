def addNumber(temp, result):
    if temp > 10:
        carry = int(str(temp)[0])
        n = str(temp)[1]
        result += n
    else:
        result += str(temp)
        carry = 0
    return result, carry

def addStrings(num1, num2):
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    i = len(num1) - 1
    j = len(num2) - 1
    result = ""
    carry = 0
    while i >= -1:
        while j >= 0:
            temp = (ord(num1[i]) - ord('0')) + (ord(num2[j]) - ord('0')) + carry  # int
            result, carry = addNumber(temp, result)
            j -= 1
            i -= 1
        if i >= 0:
            temp = (ord(num1[i]) - ord('0')) + carry
            result, carry = addNumber(temp, result)
            i -= 1
        if i < 0:
            if carry > 0:
                result += str(carry)
            i -= 1
    return result[::-1]

#num1 = "11"
#num2 = "123"
num1 = "456"
num2 = "77"
#num1 = "0"
#num2 = "0"
print(addStrings(num1, num2))
