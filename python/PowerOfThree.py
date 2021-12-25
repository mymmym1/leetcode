def isPowerOfThree(n):
    if n == 0:
        return False
    else:
        while n % 3 == 0:
            n = n / 3
    if abs(n) == 1:
        return True
    else:
        return False

n = -27
print(isPowerOfThree(n))