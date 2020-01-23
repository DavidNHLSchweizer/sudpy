import SudokuConstants
from Value import Value
from AllowedValues import AllowedValues

class Field:
    def __init__(self, value = SudokuConstants.INITIAL):
        self._value = Value(value)
        self.row = None
        self.column = None
        self.block = None
        self.allowedValues = AllowedValues()
    @property
    def value(self):
        return self._value.value
    @value.setter
    def value(self, newvalue):
        self._value.value = newvalue

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
    def __init__(self, minRow, maxRow, minCol, maxCol):
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
    def CheckValid(self, row, col):
        if row < self.minRow or row > self.maxRow:
            raise ValueError(SudokuConstants.INVALIDROWEXCEPTION + ' {}'.format(row))
        if col < self.minCol or row > self.maxCol:
            raise ValueError(SudokuConstants.INVALIDCOLEXCEPTION + ' {}'.format(col))
      
class Fields:
    def __init__(self, rowcol: RowCol = None):
        self.fields = []
        self.rowCol = rowcol
        self.allowedValues = AllowedValues()
    def addField(self, field: Field):
        if len(self.fields >= SudokuConstants.BOARDSIZE):
            raise ValueError(SudokuConstants.INVALIDSIZEEXCEPTION)
        self.fields.append(field)
        self.allowedValues.addValue(field._value)
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
        if self.rowCol == None:
            return None        
        self.rowCol.CheckValid(row, col)
        return self.fields[row * self.nCols + col]


