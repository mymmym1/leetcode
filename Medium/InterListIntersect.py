def intervalIntersection(arr1, arr2):
    i = j = 0
    result = []
    n = len(arr1)
    m = len(arr2)
    while i<n and j<m:
        l = max(arr1[i][0], arr2[j][0])
        r = min(arr1[i][1], arr2[j][1])
        if l <= r:
            result.append([l, r])
        if arr1[i][1] < arr2[j][1]:
            i += 1
        else:
            j += 1

    return result

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
#firstList = [[1,3],[5,9]]
#secondList = []
print(intervalIntersection(firstList, secondList))




