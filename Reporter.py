import logging
from GridExporter import GridExporterToString
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
misschien hier iets generaliseren?

    def Start(self, grid):
        pass
    def Report(self, rType: ReportType, **kwargs):
        pass
    def Stop(self, grid, success, solveTime):
        pass

class SimpleReporter(Reporter):
    def __init__(self, logfilename):
        logging.basicConfig(filename=logfilename, filemode = 'w',level =logging.DEBUG, 
            format='%(message)s')
        self.Modulo = 1024
        
    def Report(self, rType: Reporter.ReportType, **kwargs):
        if rType == Reporter.ReportType.START:
            start = '\nsolving:\n' + kwargs['grid']
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
            hoera = '\nsolved! ({})\n\n{}'.format(kwargs['time'], kwargs['grid'])
            logging.info(hoera)
            print(hoera)
        else:
            pass
    def Start(self, grid):
        self.Report(Reporter.ReportType.START, grid=GridExporterToString().GridAsString(grid))
    def Stop(self, grid, success, solveTime):
        if success:
            self.Report(Reporter.ReportType.ENDTRUE, time=solveTime, grid=GridExporterToString().GridAsString(grid))
        else:
            self.Report(Reporter.ReportType.ENDFALSE, time=solveTime)        

