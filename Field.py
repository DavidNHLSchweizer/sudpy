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
    def _validateFields(self, fields):
        if not fields:
            return False
        if len(fields) != SCS.BOARDSIZE:
            raise SCS.INVALIDFIELDSEXCEPTION
        if not self in fields:
            raise SCS.INVALIDFIELDSEXCEPTION2
        return True
    def _removeInfluencingFields(self, fields):
        if not self._validateFields(fields):
            return
        for field in fields:
            if field != self:
                self.StopObserveValue(field._value)
    def _addInfluencingFields(self, fields):        
        if not self._validateFields(fields):
            return
        for field in fields:
            if field != self:
                self.ObserveValue(field._value)
    @property
    def Row(self):
        return self._row
    @Row.setter
    def Row(self, rowFields):
        if self._row:
            self._removeInfluencingFields(self._row.fields)
        self._row = rowFields
        self._addInfluencingFields(rowFields.fields)        
    @property
    def Column(self):
        return self._column
    @Column.setter
    def Column(self, columnFields):
        if self._column:
            self._removeInfluencingFields(self._column.fields)
        self._column = columnFields
        self._addInfluencingFields(columnFields.fields)        
    @property
    def Block(self):
        return self._block
    @Block.setter
    def Block(self, blockFields):
        if self._block:
            self._removeInfluencingFields(self._block.fields)
        self._block = blockFields
        self._addInfluencingFields(blockFields.fields)
    def fixValue(self):
        self._value._fixedValue = True        
    def unfixValue(self):
        self._value._fixedValue = False        
    def clear(self):
        self._value.clear()
        