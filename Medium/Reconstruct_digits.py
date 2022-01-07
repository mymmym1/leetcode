# digits in ascending order
# s is guaranteed to be valid.

def originalDigits(s):
    numberdic = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    resultlist = []
    numlist = []
    numstr = ""
    if 'z' in s:
        resultlist.append("zero")
        s = s.replace('z', '', 1)
        s = s.replace('e', '', 1)
        s = s.replace('r', '', 1)
        s = s.replace('o', '', 1)
    if 'w' in s:
        resultlist.append("two")
        s = s.replace('t', '', 1)
        s = s.replace('w', '', 1)
        s = s.replace('o', '', 1)
    if 'u' in s:
        resultlist.append("four")
        s = s.replace('f', '', 1)
        s = s.replace('o', '', 1)
        s = s.replace('u', '', 1)
        s = s.replace('r', '', 1)
    if 'x' in s:
        resultlist.append("six")
        s = s.replace('s', '', 1)
        s = s.replace('i', '', 1)
        s = s.replace('x', '', 1)
    if 'g' in s:
        resultlist.append("eight")
        s = s.replace('e', '', 1)
        s = s.replace('i', '', 1)
        s = s.replace('g', '', 1)
        s = s.replace('h', '', 1)
        s = s.replace('t', '', 1)
    # Now take care of the rest
    if 'o' in s:
        resultlist.append("one")
        s = s.replace('o', '', 1)
        s = s.replace('n', '', 1)
        s = s.replace('e', '', 1)
    if 't' in s:
        resultlist.append("three")
        s = s.replace('e', '', 2)
        s = s.replace('t', '', 1)
        s = s.replace('r', '', 1)
        s = s.replace('h', '', 1)
    if 'f' in s:
        resultlist.append("five")
        s = s.replace('f', '', 1)
        s = s.replace('i', '', 1)
        s = s.replace('v', '', 1)
        s = s.replace('e', '', 1)
    if 's' in s:
        resultlist.append("seven")
        s = s.replace('e', '', 2)
        s = s.replace('s', '', 1)
        s = s.replace('v', '', 1)
        s = s.replace('n', '', 1)
    if 'i' in s:
        resultlist.append("nine")
        s = s.replace('e', '', 1)
        s = s.replace('i', '', 1)
        s = s.replace('n', '', 2)
    for i in resultlist:
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