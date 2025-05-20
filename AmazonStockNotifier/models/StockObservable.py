from models.observable_intfce import ObservableInterface
from models.observer_intfce import ObserverInterface

class ProductStockObservable(ObservableInterface):

    def __init__(self, product_id):
        self.observers = []
        self.stock_count = 0
        self.product_id = product_id

    def add_observer(self, observer: ObserverInterface):
        self.observers.append(observer)

    def remove_observer(self, observer):
        return self.observers.remove(observer)        
    
    def notify_all(self):
        for observer in self.observers:
            observer.update()

    def get_data(self) ->int :
        return f"Stock available for product : {self.product_id} - {self.stock_count}"

    def set_data(self, stock:int):
        if self.stock_count == 0:
            self.stock_count = self.stock_count + stock
            self.notify_all()
        else:
            self.stock_count = self.stock_count + stock
