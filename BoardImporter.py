import SudokuConstants as SCS
import re
from Board import Board
from BoardExporter import BoardExporter

class BoardImporter:
    def __init__(self):
        self.board = Board()
        self.patterns = []
        self.patterns.append(re.compile(r'\d\d\d.\d\d\d.\d\d\d'))
        
    def Import(self, lineSource):
        row = 0
        for line in lineSource:
            parsedLine = self.parseLine(line)
            if parsedLine:
                self._convertToRow(parsedLine, row)
                row += 1

    def parseLine(self, line):
        for pattern in self.patterns:
            match = pattern.match(line)
            if not match:
                pass
        results = []
        if match:
            for ch in line[match.start():match.end()]:
                if ch.isdigit():
                    results.append(int(ch))
        return results

    def _convertToRow(self, parsedLine, row):
        col = 0
        for value in parsedLine:
            if value > 0:
                field = self.board.field(row, col)
                field.value = value
                field.fixValue()
            col += 1

class BoardImporterFromFile(BoardImporter):
    def __init__(self, filename):
        super().__init__()
        with(open(filename, "r")) as fileHandler:
            self.Import(fileHandler)
                    
class BoardImporterFromArray(BoardImporter):
    def __init__(self, array):
        super().__init__()
        self.Import(array)


# filename = r'.\sudfiles\t9b.txt'
# I = BoardImporterFromFile(filename)

# B = BoardExporter()
# B.dumpFile(I.board, filename + '.exp')

# A = BoardImporterFromArray(["000 006 000",
#                             "059 000 008",
#                             "200 008 000",
#                             "045 000 000",
#                             "003 000 000",
#                             "006 003 054",
#                             "000 325 006",
#                             "000 000 000",
#                             "000 000 000"])
# B.dumpFile(A.board, r'.\sudfiles\arrayimport.exp')
# print(A.board.asString())
# print('---')

# A = BoardImporterFromArray(["178 236 495", 
#                             "359 174 268", 
#                             "264 598 713",
#                             "745 612 389", 
#                             "813 459 627", 
#                             "926 783 154", 
#                             "481 325 976", 
#                             "532 967 841", 
#                             "697 841 532"]) 
# print(A.board.asString())
# print('---')

# Board  = BoardImporterFromArray([
#                             "000 006 000",
#                             "059 080 000",
#                             "200 008 000",
#                             "045 000 000",
#                             "003 000 000",
#                             "006 003 054",
#                             "000 325 006",
#                             "000 000 000",
#                             "000 000 000"]).board
# # for r in range(SCS.BOARDSIZE):
# #     print(Board.Row(r).asString())
# print(Board.asString())
# print('---')
# for r in range(SCS.BLOCKSIZE):
#     for c in range(SCS.BLOCKSIZE):
#         print('block: [{}, {}]\n{}'.format(r,c, Board.Block(r,c).asString()))

