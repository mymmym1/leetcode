def arrangeCoins(n):
    i = 1
    count = 0
    while n - i >= 0:
      n = n - i
      i += 1
      count += 1
    return count

n = 5
n = 8
print(arrangeCoins(n))