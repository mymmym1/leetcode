def findPoisonedDuration(timeSeries, duration):
    totaltime = 0
    for i in range(len(timeSeries)):
        if i + 1 < len(timeSeries):
            if timeSeries[i+1] - timeSeries[i] >= duration:
                totaltime += duration
            else:
                totaltime += timeSeries[i+1] - timeSeries[i]
    totaltime += duration
    return totaltime

#timeSeries = [1,4]
#duration = 2
timeSeries = [1,2]
duration = 2
print(findPoisonedDuration(timeSeries, duration))