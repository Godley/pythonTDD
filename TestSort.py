import unittest
from sort_methods import *

class TestSort(unittest.TestCase):
    def setUp(self):
        self.valid_data = [1,5,20,30,5,0,7,6]
        self.one_input = [3]
        self.empty_data = []
        self.sorts = [insertionSort,selectionSort,MergeSort, QuickSort, BubbleSort]

    def testEmpty(self):
        for method in self.sorts:
            self.assertEquals(self.empty_data, method(self.empty_data), "Error: empty test failed on method: "+str(method))

    def testOneInput(self):
        for method in self.sorts:
            self.assertEqual(self.one_input, method(self.one_input), "Error: one input failed on method: "+str(method))

    def testNone(self):
        for method in self.sorts:
            self.assertRaises(BaseException, method, None, "Error: giving no data does not throw an exception in method: "+str(method))

    def testSorts(self):
        expected = [0,1,5,5,6,7,20,30]
        for method in self.sorts:
            self.assertEqual(expected, method(self.valid_data),"Error: sorting algorithm does not run as expected: "+str(method))



if __name__ == '__main__':
    unittest.main()