# 1 <= n <= 2^31 - 1

def isHappy(n):
    s = set()
    while n != 1:
        result = 0
        for i in str(n):
            result += int(i) * int(i)
        n = result

        if n in s:
            return False
        s.add(n)

    return True

n = 19
#n = 2
print(isHappy(n))