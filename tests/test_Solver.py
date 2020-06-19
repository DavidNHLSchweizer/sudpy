import pytest
from Grid import Grid
from GridImporter import GridImporterFromArray
from Solver import Solver, SolveStrategy

class FakeSolverTrue(SolveStrategy):
    def Solve(self, grid: Grid)->bool:
        return True

class Test_Solver:
    def _test_InvalidSudoku(self, sudokuAsArray):
        grid = GridImporterFromArray(sudokuAsArray).grid
        assert Solver().Solve(grid, FakeSolverTrue()) == False

# testcases from http://sudopedia.enjoysudoku.com/Invalid_Test_Cases.html

    def test_InvalidSudoku_Empty(self):
        self._test_InvalidSudoku([
                                '. . . | . . . | . . .',
                                '. . . | . . . | . . .',
                                '. . . | . . . | . . .',
                                '------+-------+------',
                                '. . . | . . . | . . .',
                                '. . . | . . . | . . .',
                                '. . . | . . . | . . .',
                                '------+-------+------',
                                '. . . | . . . | . . .',
                                '. . . | . . . | . . .',
                                '. . . | . . . | . . .'
                                ])

    def test_InvalidSudoku_SingleGiven(self):
        self._test_InvalidSudoku([
                                '. . . | . . . | . . .',
                                '. . . | . . . | . . .',
                                '. . . | . . . | . . .',
                                '------+-------+------',
                                '. . . | . . . | . . .',
                                '. . . | . 1 . | . . .',
                                '. . . | . . . | . . .',
                                '------+-------+------',
                                '. . . | . . . | . . .',
                                '. . . | . . . | . . .',
                                '. . . | . . . | . . .'
                                ])

    def test_InvalidSudoku_InsufficientGiven(self):
        self._test_InvalidSudoku([
                                '. . . | . . . | . . .',
                                '. . 5 | . . . | . 9 .',
                                '. . 4 | . . . | . 1 .',
                                '------+-------+------',
                                '2 . . | . . 3 | . 5 .',
                                '. . . | 7 . . | . . .',
                                '4 3 8 | . . . | 2 . .',
                                '------+-------+------',
                                '. . . | . 9 . | . . .',
                                '. 1 . | 4 . . | . 6 .',
                                '. . . | . . . | . . .'
                                ])

