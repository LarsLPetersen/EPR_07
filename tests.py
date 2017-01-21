"""Contains test cases for the sorting algorithms implemented in sort.py."""

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


class RuntimeEvaluation:
    """Performs runtime evaluations on the given sorting algorithm."""
    def __init__(self, num, function):
        self.num = num
        self.function = function
        
    def stop_time(self):
        """Measures runtime of the given function for an array of size num."""
        array = generate_random_numbers(self.num)
        if self.function.__name__ == "quick_sort":
            arguments = [array, 0, len(array) - 1]
        else: arguments = [array]

        begin = time.time()
        self.function(*arguments)
        end = time.time()
        print("Laufzeit: {0:.5f} Sekunden\n".format(end - begin))

    
class TestSortAlgorithms(unittest.TestCase):
    """TestCase comprising individual methods for each sorting algorithm."""
    
    def setUp(self):
        """Initializes the array to be sorted."""
        # numpy.random.seed(0)
        self.num = numpy.random.choice(range(1, 51), 1)
        self.singleton = self.num
        self.sorted_singleton = numpy.sort(self.singleton)
        self.equalton = numpy.array([self.singleton[0] for i in range(5)])
        self.sorted_equalton = numpy.sort(self.equalton)
        self.array = numpy.random.choice(range(-50, 51), self.num)
        self.sorted_array = numpy.sort(self.array)
        
    
    def test_bubble_sort(self):
        """Tests the implementation of bubblesort against np.sort."""
        singleton = numpy.copy(self.singleton)
        sorted_singleton = bubble_sort(singleton)
        print("\nEingabe: {}".format(self.singleton))
        print("Ausgabe: {}".format(sorted_singleton))
        self.assertEqual(list(sorted_singleton), list(self.sorted_singleton))
        
        equalton = numpy.copy(self.equalton)
        sorted_equalton = bubble_sort(equalton)
        print("\nEingabe: {}".format(self.equalton))
        print("Ausgabe: {}".format(sorted_equalton))
        self.assertEqual(list(sorted_equalton), list(self.sorted_equalton))

        array = numpy.copy(self.array)
        sorted_array = bubble_sort(array)
        print("\nEingabe: {}".format(self.array))
        print("Ausgabe: {}".format(sorted_array))
        self.assertEqual(list(sorted_array), list(self.sorted_array))

    def test_insertion_sort(self):
        """Tests the implementation of insertionsort against np.sort."""      
        singleton = numpy.copy(self.singleton)
        sorted_singleton = bubble_sort(singleton)
        print("\nEingabe: {}".format(self.singleton))
        print("Ausgabe: {}".format(sorted_singleton))
        self.assertEqual(list(sorted_singleton), list(self.sorted_singleton))
        
        equalton = numpy.copy(self.equalton)
        sorted_equalton = bubble_sort(equalton)
        print("\nEingabe: {}".format(self.equalton))
        print("Ausgabe: {}".format(sorted_equalton))
        self.assertEqual(list(sorted_equalton), list(self.sorted_equalton))

        array = numpy.copy(self.array)
        sorted_array = insertion_sort(array)
        print("\nEingabe: {}".format(self.array))
        print("Ausgabe: {}".format(sorted_array))
        self.assertEqual(list(sorted_array), list(self.sorted_array))
        
    def test_quick_sort(self):
        """Tests the implementation of quicksort against np.sort."""
        singleton = numpy.copy(self.singleton)
        sorted_singleton = bubble_sort(singleton)
        print("\nEingabe: {}".format(self.singleton))
        print("Ausgabe: {}".format(sorted_singleton))
        self.assertEqual(list(sorted_singleton), list(self.sorted_singleton))
        
        equalton = numpy.copy(self.equalton)
        sorted_equalton = bubble_sort(equalton)
        print("\nEingabe: {}".format(self.equalton))
        print("Ausgabe: {}".format(sorted_equalton))
        self.assertEqual(list(sorted_equalton), list(self.sorted_equalton))
        
        array = numpy.copy(self.array)
        sorted_array = insertion_sort(array)
        print("\nEingabe: {}".format(self.array))
        print("Ausgabe: {}".format(sorted_array))
        self.assertEqual(list(sorted_array), list(self.sorted_array))
        

if __name__ == '__main__':
    unittest.main(verbosity = 2)
    # run_time_eval_bubblesort = RuntimeEvaluation(500, bubble_sort)
    # run_time_eval_bubblesort.stop_time()
    # run_time_eval_insertionsort = RuntimeEvaluation(500, insertion_sort)
    # run_time_eval_insertionsort.stop_time()
    # run_time_eval_quicksort = RuntimeEvaluation(500, quick_sort)
    # run_time_eval_quicksort.stop_time()
    