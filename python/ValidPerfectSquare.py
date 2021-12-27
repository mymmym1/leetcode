# 1 <= num <= 2^31 - 1

def isPerfectSquare(num):
    n = 1
    while True:
        if n*n == num:
            return True
        else:
            if n*n > num:
                return False
            else:
                n += 1

num = 16
print(isPerfectSquare(num))
