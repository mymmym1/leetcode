# digits in ascending order
# s is guaranteed to be valid.

def delc(word, s):
    for c in word:
        s = s.replace(c, '', 1)
    return s

def check(rl, s):
    preDic = {'z':"zero", 'w':"two", 'u':"four", 'x':"six", 'g':"eight", 'o':"one", 't':"three", 'f':"five", 's':"seven", 'i':"nine"}
    for key in preDic.keys():
        while key in s:
            rl.append(preDic[key])
            s = delc(preDic[key], s)
    return s, rl

def originalDigits(s):
    numdic = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    rl = []
    numlist = []
    numstr = ""

    startlen = len(s)
    s, rl = check(rl, s)
    endlen = len(s)

    if startlen == endlen and endlen != 0:
        return s

    for i in rl:
        for j in numdic.keys():
            if i == j:
                numlist.append(numdic[j])
    numlist.sort()
    for i in numlist:
        numstr += str(i)
    return numstr

s = "owoztneoer"
#s = "fviefuro"
print(originalDigits(s))
