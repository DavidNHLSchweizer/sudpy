import SudokuConstants
from Value import Value
from observerPattern import Subject, SimpleSubject, Observer
from typing import List

class AllowedValues(Observer):
    def __init__(self):
        super(AllowedValues, self).__init__()
        self._allowedValues: List(int) = []
        self._refCount = [0]
        for i in range(1, SudokuConstants.BOARDSIZE+1):
            self._allowedValues.append(i)
            self._refCount.append(0)
    def _addValue(self, value):
        if not SudokuConstants.IsClear(value):
            self._refCount[value] -= 1
            if self._refCount[value] < 0:
                raise ValueError(SudokuConstants.INVALIDREFCOUNTEXCEPTION + ' {} (value {})'.format(self._refCount[value], value))
            if self._refCount[value] == 0 and not value in self._allowedValues:
                self._allowedValues.append(value)
    def _removeValue(self, value):
        self._refCount[value] += 1
        if value in self._allowedValues:
            self._allowedValues.remove(value)
    def ObserveValue(self, value: Value):
        value.attach(self)
        self._removeValue(value.value)
    def StopObserveValue(self, value: Value):
        self._addValue(value.value)
        value.detach(self)
    def update(self, subject: Value):
        self._addValue(subject.oldvalue)
        self._removeValue(subject.value)
    def IsAllowedValue(self, value):
        return value == SudokuConstants.INITIAL or value in self._allowedValues
    def GetAllowedValues(self):
        return sorted(self._allowedValues)    
    def nrAllowedValues(self):
        return len(self._allowedValues)

class ContainsAllowedValues:
    def __init__(self):
        self.allowedValues = AllowedValues()
    def IsAllowedValue(self, value):
        return self.allowedValues.IsAllowedValue(value)
    def GetAllowedValues(self):
        return self.allowedValues.GetAllowedValues()
    def nrAllowedValues(self):
        return self.allowedValues.nrAllowedValues()
    def ObserveValue(self, value: Value):
        self.allowedValues.ObserveValue(value)