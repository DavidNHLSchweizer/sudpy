import SudokuConstants as SCS
from Value import Value
from AllowedValues import ContainsAllowedValues
 
class Square(ContainsAllowedValues):
    if __debug__:
        dbgIndex = 0        
    def __init__(self, value = SCS.INITIAL):
        super().__init__()
        self._value = Value(value)
        if __debug__:
            self.dbgIndex = Square.dbgIndex
            Square.dbgIndex += 1            
    @property
    def value(self):
        return self._value.value
    @value.setter
    def value(self, newvalue):
        self._value.value = newvalue
    def fixValue(self):
        self._value._fixedValue = True        
    def unfixValue(self):
        self._value._fixedValue = False        
    def clear(self):
        self._value.clear()
        