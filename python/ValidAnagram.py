def isAnagram(s, t):
    dic1 = {}
    for i in range(len(s)):
        if s[i] not in dic1.keys():
            dic1[s[i]] = 1
        else:
            dic1[s[i]] += 1
    dic2 = {}
    for i in range(len(t)):
        if t[i] not in dic2.keys():
            dic2[t[i]] = 1
        else:
            dic2[t[i]] += 1
    if dic1 == dic2:
        return True
    else:
        return False

s = "anagram"
t = "nagaram"
#s = "rat"
#t = "car"
print(isAnagram(s, t))