def canConstruct(ransomNote, magazine):
    magazineDic = {}
    for i in range(len(magazine)):
        if magazine[i] not in magazineDic:
            magazineDic[magazine[i]] = 1
        else:
            magazineDic[magazine[i]] += 1
    ranDic = {}
    for i in range(len(ransomNote)):
        if ransomNote[i] not in ranDic:
            ranDic[ransomNote[i]] = 1
        else:
            ranDic[ransomNote[i]] += 1
    for i in ranDic.keys():
        if i not in magazineDic.keys():
            return False
        if i in magazineDic.keys():
            if ranDic[i] > magazineDic[i]:
                return False

    return True

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))

