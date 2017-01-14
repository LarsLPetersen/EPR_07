import unittest
from sort import *
import numpy
import pprint

class TestSortAlgorithms(unittest.TestCase):
    # self.array
    # self.sorted_array
    
    # cls_num = None
    # cls_array = numpy.random.choice(range(-20, 21), 10, replace = True)

    # @classmethod
    # def setUpClass(cls):
    #     cls_num = numpy.random.choice(range(1, 20), 1)
    #     cls_array = numpy.random.choice(range(-20, 21), cls_num)
    #     cls_sorted_array = numpy.sort(cls_array)

    def setUp(self):
        self.num = numpy.random.choice(range(1, 20), 1)
        self.array = numpy.random.choice(range(-50, 51), self.num)
        self.sorted_array = numpy.sort(self.array)
        

    def test_bubble_sort(self):
        array = numpy.copy(self.array)
        sorted_array = bubble_sort(array)
        self.assertEqual(list(sorted_array), list(self.sorted_array))
        print("\nEingabe: {}".format(self.array))
        print("Ausgabe: {}".format(sorted_array))


    def test_insertion_sort(self):
        array = numpy.copy(self.array)
        sorted_array = insertion_sort(array)
        self.assertEqual(list(sorted_array), list(self.sorted_array))
        print("\nEingabe: {}".format(self.array))
        print("Ausgabe: {}".format(sorted_array))


    def test_quick_sort(self):
        array = numpy.copy(self.array)
        sorted_array = insertion_sort(array)
        self.assertEqual(list(sorted_array), list(self.sorted_array))
        print("\nEingabe: {}".format(self.array))
        print("Ausgabe: {}".format(sorted_array))


if __name__ == '__main__':
    unittest.main(verbosity = 2)