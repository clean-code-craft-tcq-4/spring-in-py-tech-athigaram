import math as maths

def avg(numbers):
    return sum(numbers)/len(numbers)

def calculateStats(numbers):
    if not numbers or any(maths.isnan(number) for number in numbers):
        return statsAssigner(maths.nan,maths.nan,maths.nan)
    else:
        return statsAssigner(avg(numbers),min(numbers),max(numbers))

def statsAssigner(stats_avg,stats_min,stats_max):
    computedStats = {}
    computedStats['avg']= stats_avg
    computedStats['min']= stats_min
    computedStats['max']= stats_max
    return computedStats
