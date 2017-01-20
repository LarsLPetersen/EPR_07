"""Contains test cases for the sorting algorithms."""

__author__ = "5625448: Lilian Mendoza de Sudan, 6290157: Lars Petersen"
__copyright__ = "Goethe Universitaet 2016"
__credits__ = "" 
__email__ = "lilian_mendoza@hotmail.com, petersen@informatik.uni-frankfurt.de"


# built-in modules
import unittest
import numpy
import pprint
import logging

# customized modules
from sort import *


def logger(function):
    """"""
    logging.basicConfig(filename = "{}.log".format(function.__name__), level = logging.INFO)

    def wrapper(*args, **kwargs):
        """"""
        logging.info(function(*args, **kwargs))
        # return function(*args, **kwargs)
    return wrapper


class RuntimeEvaluation:
    """ """
    def __init__(self, num, function):
        self.num = num
        self.function = function
        
    def stop_time(self):
        array = generate_random_numbers(self.num)
        if self.function.__name__ == "quick_sort":
            arguments = [array, 0, len(array) - 1]
        else: arguments = [array]

        begin = time.time()
        self.function(*arguments)
        end = time.time()
        print("Laufzeit: {0:.5f} Sekunden\n".format(end - begin))

    
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
        self.num = numpy.random.choice(range(1, 51), 1)
        self.array = numpy.random.choice(range(-50, 51), self.num)
        self.sorted_array = numpy.sort(self.array)
        

    # @logger
    def test_bubble_sort(self):
        array = numpy.copy(self.array)
        sorted_array = bubble_sort(array)
        self.assertEqual(list(sorted_array), list(self.sorted_array))
        print("\nEingabe:\n{}".format(self.array))
        print("Ausgabe:\n{}".format(sorted_array))


    def test_insertion_sort(self):
        array = numpy.copy(self.array)
        sorted_array = insertion_sort(array)
        self.assertEqual(list(sorted_array), list(self.sorted_array))
        print("\nEingabe:\n{}".format(self.array))
        print("Ausgabe:\n{}".format(sorted_array))

    # @logger
    def test_quick_sort(self):
        array = numpy.copy(self.array)
        sorted_array = insertion_sort(array)
        self.assertEqual(list(sorted_array), list(self.sorted_array))
        print("\nEingabe:\n{}".format(self.array))
        print("Ausgabe:\n{}".format(sorted_array))

        

   
if __name__ == '__main__':
    unittest.main(verbosity = 2)
    # print("s:\n{}".format(s))
    # t = unittest.main(verbosity = 2)
    # print("t:\n{}".format(t))
    # unittest.main(verbosity = 2)
    # rtel1 = RuntimeEvaluation(500, bubble_sort)
    # rtel1.stop_time()
    # rtel1 = RuntimeEvaluation(500, insertion_sort)
    # rtel1.stop_time()
    # rtel1 = RuntimeEvaluation(500, quick_sort)
    # rtel1.stop_time()