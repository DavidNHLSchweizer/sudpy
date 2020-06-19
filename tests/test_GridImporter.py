import pytest
import SudokuConstants as SCS
from Grid import Grid
from GridImporter import GridImporterFromArray

class Test_GridImporterFromArray:

    def test_complete_grid_nrValues(self):
        grid = GridImporterFromArray([
                            "178 236 495", 
                            "359 174 268", 
                            "264 598 713",
                            "745 612 389", 
                            "813 457 627", 
                            "926 783 154", 
                            "481 325 976", 
                            "532 967 841", 
                            "697 841 532"]).grid
        assert grid.nrSquaresWithValues() == SCS.GRIDSIZE * SCS.GRIDSIZE

    def test_incomplete_grid_nrValues(self):
        grid = GridImporterFromArray([
                            "178 236 495", 
                            "359 174 268", 
                            "264 598 713",
                            "745 612 389", 
                            "813 450 627", 
                            "926 783 154", 
                            "481 325 976", 
                            "532 967 841", 
                            "697 841 532"]).grid
        assert grid.nrSquaresWithValues() == SCS.GRIDSIZE * SCS.GRIDSIZE-1

    def test_incomplete_grid_nrValues2(self):
        grid = GridImporterFromArray([
                            "000 006 000",
                            "059 000 008",
                            "200 008 000",
                            "045 000 000",
                            "003 000 000",
                            "006 003 054",
                            "000 325 006",
                            "000 000 000",
                            "000 000 000"]).grid
        assert grid.nrSquaresWithValues() == 17

