import SudokuConstants as SCS
from Field import Field
from Fields import Fields

class Board(Fields):
    def __init__(self):
        super().__init__()
        self._init_fields()
        self._init_Rows()
        self._init_Cols()
        self._init_Blocks()
        self._initFieldDependencies()        
    def _init_fields(self):
        for _ in range(SCS.BOARDSIZE):            
            for _ in range(SCS.BOARDSIZE):
                self.addField(Field())
        self.nCols = SCS.BOARDSIZE
    def _init_Rows(self):
        self.Rows = []
        for r in range(SCS.BOARDSIZE):
            Row = Fields()
            for c in range(SCS.BOARDSIZE):
                Row.addField(self.field(r, c))
            Row.nCols = SCS.BOARDSIZE
            self.Rows.append(Row)
    def _init_Cols(self):
        self.Cols = []
        for c in range(SCS.BOARDSIZE):
            Col = Fields()
            for r in range(SCS.BOARDSIZE):
                Col.addField(self.field(r, c))
            Col.nCols = 1
            self.Cols.append(Col)
    def _init_Blocks(self):
        self.Blocks = []
        for bRow in range(SCS.BLOCKSIZE):
            r0 = bRow * SCS.BLOCKSIZE
            BlockRow = []
            for bCol in range(SCS.BLOCKSIZE):
                c0 = bCol * SCS.BLOCKSIZE
                Block = Fields()
                for r in range(r0, r0+SCS.BLOCKSIZE):
                    for c in range(c0, c0+SCS.BLOCKSIZE):
                        Block.addField(self.field(r, c))
                Block.nCols = SCS.BLOCKSIZE
                BlockRow.append(Block)
            self.Blocks.append(BlockRow)
    def _getBlock(self, row, col):
        self._CheckLegal(row, col)
        return self.Blocks[row // SCS.BLOCKSIZE][col // SCS.BLOCKSIZE]
    def _initFieldDependencies(self):        
        for field in self.fields:
            row = self.fieldRow(field)
            col = self.fieldCol(field)
            field.Row = self.Row(row)
            field.Column = self.Column(col)
            field.Block = self._getBlock(row,col)    
    def Row(self, row):
        self._CheckLegal(row, 0)
        return self.Rows[row]
    def Column(self, col):
        self._CheckLegal(0, col)
        return self.Cols[col]
    def Block(self, bRow, bCol):
        self._CheckLegalBase(bRow, bCol, SCS.BLOCKSIZE, SCS.BLOCKSIZE)
        return self.Blocks[bRow][bCol]
    def clear(self):
        for r in self.Rows:
            r.clear()
