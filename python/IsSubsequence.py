def isSubsequence(s, t):
    i = 0
    j = 0
    sequence = []
    while i < len(s):
        while j < len(t):
            if s[i] == t[j]:
                sequence.append(j)
                j = 0
                break
            else:
                j += 1
                if j == len(t):
                    return False
        i += 1
    for i in range(len(sequence) - 1):
        if sequence[i+1] - sequence[i] < 0:
            return False
    return True

#s = "abc"
#t = "ahbgdc"
s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))

