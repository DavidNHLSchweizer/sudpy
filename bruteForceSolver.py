import SudokuConstants as SCS
from Solver import SolveStrategy, Solver
from Validators import GridValidator
from Grid import Grid
from Square import Square
from GridImporter import GridImporterFromArray, GridImporterFromFile
from GridExporter import GridExporterToString
from Reporter import Reporter, SimpleReporter

class BruteForceSolver(SolveStrategy):
    def __init__(self, reporter = Reporter()):
        super().__init__()
        self.nPass = 0
        self.depth = 0
        self.validator = GridValidator()
        self.reporter = reporter

    def findBestSquareToTryNext(self, grid)->Square:
        # find the open square with the least values possible
        def _NoSolutionPossibleInThisBranch(n):
            return n == 0
        def _SquareHasOneAllowedValue(n):
            return n == 1
        result = None
        LeastNrAllowedValues = SCS.GRIDSIZE + 1
        for square in grid.squares:
            if not SCS.IsClear(square.value):
                continue
            n = square.nrAllowedValues()
            if _NoSolutionPossibleInThisBranch(n):
                return None 
            elif _SquareHasOneAllowedValue(n): 
                return square 
            elif n < LeastNrAllowedValues:
                LeastNrAllowedValues = n
                result = square
        return result

    def Solve(self, grid)->bool:
        self.reporter.Start(grid)
        result = self._RecursiveSolve(grid, 0)
        self.reporter.Stop(grid, result, self.SolveTime())
        return result

    def _RecursiveSolve(self, grid, depth)->bool:
        self.nPass += 1
        self.reporter.Report(Reporter.ReportType.STARTSOLVE, nPass=self.nPass, depth=depth, filled=grid.nrSquaresWithValues())
        if not self.validator.IsValidValues(grid):
            return False
        if self.validator.IsCompleteValues(grid):
            return True
        square = self.findBestSquareToTryNext(grid)
        if square == None:
            self.reporter.Report(Reporter.ReportType.STUCK)
            return False
        row, col = grid.sqRow(square), grid.sqCol(square)
        values = square.GetAllowedValues()
        for v in values:            
            self.reporter.Report(Reporter.ReportType.NEWVALUE, row=row, col=col, values=values, value=v)
            square.value = v
            if self._RecursiveSolve(grid, depth+1):
                return True
            else:
                self.reporter.Report(Reporter.ReportType.BACKTRACK, depth=depth)
                square.value = SCS.INITIAL
        return False

def SolveFile(filename, logfilename):
    Solver().Solve(GridImporterFromFile(filename).grid, BruteForceSolver(SimpleReporter(logfilename)))

