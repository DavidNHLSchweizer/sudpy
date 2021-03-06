INVALIDROWEXCEPTION = 'invalid row'
INVALIDCOLEXCEPTION = 'invalid col'
INVALIDROWSEXCEPTION = 'invalid nr of rows'
INVALIDCOLSEXCEPTION = 'invalid nr of cols'
INVALIDVALUEEXCEPTION = 'invalid value'
INVALIDSQUARESEXCEPTION = 'invalid dimension of squares group'
INVALIDSIZEEXCEPTION = 'invalid size'
INVALIDSQUARESEXCEPTION2 = 'adding invalid block'
INVALIDREFCOUNTEXCEPTION    = 'reference count'
PROGRAMMINGEXCEPTION    = 'invalid (series) of calls'
INITIAL   = 0
GRIDSIZE  = 9
BLOCKSIZE = 3
INDEXNOTFOUND = -1
MINIMUMFILLEDSQUARES = 17 # theoretical minimal needed filled squares to be solvable


def IsClear(value):
    return value == INITIAL

