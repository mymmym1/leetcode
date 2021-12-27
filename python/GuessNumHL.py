# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# 1 <= n <= 231 - 1, 1 <= pick <= n
pick = 0
def guessNumber(n):
    if n < 2:
        mid = 1
        print("0", "mid=", mid)
        return mid
    start = 1
    end = n
    while start <= end:
        mid = (end - start) // 2 + start
        if mid > pick:
            end = mid
            print("1", "mid=", mid)
        elif mid < pick:
            start = mid
            print("-1", "mid=", mid)
        else:
            print("0", "mid=", mid)
            return mid

pick = 6
print(guessNumber(10))

