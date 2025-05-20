from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.observer_intfce import ObserverInterface

class ObservableInterface(ABC):

    def __init__(self):
        self.observers = list['ObserverInterface']


    @abstractmethod
    def add_observer(self, observer: 'ObserverInterface'):
        pass
    
    @abstractmethod
    def remove_observer(self, observer: 'ObserverInterface'):
        pass

    @abstractmethod
    def notify_all(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self):
        pass