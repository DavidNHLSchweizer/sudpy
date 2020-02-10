import SudokuConstants
import re
from Board import Board


def parseLine(line):
    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')
    match = pattern.match(line)
    if not match:
        return
    results = []
    for ch in line[match.start():match.end()]:
        if ch.isdigit():
            results.append(int(ch))
    return results

class BoardImporter:
    def _convertToRow(self, parsedLine, row):
        col = 0
        for value in parsedLine:
            if value > 0:
                field = self.board.field(row, col)
                field.value = value
                field.fixValue()
            col += 1

    def __init__(self, filename):
        self.board = Board()
        with(open(filename, "r")) as fileHandler:
            row = 0
            for line in fileHandler:
                parsedLine = parseLine(line)
                if parsedLine:
                    self._convertToRow(parsedLine, row)
                    row += 1
                    
class BoardDumper:
    def _getLineFromBoard(self, board, row):
        line = ''
        for col in range(SudokuConstants.BOARDSIZE):
            field = board.field(row,col)
            line = line + ('0' if field.value == SudokuConstants.INITIAL else str(field.value))
            if col % 3 == 2:
                line = line + ' '
        return line
        
    def dumpFile(self, board, filename):
        with(open(filename, "w")) as fileHandler:
            for row in range(SudokuConstants.BOARDSIZE):            
                line = self._getLineFromBoard(board, row)
                if line:
                    fileHandler.write(line+'\n')

filename = r'.\sudfiles\t9b.txt'
I = BoardImporter(filename)

B = BoardDumper()
B.dumpFile(I.board, filename + '.exp')