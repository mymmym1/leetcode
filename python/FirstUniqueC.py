def firstUniqChar(s):
    sdic = {}
    c = ''
    for i in range(len(s)):
        if s[i] not in sdic:
            sdic[s[i]] = 1
        else:
            sdic[s[i]] += 1
    for i in sdic.keys():
        if sdic[i] == 1:
            c = i
            break
    for i in range(len(s)):
        if s[i] == c:
            return i
    return -1

s = "leetcode"
s = "loveleetcode"
s = "aabb"
print(firstUniqChar(s))
