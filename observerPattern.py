from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def notify(self) -> None:
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class SimpleSubject(Subject):
    def __init__(self):
        super(SimpleSubject, self).__init__()
        self.observers:List[Observer] = []
    def attach(self, observer: Observer) -> None:
        if not observer in self.observers:
            self.observers.append(observer)
    def detach(self, observer: Observer) -> None:
        if observer in self.observers:
            self.observers.remove(observer)
    def notify(self) -> None:
        for observer in self.observers:
            observer.update(self)
    def detachAll(self):
        for observer in self.observers:
            self.detach(observer)