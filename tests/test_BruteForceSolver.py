import pytest
from GridImporter import GridImporterFromArray
from Solver import Solver
from bruteForceSolver import BruteForceSolver

class TestBruteForceSolver:
    def _test_InvalidSudoku(self, sudokuAsArray):
        grid = GridImporterFromArray(sudokuAsArray).grid
        assert Solver().Solve(grid, BruteForceSolver()) == False

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

    def test_InvalidSudoku_DuplicateGiven_Box(self):
        self._test_InvalidSudoku([
                                '. . 9 | . 7 . | . . 5',
                                '. . 2 | 1 . . | 9 . .',
                                '1 . . | . 2 8 | . . .',
                                '------+-------+------',
                                '. 7 . | . . 5 | . . 1',
                                '. . 8 | 5 1 . | . . .',
                                '. 5 . | . . . | 3 . .',
                                '------+-------+------',
                                '. . . | . . 3 | . . 6',
                                '8 . . | . . . | . . .',
                                '2 1 . | . . . | . 8 7'
                                ])

    def test_InvalidSudoku_DuplicateGiven_Column(self):
        self._test_InvalidSudoku([
                                '6 . 1 | 5 9 . | . . .',
                                '. 9 . | . 1 . | . . .',
                                '. . . | . . . | . . 4',
                                '------+-------+------',
                                '. 7 . | 3 1 4 | . . 6',
                                '. 2 4 | . . . | . . 5',
                                '. . 3 | . . . | . 1 .',
                                '------+-------+------',
                                '. . 6 | . . . | . . 3',
                                '. . . | 9 . 2 | . 4 .',
                                '. . . | . . 1 | 6 . .'
                                ])
    def test_InvalidSudoku_DuplicateGiven_Row(self):
        self._test_InvalidSudoku([
                                '. 4 . | 1 . . | 3 5 .',
                                '. . . | . . . | . . .',
                                '. . . | 2 . 5 | . . .',
                                '------+-------+------',
                                '. . . | 4 . 8 | 9 . .',
                                '2 6 . | . . . | . 1 2',
                                '. 5 . | 3 . . | . . 7',
                                '------+-------+------',
                                '. . 4 | . . . | 1 6 .',
                                '6 . . | . . 7 | . . .',
                                '. 1 . | . 8 . | . 2 .'
                                ])

    def test_InvalidSudoku_Unsolvable_Square(self):
        self._test_InvalidSudoku([
                                '. . 9 | . 2 8 | 7 . .',
                                '8 . 6 | . . 4 | . . 5',
                                '. . 3 | . . . | . . 4',
                                '------+-------+------',
                                '6 . . | . . . | . . .',
                                '. 2 . | 7 1 3 | 4 5 .',
                                '. . . | . . . | . . 2',
                                '------+-------+------',
                                '3 . . | . . . | 5 . .',
                                '9 . . | 4 . . | 8 . 7',
                                '. . 1 | 2 5 . | 3 . .'
                                ])
       
    def test_InvalidSudoku_Unsolvable_Box(self):
        self._test_InvalidSudoku([
                                '. 9 . | 3 . . | . . 1',
                                '. . . | . 8 . | . 4 6',
                                '. . . | . . . | 8 . .',
                                '------+-------+------',
                                '4 . 5 | . 6 . | . 3 .',
                                '. . 3 | 2 7 5 | 6 . .',
                                '. 6 . | . 1 . | 9 . 4',
                                '------+-------+------',
                                '. . 1 | . . . | . . .',
                                '5 8 . | . 2 . | . . .',
                                '2 . . | . . 7 | . 6 .'                                
                                ])
    def test_InvalidSudoku_Unsolvable_Column(self):
        self._test_InvalidSudoku([
                                '. . . | . 4 1 | . . .',
                                '. 6 . | . . . | . 2 .',
                                '. . 2 | . . . | . . .',
                                '------+-------+------',
                                '3 2 . | 6 . . | . . .',
                                '. . . | . 5 . | . 4 1',
                                '7 . . | . . . | . . 2',
                                '------+-------+------',
                                '. . . | . . . | 2 3 .',
                                '. 4 8 | . . . | . . .',
                                '5 . 1 | . . 2 | . . .'                                                             
                                ])
    def test_InvalidSudoku_Unsolvable_Row(self):
        self._test_InvalidSudoku([
                                '9 . . | 1 . . | . . 4',
                                '. 1 4 | . 3 . | 8 . .',
                                '. . 3 | . . . | . 9 .',
                                '------+-------+------',
                                '. . . | 7 . 8 | . . 1',
                                '8 . . | . . 3 | . . .',
                                '. . . | . . . | . 3 .',
                                '------+-------+------',
                                '. 2 1 | . . . | . 7 .',
                                '. . 9 | . 4 . | 5 . .',
                                '5 . . | . 1 6 | . . 3'
                                ])


