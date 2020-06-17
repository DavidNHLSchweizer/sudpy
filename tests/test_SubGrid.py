import pytest
import SudokuConstants as SCS
from Square import Square
from Squares import Squares
from SubGrid import Row, Column, Block

class TestSubGrids:
    def _buildSingleSquares(self):
        self.singleSquares = []
        for i in range(1,SCS.GRIDSIZE+1):
            self.singleSquares.append(Square(i))
        return self.singleSquares

    def _test_SubGrid_initial(self, subgrid):
        assert subgrid.nSquares == SCS.GRIDSIZE
        for r in range(subgrid.nRows):
            for c in range(subgrid.nCols):
                square = subgrid.square(r,c)
                assert square.GetAllowedValues() == [square.value]

    def _test_SubGrid_values_toggle(self, subgrid):
        for r in range(subgrid.nRows):
            for c in range(subgrid.nCols):
                square = subgrid.square(r,c)
                val = square.value
                square.clear()
                for square2 in subgrid.squares:
                    if not square == square2:
                        assert square2.GetAllowedValues() == sorted([val, square2.value])
                square.value = val
                for square2 in subgrid.squares:
                    if not square == square2:
                        assert square2.GetAllowedValues() == [square2.value]

    def test_Row_initial(self):
        testRow = Row(self._buildSingleSquares())
        assert testRow.nRows == 1
        assert testRow.nCols == SCS.GRIDSIZE
        self._test_SubGrid_initial(testRow)

    def test_Row_values_toggle(self):
        self._test_SubGrid_values_toggle(Row(self._buildSingleSquares()))

    def test_Column_initial(self):
        testColumn = Column(self._buildSingleSquares())
        assert testColumn.nRows == SCS.GRIDSIZE
        assert testColumn.nCols == 1
        self._test_SubGrid_initial(testColumn)

    def test_Column_values_toggle(self):
        self._test_SubGrid_values_toggle(Column(self._buildSingleSquares()))

    def test_Block_initial(self):
        testBlock = Block(self._buildSingleSquares())
        assert testBlock.nRows == SCS.BLOCKSIZE
        assert testBlock.nCols == SCS.BLOCKSIZE
        self._test_SubGrid_initial(testBlock)

    def test_Block_values_toggle(self):
        self._test_SubGrid_values_toggle(Block(self._buildSingleSquares()))

