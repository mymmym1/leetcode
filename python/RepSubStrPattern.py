def repeatedSubstringPattern(s):
    if len(s) == 1:
        return True
    else:
        newstring = ""
        for i in range(len(s)):
            if s[i] != s[0]:
                newstring += s[i]
            else:
                newstring += " "
                newstring += s[i]
        l = newstring.split()
        #print(l)
        if len(l) == 1:
            return True
        else:
            i = 0
            while i+1 < len(l):
                if l[i] == l[i + 1]:
                    i += 1
                else:
                    return False
            return True
    return False

s = "abab"
s = "aba"
s = "abcabcabcabc"
print(repeatedSubstringPattern(s))

