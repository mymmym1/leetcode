# 322. Coin Change

def coinChange(coins, amount):
    coins.sort()
    if amount < coins[0]:
        return 0
    else:
        i = len(coins) - 1
        while i >= 0:
            if amount >= coins[i]:
                count = amount // coins[i]
                rest = amount % coins[i]
                break
            i -= 1
        while i - 1 >= 0:
            while rest != 0:
                count += rest // coins[i - 1]
                rest = rest % coins[i - 1]
                i -= 1
        if i == 0 and rest != 0:
            return -1
    return count

coins = [1,2,5]
amount = 11
coins = [2]
amount = 3
coins = [1]
amount = 0
print(coinChange(coins, amount))

