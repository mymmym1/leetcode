def findContentChildren(g, s):
    g.sort()
    s.sort()
    l = min(len(g), len(s))
    count = 0
    for i in range(l):
        if s[i]>=g[i]:
            count += 1
    return count

g = [1,2,3]
s = [1,1]
#g = [1,2]
#s = [1,2,3]
print(findContentChildren(g, s))