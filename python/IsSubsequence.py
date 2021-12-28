def isSubsequence(s, t):
    i = 0
    j = 0
    sequence = []
    while i < len(s):
        while j < len(t):
            if s[i] == t[j]:
                if j not in sequence:
                    sequence.append(j)
                    j = 0
                    break
                else:
                    j += 1
            else:
                j += 1
                if j == len(t):
                    return False
        i += 1
    #print(sequence)    
    for i in range(len(sequence) - 1):
        if sequence[i+1] - sequence[i] < 0:
            return False
    return True

#s = "abc"
#t = "ahbgdc"
#s = "axc"
#t = "ahbgdc"
s = "aabc"
t = "ahbagdc"
#s = "aabc"
#t = "ahbgdc"
print(isSubsequence(s, t))

