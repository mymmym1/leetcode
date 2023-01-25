def reverseString(s):
    first = 0
    last = len(s) - 1
    while first < last:
        temp = s[first]
        s[first] = s[last]
        s[last] = temp
        first += 1
        last -= 1
    print(s)

s = ["h","e","l","l","o"]
#s = ["H","a","n","n","a","h"]
reverseString(s)
