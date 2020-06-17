import SudokuConstants as SCS
from Square import Square
from Squares import Squares

class Grid(Squares):
    def __init__(self):
        super().__init__()
        self._init_squares()
        self._init_Rows()
        self._init_Cols()
        self._init_Blocks()
        self._initSquareDependencies()        
    def _init_squares(self):
        for _ in range(SCS.GRIDSIZE):            
            for _ in range(SCS.GRIDSIZE):
                self.addSquare(Square())
        self.nCols = SCS.GRIDSIZE
    def _init_Rows(self):
        self.Rows = []
        for r in range(SCS.GRIDSIZE):
            Row = Squares()
            for c in range(SCS.GRIDSIZE):
                Row.addSquare(self.square(r, c))
            Row.nCols = SCS.GRIDSIZE
            self.Rows.append(Row)
    def _init_Cols(self):
        self.Cols = []
        for c in range(SCS.GRIDSIZE):
            Col = Squares()
            for r in range(SCS.GRIDSIZE):
                Col.addSquare(self.square(r, c))
            Col.nCols = 1
            self.Cols.append(Col)
    def _init_Blocks(self):
        self.Blocks = []
        for bRow in range(SCS.BLOCKSIZE):
            r0 = bRow * SCS.BLOCKSIZE
            BlockRow = []
            for bCol in range(SCS.BLOCKSIZE):
                c0 = bCol * SCS.BLOCKSIZE
                Block = Squares()
                for r in range(r0, r0+SCS.BLOCKSIZE):
                    for c in range(c0, c0+SCS.BLOCKSIZE):
                        Block.addSquare(self.square(r, c))
                Block.nCols = SCS.BLOCKSIZE
                BlockRow.append(Block)
            self.Blocks.append(BlockRow)
    def _getBlock(self, row, col):
        self._CheckLegal(row, col)
        return self.Blocks[row // SCS.BLOCKSIZE][col // SCS.BLOCKSIZE]
    def _initSquareDependencies(self):        
        for square in self.squares:
            row = self.sqRow(square)
            col = self.sqCol(square)
            square.Row = self.Row(row)
            square.Column = self.Column(col)
            square.Block = self._getBlock(row,col)    
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