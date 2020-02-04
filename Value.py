import SudokuConstants
from abc import abstractmethod
from observerPattern import SimpleSubject, Observer

class Value(SimpleSubject):
    def __init__(self, value=SudokuConstants.INITIAL):
        super().__init__()
        self._checkLegalValue(value)
        self._value = value
        self._oldvalue = SudokuConstants.INITIAL
    def _checkLegalValue(self, value):
        if not (SudokuConstants.IsClear(value) or (value >= 1 and value <= SudokuConstants.BOARDSIZE)):
            raise ValueError(SudokuConstants.INVALIDVALUEEXCEPTION + ' {}'.format(value))        
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
    def clear(self):
        self.value = SudokuConstants.INITIAL
        self._oldvalue = SudokuConstants.INITIAL
    @property
    def oldvalue(self):
        return self._oldvalue
