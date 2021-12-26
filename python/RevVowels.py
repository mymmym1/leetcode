def reverseVowels(s):
    vowelList = list()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        for j in vowels:
            if s[i] == j:
                vowelList.append([j,i])
    #print(vowelList)
    for i in range(len(vowelList)//2):
        temp = vowelList[i][1]
        vowelList[i][1] = vowelList[len(vowelList)-1-i][1]
        vowelList[len(vowelList) - 1 - i][1] = temp
    #print(vowelList)
    #Strings are immutable in Python.
    output = ""
    for i in range(len(s)):
        for j in range(len(vowelList)):
            if i == vowelList[j][1]:
                output += vowelList[j][0]
        if len(output) <= i:
            output += s[i]

    return output

s = "hello"
s = "leetcode"
print(reverseVowels(s))
