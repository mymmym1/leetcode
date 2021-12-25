def canWinNim(n):
    if n % 4 == 0:
        return False
    else:
        return True

n = 4
print(canWinNim(n))