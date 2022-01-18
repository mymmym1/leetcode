# digits in ascending order
# s is guaranteed to be valid.

def delc(word, s):
    for c in word:
        s = s.replace(c, '', 1)
    return s

def check(rl, s):
    while 'z' in s:
        rl.append("zero")
        s = delc("zero", s)
    while 'w' in s:
        rl.append("two")
        s = delc("two", s)
    while 'u' in s:
        rl.append("four")
        s = delc("four", s)
    while 'x' in s:
        rl.append("six")
        s = delc("six", s)
    while 'g' in s:
        rl.append("eight")
        s = delc("eight", s)
    while 'o' in s:
        rl.append("one")
        s = delc("one", s)
    while 't' in s:
        rl.append("three")
        s = delc("three", s)
    while 'f' in s:
        rl.append("five")
        s = delc("five", s)
    while 's' in s:
        rl.append("seven")
        s = delc("seven", s)
    while 'i' in s:
        rl.append("nine")
        s = delc("nine", s)
    return s, rl

def originalDigits(s):
    numberdic = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    rl = []
    numlist = []
    numstr = ""

    startlen = len(s)
    s, rl = check(rl, s)
    endlen = len(s)

    if startlen == endlen and endlen != 0:
        return s

    for i in rl:
        for j in numberdic.keys():
            if i == j:
                numlist.append(numberdic[j])
    numlist.sort()
    for i in numlist:
        numstr += str(i)
    return numstr

s = "owoztneoer"
#s = "fviefuro"
print(originalDigits(s))
