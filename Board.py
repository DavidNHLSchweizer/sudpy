from Fields import Fields
import SudokuConstants

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
                        Block.addField(self.field(r, c))
                Block.nCols = SudokuConstants.BLOCKSIZE
                BlockRow.append(Block)
            self.Blocks.append(BlockRow)
    def Row(self, row):
        self._CheckLegal(row, 0)
        return self.Rows[row]
    def Column(self, col):
        self._CheckLegal(0, col)
        return self.Cols[col]
    def Block(self, row, col):
        self._CheckLegal(row, col)
        return self.Blocks[row // SudokuConstants.BLOCKSIZE][col // SudokuConstants.BLOCKSIZE]
    def _updateFields(self):
        for field in self.fields:
            row = self.fieldRow(field)
            col = self.fieldCol(field)
            field.Row = self.Row(row)
            field.Column = self.Column(col)
            field.Block = self.Block(row,col)
        
Board()

