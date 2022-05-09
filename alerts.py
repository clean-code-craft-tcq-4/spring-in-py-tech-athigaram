#interface for all Alert type of objects
class Alert:
    def alert(self):
        print("""Sending Alert""")
        pass

# Class for Mail Alert 
class EmailAlert(Alert):
    def __init__(self):
        self.emailSent = False
    def alert(self):
        print("""Sending mail alert""")
        self.emailSent = True

# Class for Mail Alert 
class LEDAlert(Alert):
    def __init__(self):
        self.ledGlows = False
    def alert(self):
        print("""Sending LED alert""")
        self.ledGlows = True

# Class for Status Alert           
class StatsAlerter:
    def __init__(self,maxThreshold,alerts=[]):
        self.maxThreshold = maxThreshold
        self.alerts = alerts
    
    def checkAndAlert(self,numbers):
        if (max(numbers)>self.maxThreshold):
            # iterating all type of alerts and triggering alerts.
            for alert in self.alerts:
                # checking the object type before triggering alert
                if(isinstance(alert,Alert)):
                    alert.alert();
                else :
                    print(str(type(alert))+ " is not a alert type object.")
