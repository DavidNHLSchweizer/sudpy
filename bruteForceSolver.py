import SudokuConstants as SCS
from Validators import FieldsValidator, BoardValidator
from Board import Board
from BoardImporter import BoardImporterFromArray, BoardImporterFromFile
from BoardExporter import BoardExporterToString
import logging
from stopwatch import Stopwatch
from enum import Enum

class Reporter:
    class ReportType(Enum):
        START       = 0   
        STARTSOLVE  = 1
        STUCK       = 2
        NEWVALUE    = 3
        BACKTRACK   = 4
        ENDFALSE    = 41
        ENDTRUE     = 42

    def Report(self, rType: ReportType, data = None):
        pass

class SimpleReporter(Reporter):
    def __init__(self, logfilename):
        logging.basicConfig(filename=logfilename, filemode = 'w',level =logging.DEBUG, 
            format='%(message)s')
        self.Modulo = 1024

    def Report(self, rType: Reporter.ReportType, data = None):
        if rType == Reporter.ReportType.START:
            start = '\nsolving:\n' + data['board']
            print(start)
            logging.info(start)
        elif rType == Reporter.ReportType.STARTSOLVE:
            if data['nPass'] % self.Modulo == 0:
                print('.', end = '', flush=True)
            logging.info('call to Solve [{}, {}] (filled: {})'.format(data['nPass'], data['depth'], data['filled']))
        elif rType == Reporter.ReportType.STUCK:
            logging.info('stuck...')
        elif rType == Reporter.ReportType.NEWVALUE:
            logging.info('field: ({},{}) possible values: {} try {}'.format(data['row'], data['col'], data['values'], data['value']))
        elif rType == Reporter.ReportType.BACKTRACK:
            logging.info('backtrack [{}]'.format(data['depth'])) 
        elif rType == Reporter.ReportType.ENDFALSE:
            logging.info('end (false)')
            bah = '\nNO SOLUTION FOUND! ({})\n'.format(data['time'])
            logging.info(bah)
            print(bah)
        elif rType == Reporter.ReportType.ENDTRUE:
            hoera = '\nsolved! ({})\n\n{}'.format(data['time'], data['board'])
            logging.info(hoera)
            print(hoera)
        else:
            pass

class BruteForceSolver:
    def __init__(self):
        self._fieldsValidator = FieldsValidator()
        self.stopwatch = Stopwatch()
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
        reporter.Report(Reporter.ReportType.STARTSOLVE, {'nPass':self.nPass, 'depth':depth, 'filled':self.validator.nrFieldsWithValues(board)})
        if self.validator.IsCompleteValues(board) and self.validator.IsValidValues(board):
            return True
        field = self.findBestFieldToTryNext(board)
        if field == None:
            reporter.Report(Reporter.ReportType.STUCK)
            return False
        values = field.GetAllowedValues()
        for v in values:            
            reporter.Report(Reporter.ReportType.NEWVALUE, {'row':board.fieldRow(field), 'col':board.fieldCol(field),
                                         'values':field.GetAllowedValues(), 'value':v})
            field.value = v
            if self.Solve(board, depth+1, reporter):
                return True
            else:
                reporter.Report(Reporter.ReportType.BACKTRACK, {'depth':depth})
                field.value = SCS.INITIAL
        return False

    def SolveWithTiming(self, board, reporter = Reporter()):
        self.stopwatch.reset()
        self.stopwatch.start()
        reporter.Report(Reporter.ReportType.START, {'board': BoardExporterToString().BoardAsString(board)})
        result = self.Solve(board, 0, reporter)
        self.stopwatch.stop()  
        if result:
            reporter.Report(Reporter.ReportType.ENDTRUE, {'time':self.SolveTime(), 'board': BoardExporterToString().BoardAsString(board)})
        else:
            reporter.Report(Reporter.ReportType.ENDFALSE, {'time':self.SolveTime()})        
        return result      
    
    def SolveTime(self):
        return str(self.stopwatch)
    
def SolveFile(filename, logfilename):
    BruteForceSolver().SolveWithTiming(BoardImporterFromFile(filename).board, SimpleReporter(logfilename))

