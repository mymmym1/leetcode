def merge(intervals):
    numset = set()
    result = []
    for n in intervals:
        for i in range(n[0],n[1]+1):
            if i not in numset:
                numset.add(i)
    #print(numset)
    numlist = list(numset)
    i = 0
    while i <= len(numlist) - 1:
        j = i
        while j + 1 <= len(numlist) - 1:
            if numlist[j+1] - numlist[j] == 1:
                j += 1
                if j == len(numlist) - 1:
                    result.append([numlist[i], numlist[j]])
                    break
            elif numlist[j+1] - numlist[j] > 1:
                result.append([numlist[i], numlist[j]])
                break
        i = j + 1
        if i == len(numlist) - 1:
            result.append([numlist[i], numlist[i]])
    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
print(merge(intervals))
