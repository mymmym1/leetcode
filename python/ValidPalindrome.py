def isPalindrome(s):
    newWord = ''
    for i in range(len(s)):
        if s[i].isalnum():
            newWord += s[i].lower()
    revWord = newWord[::-1]
    #print(newWord, ',', revWord)
    if newWord == revWord:
        return True
    else:
        return False

s = "A man, a plan, a canal: Panama"
#s = "race a car"
#s = " "
print(isPalindrome(s))


