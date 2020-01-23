import SudokuConstants
from abc import abstractmethod
from observerPattern import SimpleSubject, Observer

class ValueSubject(SimpleSubject):
    def _checkLegalValue(self, value):
        if not (SudokuConstants.IsClear(value) or (value >= 1 and value <= SudokuConstants.BOARDSIZE)):
            raise ValueError(SudokuConstants.INVALIDVALUEEXCEPTION + ' {}'.format(value))        
    @abstractmethod
    def getValue(self)->int:
        pass    
    @property
    def value(self):
        return self.getValue()
    @abstractmethod
    def setValue(self, value):
        pass
    @value.setter
    def value(self, newvalue):
        if (self.value == newvalue):
            return
        self._checkLegalValue(newvalue)
        self.setValue(newvalue)
        self.notify()
    @abstractmethod
    def getOldValue(self)->int:
        pass    
    @property
    def oldvalue(self):
        return self.getOldValue()    

class Value(ValueSubject):
    def __init__(self, value=SudokuConstants.INITIAL):
        super().__init__()
        self._checkLegalValue(value)
        self._value = value
        self._oldvalue = SudokuConstants.INITIAL
    def getValue(self)->int:
        return self._value
    def setValue(self, newvalue):
        self._oldvalue = self._value
        self._value = newvalue
    def getOldValue(self)->int:
        return self._oldvalue
    def clear(self):
        self.value = SudokuConstants.INITIAL
        self._oldvalue = SudokuConstants.INITIAL
