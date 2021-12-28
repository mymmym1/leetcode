def findTheDifference(s, t):
    sdic = {}
    for i in range(len(s)):
        if s[i] not in sdic:
            sdic[s[i]] = 1
        else:
            sdic[s[i]] += 1
    tdic = {}
    for i in range(len(t)):
        if t[i] not in tdic:
            tdic[t[i]] = 1
        else:
            tdic[t[i]] += 1
    for i in tdic.keys():
        if i not in sdic.keys():
            return i
        else:
            if tdic[i] != sdic[i]:
                return t
    return -1

#s = "abcd"
#t = "abcde"
s = ""
t = "y"
print(findTheDifference(s, t))