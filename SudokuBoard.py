import SudokuConstants
from observerPattern import SimpleSubject, Observer
from typing import List

def IsClear(value):
    return value == SudokuConstants.INITIAL

class Field(SimpleSubject):
    def _checkLegalValue(self, value):
        if not (IsClear(value) or (value >= 1 and value <= SudokuConstants.BOARDSIZE)):
            raise ValueError(SudokuConstants.INVALIDVALUEEXCEPTION + ' {}'.format(value))        
 
    def __init__(self, value=SudokuConstants.INITIAL):
        super().__init__()
        self._checkLegalValue(value)
        self._value = value
        self._oldvalue = SudokuConstants.INITIAL
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, newvalue):
        if (self.value == newvalue):
            return
        self._checkLegalValue(newvalue)
        self._oldvalue = self._value
        self._value = newvalue
        self.notify()
    @property
    def oldvalue(self):
        return self._oldvalue
    def clear(self):
        self.value = SudokuConstants.INITIAL

class AllowedValues(Observer):
    def __init__(self):
        self._allowedValues: List(int) = []
        self._fieldCount = [0]
        for i in range(1, SudokuConstants.BOARDSIZE+1):
            self._allowedValues.append(i)
            self._fieldCount.append(0)
    def _addAllowedValue(self, value):
        if not IsClear(value):
            self._fieldCount[value] -= 1
            if self._fieldCount[value] < 0:
                raise ValueError(SudokuConstants.INVALIDREFCOUNTEXCEPTION + ' {} (value {})'.format(self._fieldCount[value], value))
            if self._fieldCount[value] == 0 and not value in self._allowedValues:
                self._allowedValues.append(value)
    def _removeAllowedValue(self, value):
        self._fieldCount[value] += 1
        if value in self._allowedValues:
            self._allowedValues.remove(value)
    def addField(self, field):
        field.attach(self)
        self._removeAllowedValue(field.value)
    def update(self, field):
        self._addAllowedValue(field.oldvalue)
        self._removeAllowedValue(field.value)
    def IsAllowedValue(self, value):
        return value in self._allowedValues
    def GetAllowedValues(self):
        return sorted(self._allowedValues)

class FieldGroup:
    def __init__(self):
        self.fields:List[Field] = []
        self._allowedValues = AllowedValues()
    def clear(self):
        for field in self.fields:
            field.clear()
    def addField(self, field):
        if not field in self.fields:
            self.fields.append(field)
            self._allowedValues.addField(field)
    def addFields(self, fields):
        for field in fields:
            self.addField(field)
    def IsAllowedValue(self, value):
        return self._allowedValues.IsAllowedValue(value)
    def GetAllowedValues(self):
        return self._allowedValues.GetAllowedValues()

f = Field()
A = AllowedValues()
A.addField(f)
print (A._allowedValues)
print (A._fieldCount[1:])
f.value = 3
print (A._allowedValues)
print (A._fieldCount[1:])
f.value = 0
print (A.GetAllowedValues())
print (A._fieldCount[1:])

