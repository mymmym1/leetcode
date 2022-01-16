def countRMs(intervals):
    count = 0
    if len(intervals) == 1:
        return 1
    if len(intervals) == 0:
        return 0
    for i in range(len(intervals)):
        for j in range(len(intervals)):
            if j > i:
                if intervals[j][1] - intervals[i][1] < 0:
                    if intervals[j][1] - intervals[i][0] >= 0:
                        count += 1
                else:
                    if intervals[j][0] - intervals[i][1] < 0:
                        count += 1
    return count

intervals = [(0,30),(5,10),(15,20)]
intervals = [(2,7)]
print(countRMs(intervals))
