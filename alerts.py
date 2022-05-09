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
