def isPowerOfFour(n):
    if n == 0:
        return False
    else:
        while n % 4 == 0:
            n = n / 4
        if abs(n) == 1:
            return True
        else:
            return False

n = 16
#n = 5
#n = 1
print(isPowerOfFour(n))