def longestPalindrome(s):
    dics = {}
    count = 0
    plusone = False
    for i in range(len(s)):
        if s[i] not in dics:
            dics[s[i]] = 1
        else:
            dics[s[i]] += 1
    print(dics)
    for i in dics.keys():
        if dics[i] % 2 == 0:
            count += dics[i]
        else:
            plusone = True
    if plusone == True:
        count += 1
    return count

s = "abccccdd"
s = "a"
s = "bB"
print(longestPalindrome(s))


