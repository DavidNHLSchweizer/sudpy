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
        totalSize = (maxRow - minRow + 1) * (maxCol - minCol + 1)
        if  totalSize != SudokuConstants.BOARDSIZE and totalSize != SudokuConstants.BOARDSIZE * SudokuConstants.BOARDSIZE:
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
    def clear(self):
        self._value.clear()
    def dump(self):
        print("Field: value " + str(self.value))
        
class Fields:
    def __init__(self, rowcol: RowCol = None):
        self.fields = []
        self.rowCol = rowcol
        self.allowedValues = AllowedValues()
    def addField(self, field: Field):
        #if len(self.fields) >= SudokuConstants.BOARDSIZE:
         #   raise ValueError(SudokuConstants.INVALIDSIZEEXCEPTION)
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
    def field(self, row, col):
        if self.rowCol == None or not self.rowCol.IsInRange(row, col):
            return None        
        return self.fields[row * self.nCols + col]
        
class Board(Fields):
    def __init__(self):
        super().__init__(RowCol(0,SudokuConstants.BOARDSIZE, 0, SudokuConstants.BOARDSIZE))
        self._init_fields()
        self._init_Rows()
        self._init_Cols()
        self._init_Blocks()
        self._updateFields()
    def _init_fields(self):
        for _ in range(SudokuConstants.BOARDSIZE):            
            for _ in range(SudokuConstants.BOARDSIZE):
                self.addField(Field())
    def _init_Rows(self):
        self.Rows = []
        for r in range(SudokuConstants.BOARDSIZE):
            Row = Fields(RowCol(r, 1, 0, SudokuConstants.BOARDSIZE))
            for c in range(SudokuConstants.BOARDSIZE):
                Row.addField(self.field(r, c))
            self.Rows.append(Row)
    def _init_Cols(self):
        self.Cols = []
        for c in range(SudokuConstants.BOARDSIZE):
            Col = Fields(RowCol(0, SudokuConstants.BOARDSIZE, c, 1))
            for r in range(SudokuConstants.BOARDSIZE):
                Col.addField(self.field(r, c))
            self.Cols.append(Col)
    def _init_Blocks(self):
        self.Blocks = []
        for bRow in range(SudokuConstants.BLOCKSIZE):
            r0 = bRow * SudokuConstants.BLOCKSIZE
            BlockRow = []
            for bCol in range(SudokuConstants.BLOCKSIZE):
                c0 = bCol * SudokuConstants.BLOCKSIZE
                Block = Fields(RowCol(r0, SudokuConstants.BLOCKSIZE, c0, SudokuConstants.BLOCKSIZE))
                for r in range(r0, r0+SudokuConstants.BLOCKSIZE):
                    for c in range(c0, c0+SudokuConstants.BLOCKSIZE):
                        Block.addField(self.field(r, c))
                BlockRow.append(Block)
            self.Blocks.append(BlockRow)
    def Row(self, row):
        if not self.rowCol.IsInRange(row,0):
            return None
        return self.Rows[row]
    def Column(self, col):
        if not self.rowCol.IsInRange(0,col):
            return None
        return self.Cols[col]
    def Block(self, row, col):
        if not self.rowCol.IsInRange(row,col):
            return None
        return self.Blocks[row // SudokuConstants.BLOCKSIZE][col // SudokuConstants.BLOCKSIZE]
    def _updateFields(self):
        pass

