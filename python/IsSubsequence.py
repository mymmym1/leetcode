def isSubsequence(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

#s = "abc"
#t = "ahbgdc"
#s = "axc"
#t = "ahbgdc"
s = "aabc"
t = "ahbagdc"
#s = "aabc"
#t = "ahbgdc"
print(isSubsequence(s, t))

