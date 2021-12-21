# -2^31 <= n <= 2^31 - 1

def isPowerOfTwo(n):
    m = 0
    while n % 2 == 0 and n // 2 != 0:
        m = n % 2
        n = n // 2
    if abs(n) == 1 and m == 0:
        return True
    else:
        return False

n = 1
n = 16
n = -2
n = -3
n = 0
print(isPowerOfTwo(n))
