import SudokuConstants as SCS
from Validators import FieldsValidator, BoardValidator
from Board import Board
from BoardImporter import BoardImporterFromArray, BoardImporterFromFile
from BoardExporter import BoardExporterToString
from Reporter import Reporter, SimpleReporter

class BruteForceSolver:
    def __init__(self):
        self._fieldsValidator = FieldsValidator()
        self.validator = BoardValidator()
        self.nPass = 0

    def findBestFieldToTryNext(self, board):
        # find the open field with the minimum values possible
        result = None
        curBest = SCS.BOARDSIZE + 1
        for r in range(SCS.BOARDSIZE):
            for c in range(SCS.BOARDSIZE):
                field = board.field(r,c)
                if not SCS.IsClear(field.value):
                    continue
                n = field.nrAllowedValues()
                if n == 0:
                    return None # no solution possible in this branch
                elif n == 1: 
                    return field # no reason to search any further
                elif n < curBest:
                    curBest = n
                    result = field
        return result

    def Solve(self, board, depth, reporter=Reporter())->bool:
        self.nPass += 1
        reporter.Report(Reporter.ReportType.STARTSOLVE, nPass=self.nPass, depth=depth, filled=self.validator.nrFieldsWithValues(board))
        if self.validator.IsCompleteValues(board) and self.validator.IsValidValues(board):
            return True
        field = self.findBestFieldToTryNext(board)
        if field == None:
            reporter.Report(Reporter.ReportType.STUCK)
            return False
        values = field.GetAllowedValues()
        for v in values:            
            reporter.Report(Reporter.ReportType.NEWVALUE, row=board.fieldRow(field), col=board.fieldCol(field), 
                                         values=field.GetAllowedValues(), value=v)
            field.value = v
            if self.Solve(board, depth+1, reporter):
                return True
            else:
                reporter.Report(Reporter.ReportType.BACKTRACK, depth=depth)
                field.value = SCS.INITIAL
        return False

    def SolveWithTiming(self, board, reporter = Reporter()):
        reporter.Start(board)
        result = self.Solve(board, 0, reporter)
        reporter.Stop(board, result)
        return result      
    
def SolveFile(filename, logfilename):
    BruteForceSolver().SolveWithTiming(BoardImporterFromFile(filename).board, SimpleReporter(logfilename))

