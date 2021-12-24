# 1 <= pattern.length <= 300. Pattern contains only lower-case English letters. 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '. s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

def wordPattern(pattern, s):
    slist = s.split()
    if len(pattern) != len(slist):
        return False
    else:
        listOflist = []
        for i in range(len(pattern)):
            listOflist.append([pattern[i], slist[i]])
        for i in range(len(listOflist)):
            for j in range(len(listOflist)):
                if j>i and listOflist[i][0] == listOflist[j][0]:
                    if listOflist[i][1] != listOflist[j][1]:
                        return False
        return True

#pattern = "abba"
#s = "dog cat cat dog"
#s = "dog cat cat fish"
pattern = "aaaa"
s = "dog cat cat dog"

print(wordPattern(pattern, s))