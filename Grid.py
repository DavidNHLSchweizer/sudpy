import SudokuConstants as SCS
from Square import Square
from Squares import Squares
from SubGrid import Row, Column, Block

class Grid(Squares):
    def __init__(self):
        super().__init__()
        self._init_squares()
        self._init_Rows()
        self._init_Cols()
        self._init_Blocks()
    def _init_squares(self):
        for _ in range(SCS.GRIDSIZE):            
            for _ in range(SCS.GRIDSIZE):
                self.addSquare(Square())
        self.nCols = SCS.GRIDSIZE
        self.nRows = SCS.GRIDSIZE
    def _init_Rows(self):
        self.Rows = []
        for r in range(self.nRows):
            rowArray = []
            for c in range(self.nCols):
                rowArray.append(self.square(r, c))
            self.Rows.append(Row(rowArray))
    def _init_Cols(self):
        self.Cols = []
        for c in range(self.nCols):
            colArray = []
            for r in range(self.nRows):
                colArray.append(self.square(r, c))
            self.Cols.append(Column(colArray))
    def _init_Blocks(self):
        self.Blocks = []
        for bRow in range(self.nBlockRows):
            r0 = bRow * self.nBlockRows
            BlockRow = []
            for bCol in range(self.nBlockCols):
                c0 = bCol * self.nBlockCols
                blkArray = []
                for r in range(r0, r0+self.nBlockRows):
                    for c in range(c0, c0+self.nBlockCols):
                        blkArray.append(self.square(r, c))
                BlockRow.append(Block(blkArray))
            self.Blocks.append(BlockRow)
    def Row(self, row):
        self._CheckLegal(row, 0)
        return self.Rows[row]
    def Column(self, col):
        self._CheckLegal(0, col)
        return self.Cols[col]
    def BlockFromSquare(self, row, col):
        self._CheckLegal(row, col)
        return self.Blocks[row // self.nBlockRows][col // self.nBlockCols]
    def sqBlock(self, square):
        return self.BlockFromSquare(self.sqRow(square), self.sqCol(square))
    def Block(self, bRow, bCol):
        self._CheckLegalBase(bRow, bCol, self.nBlockRows, self.nBlockCols)
        return self.Blocks[bRow][bCol]
    @property
    def nBlockRows(self):
        return SCS.BLOCKSIZE
    @property
    def nBlockCols(self):
        return SCS.BLOCKSIZE
    @property
    def nBlocks(self):
        return self.nBlockRows * self.nBlockCols
    def clear(self):
        for square in self.squares:
            square.clear()
    if __debug__:
        def _dbg_print(self):
            for r in range(self.nRows):
                s = '{}:'.format(r+1)
                for c in range(self.nCols):
                    s = s + '{} '.format(self.square(r,c).dbgIndex)
                print(s)
