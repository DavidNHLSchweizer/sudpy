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
                self.allowedValues.addValue(field.value)
    @property
    def Row(self):
        return self._row
    @Row.setter
    def Row(self, rowFields):
        self._row = rowFields
        self._addInfluencingFields(rowFields)        
    @property
    def Column(self):
        return self._column
    @Column.setter
    def Column(self, columnFields):
        self._column = columnFields
        self._addInfluencingFields(columnFields)        
    @property
    def Block(self):
        return self._block
    @Block.setter
    def Block(self, blockFields):
        self._block = blockFields
        self._addInfluencingFields(blockFields)        
    def clear(self):
        self._value.clear()
        
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
    def _RowColToIndex(self, row, col):
        return row * self.nCols + col
    def _IndexToRow(self, index):
        return index // self.nCols
    def _IndexToCol(self, index):
        return index % self.nCols
    def field(self, row, col):
        return self.fields[self._RowColToIndex(row, col)]
    def fieldRow(self, field):
        return self._IndexToRow(self._GetIndex(field))
    def fieldCol(self, field):
        return self._IndexToCol(self._GetIndex(field))
    @property
    def nCols(self):
        return self._nCols
    @nCols.setter
    def nCols(self, value):
        if value <= 0 or value > len(self.fields) or len(self.fields) % value != 0:
            raise ValueError(SudokuConstants.INVALIDCOLSEXCEPTION + ' {}'.format(value))
        self._nCols = value
        
class Board(Fields):
    def __init__(self):
        super().__init__()
        self._init_fields()
        self._init_Rows()
        self._init_Cols()
        self._init_Blocks()
        self._updateFields()
    def _init_fields(self):
        for _ in range(SudokuConstants.BOARDSIZE):            
            for _ in range(SudokuConstants.BOARDSIZE):
                self.addField(Field())
        self.nCols = SudokuConstants.BOARDSIZE
    def _init_Rows(self):
        self.Rows = []
        for r in range(SudokuConstants.BOARDSIZE):
            Row = Fields()
            for c in range(SudokuConstants.BOARDSIZE):
                Row.addField(self.field(r, c))
            Row.nCols = SudokuConstants.BOARDSIZE
            self.Rows.append(Row)
    def _init_Cols(self):
        self.Cols = []
        for c in range(SudokuConstants.BOARDSIZE):
            Col = Fields()
            for r in range(SudokuConstants.BOARDSIZE):
                Col.addField(self.field(r, c))
            Col.nCols = 1
            self.Cols.append(Col)
    def _init_Blocks(self):
        self.Blocks = []
        for bRow in range(SudokuConstants.BLOCKSIZE):
            r0 = bRow * SudokuConstants.BLOCKSIZE
            BlockRow = []
            for bCol in range(SudokuConstants.BLOCKSIZE):
                c0 = bCol * SudokuConstants.BLOCKSIZE
                Block = Fields()
                for r in range(r0, r0+SudokuConstants.BLOCKSIZE):
                    for c in range(c0, c0+SudokuConstants.BLOCKSIZE):
                        Block.addField(self.field(r, c))`
                Block.nCols = SudokuConstants.BLOCKSIZE
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

