import SudokuConstants as SCS
from Value import Value
from AllowedValues import ContainsAllowedValues
 
class Field(ContainsAllowedValues):
    def __init__(self, value = SCS.INITIAL):
        super().__init__()
        self._value = Value(value)
        self._row    = None
        self._column = None
        self._block  = None
    @property
    def value(self):
        return self._value.value
    @value.setter
    def value(self, newvalue):
        self._value.value = newvalue
    def _addInfluencingFields(self, fields):        
        if len(fields) != SCS.BOARDSIZE:
            raise SCS.INVALIDFIELDSEXCEPTION
        if not self in fields:
            raise SCS.INVALIDFIELDSEXCEPTION2
        for field in fields:
            if field != self:
                self.ObserveValue(field._value)
    @property
    def Row(self):
        return self._row
    @Row.setter
    def Row(self, rowFields):
        self._row = rowFields
        self._addInfluencingFields(rowFields.fields)        
    @property
    def Column(self):
        return self._column
    @Column.setter
    def Column(self, columnFields):
        self._column = columnFields
        self._addInfluencingFields(columnFields.fields)        
    @property
    def Block(self):
        return self._block
    @Block.setter
    def Block(self, blockFields):
        self._block = blockFields
        self._addInfluencingFields(blockFields.fields)
    def fixValue(self):
        self._value._fixedValue = True        
    def unfixValue(self):
        self._value._fixedValue = False        
    def clear(self):
        self._value.clear()
        