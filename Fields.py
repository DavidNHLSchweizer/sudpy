import SudokuConstants
from Value import Value
from AllowedValues import AllowedValues

class RowCol:
    def _checkLegalValue(self, minRow, maxRow, minCol, maxCol):
        if (minRow < 0 or minRow >= SudokuConstants.BOARDSIZE):
            raise ValueError(SudokuConstants.INVALIDVALUEEXCEPTION + ' row {}'.format(minRow))        
        if (maxRow < minRow or maxRow >= SudokuConstants.BOARDSIZE):
            raise ValueError(SudokuConstants.INVALIDVALUEEXCEPTION + ' row {}'.format(maxRow))        
        if (minCol < 0 or minCol >= SudokuConstants.BOARDSIZE):
            raise ValueError(SudokuConstants.INVALIDVALUEEXCEPTION + ' col {}'.format(minCol))        
        if (maxCol < minCol or maxCol >= SudokuConstants.BOARDSIZE):
            raise ValueError(SudokuConstants.INVALIDVALUEEXCEPTION + ' col {}'.format(maxCol))
        if (maxRow - minRow + 1) * (maxCol - minCol + 1) != SudokuConstants.BOARDSIZE:
            raise ValueError(SudokuConstants.INVALIDVALUEEXCEPTION + ' dimension ({},{}) ({},{})'.format(minRow, maxRow, minCol, maxCol))
    def __init__(self, minRow, nRows, minCol, nCols):
        maxRow = minRow + nRows -1
        maxCol = minCol + nCols -1
        self._checkLegalValue(minRow, maxRow, minCol, maxCol)
        self.minRow = minRow
        self.maxRow = maxRow
        self.minCol = minCol
        self.maxCol = maxCol
    @property
    def nRows(self):
        return self.maxRow - self.minRow + 1
    @property
    def nCols(self):
        return self.maxCol - self.minCol + 1
    def IsInRange(self, row, col):
        if row < self.minRow or row > self.maxRow or col < self.minCol or col > self.maxCol:
            return False
        return True
    
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
    def _addFields(self, fields):
        if len(fields) != SudokuConstants.BOARDSIZE:
            raise SudokuConstants.INVALIDFIELDSEXCEPTION
        if not self in fields:
            raise SudokuConstants.INVALIDFIELDSEXCEPTION2
        for field in fields:
            if field != self:
                self.allowedValues.addValue(field.value)
    @property
    def Row(self):
        return self._row
    @Row.setter
    def Row(self, rowFields):
        self._row = rowFields
        self._addFields(rowFields)
    @property
    def Column(self):
        return self._column
    @Column.setter
    def Column(self, columnFields):
        self._column = columnFields
        self._addFields(columnFields)
    @property
    def Block(self):
        return self._block
    @Block.setter
    def Block(self, blockFields):
        self._block = blockFields
        self._addFields(blockFields)
        
class Fields:
    def __init__(self, rowcol: RowCol = None):
        self.fields = []
        self.rowCol = rowcol
        self.allowedValues = AllowedValues()
    def addField(self, field: Field):
        if len(self.fields) >= SudokuConstants.BOARDSIZE:
            raise ValueError(SudokuConstants.INVALIDSIZEEXCEPTION)
        self.fields.append(field)
        self.allowedValues.addValue(field._value)   
    def addFields(self, fields):
        for field in fields: 
            self.addField(field)
    def IsAllowedValue(self, value):
        return self.allowedValues.IsAllowedValue(value)
    def GetAllowedValues(self):
        return self.allowedValues.GetAllowedValues()
    @property
    def nRows(self):
        if self.rowCol == None:
            return 0
        return self.rowCol.nRows
    @property
    def nCols(self):
        if self.rowCol == None:
            return 0
        return self.rowCol.nCols
    @property
    def field(self, row, col):
        if self.rowCol == None or not self.rowCol.IsInRange(row, col):
            return None        
        return self.fields[row * self.nCols + col]
        

