# Reverse bits of a given 32 bits unsigned integer.
# The input must be a binary string of length 32.
import math

def reverseBits(n):
    result = 0
    numstring = n[::-1]
    for i in range(len(numstring)):
        result += int(numstring[i]) * math.pow(2, len(numstring) - i - 1)
    return int(result)

n = "00000010100101000001111010011100"
n = "11111111111111111111111111111101"
print(reverseBits(n))