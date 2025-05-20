from models.observer_intfce import ObserverInterface
from models.observable_intfce import ObservableInterface

class EmailNotifier(ObserverInterface):

    def __init__(self, observable:ObservableInterface):
        self.observable = observable

    def update(self):
        #email logic will be written here
        print(f"Email notification sent :  {self.observable.get_data()}")

        