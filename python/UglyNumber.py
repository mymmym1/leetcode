def isUgly(n):
    while n % 2 == 0:
        n = n/2
    while n % 3 == 0:
        n = n/3
    while n % 5 == 0:
        n = n/5
    if n == 1:
        return True
    else:
        return False

n = 6
n = 1
n = 14
print(isUgly(n))