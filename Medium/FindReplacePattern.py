# words[i].length == pattern.length

def findAndReplacePattern(words, pattern):
    foundw = []
    for s in words:
        singledic = {}
        count = 0
        for i in range(len(s)):
            if s[i] not in singledic:
                singledic[s[i]] = pattern[i]
                count += 1
            else:
                if singledic[s[i]] != pattern[i]:
                    break
                else:
                    count += 1
        if count == len(pattern):
            sameP = True
            for j in singledic.keys():
                for k in singledic.keys():
                    if j != k:
                        if singledic[j] == singledic[k]:
                            sameP = False
            if sameP is True:
                foundw.append(s)
    return foundw

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
words = ["a","b","c"]
pattern = "a"
print(findAndReplacePattern(words, pattern))



