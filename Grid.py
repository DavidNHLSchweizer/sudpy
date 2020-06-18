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
        for r in range(SCS.GRIDSIZE):
            rowArray = []
            for c in range(SCS.GRIDSIZE):
                rowArray.append(self.square(r, c))
            self.Rows.append(Row(rowArray))
    def _init_Cols(self):
        self.Cols = []
        for c in range(SCS.GRIDSIZE):
            colArray = []
            for r in range(SCS.GRIDSIZE):
                colArray.append(self.square(r, c))
            self.Cols.append(Column(colArray))
    def _init_Blocks(self):
        self.Blocks = []
        for bRow in range(SCS.BLOCKSIZE):
            r0 = bRow * SCS.BLOCKSIZE
            BlockRow = []
            for bCol in range(SCS.BLOCKSIZE):
                c0 = bCol * SCS.BLOCKSIZE
                blkArray = []
                for r in range(r0, r0+SCS.BLOCKSIZE):
                    for c in range(c0, c0+SCS.BLOCKSIZE):
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
        return self.Blocks[row // SCS.BLOCKSIZE][col // SCS.BLOCKSIZE]
    def Block(self, bRow, bCol):
        self._CheckLegalBase(bRow, bCol, SCS.BLOCKSIZE, SCS.BLOCKSIZE)
        return self.Blocks[bRow][bCol]
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
