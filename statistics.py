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

class Alert:
    def alert(self):
        print("""Sending Alert""")
        pass
    
class EmailAlert(Alert):
    def __init__(self):
        self.emailSent = False
    def alert(self):
        print("""Sending mail alert""")
        self.emailSent = True

class LEDAlert(Alert):
    def __init__(self):
        self.ledGlows = False
    def alert(self):
        print("""Sending LED alert""")
        self.ledGlows = True
          
class StatsAlerter:
    def __init__(self,maxThreshold,alerts=[]):
        self.maxThreshold = maxThreshold
        self.alerts = alerts
    
    def checkAndAlert(self,numbers):
        if (max(numbers)>self.maxThreshold):
            for alert in self.alerts:
                    alert.alert();
