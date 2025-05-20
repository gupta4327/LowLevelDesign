from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.observable_intfce import ObservableInterface

class ObserverInterface(ABC):

    def __init__(self, observable: 'ObservableInterface'):
        self.observable = observable

    @abstractmethod
    def update(self):
        pass