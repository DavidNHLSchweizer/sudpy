import SudokuConstants
from observerPattern import SimpleSubject, Observer
from typing import List

class Value(SimpleSubject):
    def _checkLegalValue(self, value):
        if not (SudokuConstants.IsClear(value) or (value >= 1 and value <= SudokuConstants.BOARDSIZE)):
            raise ValueError(SudokuConstants.INVALIDVALUEEXCEPTION + ' {}'.format(value))        
 
    def __init__(self, value=SudokuConstants.INITIAL):
        super().__init__()
        self._checkLegalValue(value)
        self._value = value
        self._oldvalue = SudokuConstants.INITIAL
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, newvalue):
        if (self.value == newvalue):
            return
        self._checkLegalValue(newvalue)
        self._oldvalue = self._value
        self._value = newvalue
        self.notify()
    @property
    def oldvalue(self):
        return self._oldvalue
    def clear(self):
        self.value = SudokuConstants.INITIAL

class AllowedValues(Observer):
    def __init__(self):
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
    def addValue(self, value):
        value.attach(self)
        self._removeValue(value.value)
    def update(self, value):
        self._addValue(value.oldvalue)
        self._removeValue(value.value)
    def IsAllowedValue(self, value):
        return value in self._allowedValues
    def GetAllowedValues(self):
        return sorted(self._allowedValues)
