from models.observer_intfce import ObserverInterface
from models.observable_intfce import ObservableInterface

class SMSNotifier(ObserverInterface):

    def __init__(self, observable: ObservableInterface): 
        self.observable = observable

    def update(self):
        #sms logic will be written here    
        print(f"SMS Notification sent : {self.observable.get_data()}")
