def change(amount, coins):
    arr = [1] + [0] * amount  # initialize to [1, 0, 0, 0, 0, 0];
    # 1 means if that amount of money cannot be made up by any combination of the coins, return 0, which is the only answer.
    for c in coins:
        for i in range(c, amount+1):  # [c,amount] e.g. [1,5]; [2,5]
            arr[i] += arr[i-c]  # arr[i]: the possible ways at i = arr[c]: the possible ways with only coin c
                                                               # + arr[i-c]: the possible ways with more than one coin
    return arr[amount]
# https://maxming0.github.io/2020/06/07/Coin-Change-2/

amount = 5
coins = [1, 2, 5]
# amount = 3
# coins = [2]
# amount = 10
# coins = [10]
m = change(amount, coins)
print(m)