#1 <= s.length <= 5 * 10^4, t.length == s.length, s and t consist of any valid ascii character.
def isIsomorphic(s, t):
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = t[i]
        else:
            if t[i] != dic[s[i]]:
                return False

    return True

#s = "egg"
#t = "add"
s = "foo"
t = "bar"
#s = "paper"
#t = "title"
print(isIsomorphic(s, t))