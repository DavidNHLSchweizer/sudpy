import pytest
import SudokuConstants
from AllowedValues import AllowedValues
from Value import Value

class TestAllowedValues:
    def _get_values(self, allowedValues=None, initialize=True):
        values = []
        for i in range(SudokuConstants.BOARDSIZE):
            if initialize:
                v = Value(i+1)
            else:
                v = Value()
            values.append(v)
            if allowedValues:
                allowedValues.ObserveValue(v)
        return values

    def _testAllowed(self, allowedValues, value, ExpectAllowed):
            assert allowedValues.IsAllowedValue(value) == ExpectAllowed
            assert bool(not value in allowedValues.GetAllowedValues()) ^ bool(ExpectAllowed)

    def test_allowedValues_initial(self):
        AV = AllowedValues()
        for i in range(1,SudokuConstants.BOARDSIZE+1):
            self._testAllowed(AV, i, True)
        assert AV.nrAllowedValues() == SudokuConstants.BOARDSIZE

    def test_allowedValues_observe(self):
        AV = AllowedValues()
        values = self._get_values()
        n = AV.nrAllowedValues()
        assert n == SudokuConstants.BOARDSIZE
        for v in values:                        
            self._testAllowed(AV, v.value, True)
            AV.ObserveValue(v)
            self._testAllowed(AV, v.value, False)
            assert AV.nrAllowedValues() == n-1
            n -= 1

    def test_allowedValues_clear(self):
        AV = AllowedValues()
        values = self._get_values(AV)
        for v in values:
            testvalue = v.value
            self._testAllowed(AV, testvalue, False)
            v.clear()
            self._testAllowed(AV, testvalue, True)

    def _test_swap_and_back(self, AV, values, i1, i2):
        v1 = values[i1].value
        v2 = values[i2].value
        self._testAllowed(AV, v1, False)
        self._testAllowed(AV, v2, False)
        values[i1].clear()
        self._testAllowed(AV, v1, True)
        values[i2].value = v1
        self._testAllowed(AV, v1, False)
        self._testAllowed(AV, v2, True)
        values[i1].value = v1
        values[i2].value = v2

    def test_allowedValues_move(self):
        AV = AllowedValues()
        values = self._get_values(AV)
        for i in range(len(values)):
            if i < len(values) - 1:
                self._test_swap_and_back(AV, values, i, i+1)
            else:
                self._test_swap_and_back(AV, values, i, 0)

    def test_allowedValues_toggle(self):
        AV = AllowedValues()
        values = self._get_values(AV)
        for v in values:
            testvalue = v.value
            v.clear()
            self._testAllowed(AV, testvalue, True)
            v.value = testvalue
            self._testAllowed(AV, testvalue, False)

    def test_multiple_values(self):
        AV = AllowedValues()
        values = self._get_values(AV, False)
        testvalue = 3
        self._testAllowed(AV, testvalue, True)
        values[0].value = testvalue
        values[1].value = testvalue
        values[2].value = testvalue
        self._testAllowed(AV, testvalue, False)
        values[0].clear()
        self._testAllowed(AV, testvalue, False)
        values[2].clear()
        self._testAllowed(AV, testvalue, False)
        values[1].clear()
        self._testAllowed(AV, testvalue, True)

    def test_multiple_values2(self):
        AV = AllowedValues()
        values = self._get_values(AV, False)
        testvalue = 2
        values[1].value = testvalue
        self._testAllowed(AV, testvalue, False)
        self._testAllowed(AV, testvalue+1, True)
        values[1].value = testvalue+1
        self._testAllowed(AV, testvalue, True)
        self._testAllowed(AV, testvalue+1, False)

    def test_sort_order_GetAllowedValues(self):
        AV = AllowedValues()
        self._get_values(AV, False)
        av = AV.GetAllowedValues()
        assert len(av) == SudokuConstants.BOARDSIZE
        prev = av[0]
        for i in range(1, len(av)):
            assert av[i] > prev
            prev = av[i]

    def test_sort_order_GetAllowedValues2(self):
        AV = AllowedValues()
        values = self._get_values(AV, True)
        values[0].clear()
        values[3].clear()
        values[6].clear()
        values[8].clear()
        av = AV.GetAllowedValues()
        assert len(av) == 4
        prev = av[0]
        for i in range(1, len(av)):
            assert av[i] > prev
            prev = av[i]
