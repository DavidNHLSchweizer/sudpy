import logging
from stopwatch import Stopwatch
from BoardExporter import BoardExporterToString
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

    def Start(self, board):
        pass
    def Report(self, rType: ReportType, **kwargs):
        pass
    def Stop(self, board, success):
        pass

class SimpleReporter(Reporter):
    def __init__(self, logfilename):
        logging.basicConfig(filename=logfilename, filemode = 'w',level =logging.DEBUG, 
            format='%(message)s')
        self.Modulo = 1024
        self.stopwatch = Stopwatch()
        
    def Report(self, rType: Reporter.ReportType, **kwargs):
        if rType == Reporter.ReportType.START:
            start = '\nsolving:\n' + kwargs['board']
            print(start)
            logging.info(start)
        elif rType == Reporter.ReportType.STARTSOLVE:
            if kwargs['nPass'] % self.Modulo == 0:
                print('.', end = '', flush=True)
            logging.info('call to Solve [{}, {}] (filled: {})'.format(kwargs['nPass'], kwargs['depth'], kwargs['filled']))
        elif rType == Reporter.ReportType.STUCK:
            logging.info('stuck...')
        elif rType == Reporter.ReportType.NEWVALUE:
            logging.info('field: ({},{}) possible values: {} try {}'.format(kwargs['row'], kwargs['col'], kwargs['values'], kwargs['value']))
        elif rType == Reporter.ReportType.BACKTRACK:
            logging.info('backtrack [{}]'.format(kwargs['depth'])) 
        elif rType == Reporter.ReportType.ENDFALSE:
            logging.info('end (false)')
            bah = '\nNO SOLUTION FOUND! ({})\n'.format(kwargs['time'])
            logging.info(bah)
            print(bah)
        elif rType == Reporter.ReportType.ENDTRUE:
            hoera = '\nsolved! ({})\n\n{}'.format(kwargs['time'], kwargs['board'])
            logging.info(hoera)
            print(hoera)
        else:
            pass
    def SolveTime(self):
        return str(self.stopwatch)
    def Start(self, board):
        self.stopwatch.reset()
        self.stopwatch.start()
        self.Report(Reporter.ReportType.START, board=BoardExporterToString().BoardAsString(board))
    def Stop(self, board, success):
        self.stopwatch.stop()  
        if success:
            self.Report(Reporter.ReportType.ENDTRUE, time=self.SolveTime(), board=BoardExporterToString().BoardAsString(board))
        else:
            self.Report(Reporter.ReportType.ENDFALSE, time=self.SolveTime())        

