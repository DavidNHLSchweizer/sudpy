import SudokuConstants as SCS
import re
from Grid import Grid

class GridImporter:
    def __init__(self):
        self.grid = Grid()
        self.patterns = []
        self.patterns.append(re.compile(r'\d\d\d.\d\d\d.\d\d\d'))
        self.patterns.append(re.compile(r'[\.,\d]'))
        
    def Import(self, lineSource):
        row = 0
        for line in lineSource:
            parsedLine = self.parseLine(line)
            if parsedLine:
                self._convertToRow(parsedLine, row)
                row += 1

    def parseLine(self, line):
        for pattern in self.patterns:
            results = []
            for match in pattern.finditer(line):
                for ch in line[match.start():match.end()]:
                    if ch.isdigit():
                        results.append(int(ch))
                    elif ch == '.':
                        results.append(int(0))
            if len(results) == SCS.GRIDSIZE:
                return results
        return None

    def _convertToRow(self, parsedLine, row):
        col = 0
        for value in parsedLine:
            if value > 0:
                field = self.grid.square(row, col)
                field.value = value
                field.fixValue()
            col += 1

class GridImporterFromFile(GridImporter):
    def __init__(self, filename):
        super().__init__()
        with(open(filename, "r")) as fileHandler:
            self.Import(fileHandler)
                    
class GridImporterFromArray(GridImporter):
    def __init__(self, array):
        super().__init__()
        self.Import(array)


# filename = r'.\sudfiles\t9b.txt'
# I = GridImporterFromFile(filename)

# B = GridExporter()
# B.dumpFile(I.grid, filename + '.exp')

# A = GridImporterFromArray(["000 006 000",
#                             "059 000 008",
#                             "200 008 000",
#                             "045 000 000",
#                             "003 000 000",
#                             "006 003 054",
#                             "000 325 006",
#                             "000 000 000",
#                             "000 000 000"])
# B.dumpFile(A.grid, r'.\sudfiles\arrayimport.exp')
# print(A.grid.asString())
# print('---')

# A = GridImporterFromArray(["178 236 495", 
#                             "359 174 268", 
#                             "264 598 713",
#                             "745 612 389", 
#                             "813 459 627", 
#                             "926 783 154", 
#                             "481 325 976", 
#                             "532 967 841", 
#                             "697 841 532"]) 
# print(A.grid.asString())
# print('---')

# Grid  = GridImporterFromArray([
#                             "000 006 000",
#                             "059 080 000",
#                             "200 008 000",
#                             "045 000 000",
#                             "003 000 000",
#                             "006 003 054",
#                             "000 325 006",
#                             "000 000 000",
#                             "000 000 000"]).grid
# # for r in range(SCS.GRIDSIZE):
# #     print(Grid.Row(r).asString())
# print(Grid.asString())
# print('---')
# for r in range(SCS.BLOCKSIZE):
#     for c in range(SCS.BLOCKSIZE):
#         print('block: [{}, {}]\n{}'.format(r,c, Grid.Block(r,c).asString()))


# pattern = re.compile(r'[\.,\d]')
# for match in pattern.finditer('. . 9 | . 7 . | . . 5'):
#     print(match)

# G = GridImporterFromArray([
#         '. . 9 | . 7 . | . . 5',
#         '. . 2 | 1 . . | 9 . .',
#         '1 . . | . 2 8 | . . .',
#         '------+-------+------',
#         '. 7 . | . . 5 | . . 1',
#         '. . 8 | 5 1 . | . . .',
#         '. 5 . | . . . | 3 . .',
#         '------+-------+------',
#         '. . . | . . 3 | . . 6',
#         '8 . . | . . . | . . .',
#         '2 1 . | . . . | . 8 7'
#     ])
# print(G.grid.asString())
# print('--------')
# grid = GridImporterFromArray([
#                     "000 006 000",
#                     "059 080 000",
#                     "200 008 000",
#                     "045 000 000",
#                     "003 000 000",
#                     "006 003 054",
#                     "000 325 006",
#                     "000 000 000",
#                     "000 000 000"]).grid
# print(grid.asString())

# print( G.parseLine('. . 9 | . 7 . | . . 5'))

# print(parseLine(r'\d\d\d.\d\d\d.\d\d\d', '000 006 000'))
# print(parseLine(r'[\.,\d]', '. . 9 | . 7 . | . . 5'))
# print(parseLine(r'[\.,\d]', '------+-------+------'))

