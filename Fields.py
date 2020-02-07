import SudokuConstants
from Value import Value
from AllowedValues import AllowedValues

class Field:
    def __init__(self, value = SudokuConstants.INITIAL):
        self._value = Value(value)
        self._row    = None
        self._column = None
        self._block  = None
        self.allowedValues = AllowedValues()
    @property
    def value(self):
        return self._value.value
    @value.setter
    def value(self, newvalue):
        self._value.value = newvalue
    def _addInfluencingFields(self, fields):        
        if len(fields) != SudokuConstants.BOARDSIZE:
            raise SudokuConstants.INVALIDFIELDSEXCEPTION
        if not self in fields:
            raise SudokuConstants.INVALIDFIELDSEXCEPTION2
        for field in fields:
            if field != self:
                self.allowedValues.addValue(field._value)
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
    def clear(self):
        self._value.clear()
    def IsAllowedValue(self, value):
        return self.allowedValues.IsAllowedValue(value)
    def GetAllowedValues(self):
        return self.allowedValues.GetAllowedValues()
        
class Fields:
    def __init__(self):
        self.fields = []
        self.allowedValues = AllowedValues()
        self._nCols = 0
    def addField(self, field: Field):
        self.fields.append(field)
        self.allowedValues.addValue(field._value)   
        self._nCols += 1
    def addFields(self, fields):
        for field in fields: 
            self.addField(field)
    def IsAllowedValue(self, value):
        return self.allowedValues.IsAllowedValue(value)
    def GetAllowedValues(self):
        return self.allowedValues.GetAllowedValues()
    def _GetIndex(self, field):
        if not field in self.fields:
            return SudokuConstants.INDEXNOTFOUND        
        return self.fields.index(field)
    def _Contains(self, field):
        return field in self.fields
    def _RowColToIndex(self, row, col):
        return row * self.nCols + col
    def _IndexToRow(self, index):
        return index // self.nCols
    def _IndexToCol(self, index):
        return index % self.nCols
    def _CheckLegal(self, row, col):
        if row < 0 or row >= self.nRows:
            ValueError(SudokuConstants.INVALIDROWSEXCEPTION + ' {}'.format(row))
        if col < 0 or col >= self.nCols:
            ValueError(SudokuConstants.INVALIDCOLSEXCEPTION + ' {}'.format(col))
    def field(self, row, col):
        self._CheckLegal(row, col)
        return self.fields[self._RowColToIndex(row, col)]
    def fieldRow(self, field):
        return self._IndexToRow(self._GetIndex(field))
    def fieldCol(self, field):
        return self._IndexToCol(self._GetIndex(field))
    @property
    def nCols(self)->int:
        return self._nCols
    @nCols.setter
    def nCols(self, value):
        if value <= 0 or value > len(self.fields) or len(self.fields) % value != 0:
            raise ValueError(SudokuConstants.INVALIDCOLSEXCEPTION + ' {}'.format(value))
        self._nCols = value
    @property
    def nRows(self)->int:
        return len(self.fields) // self.nCols
        
