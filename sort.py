
"""Contains the sorting algorithms Bubble Sort, Insertion Sort and Quick Sort"""

__author__ = "5625448: Lilian Mendoza de Sudan, 6290157: Lars Petersen"
__copyright__ = "Goethe Universitaet 2016"
__credits__ = "" 
__email__ = "lilian_mendoza@hotmail.com, petersen@informatik.uni-frankfurt.de"


# built-in modules
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle, randint
import time
import sys
import os


# constants
INFO_CHOICE = "\nBitte wählen Sie:\n" + \
              "0 -> Computer wählt zufällig die zu sortierende Liste\n" + \
              "1 -> individuelle Eingabe der zu sortierenden Liste\n"

INFO_LIST = "\nBitte geben Sie eine durch genau ein Leerzeichen separierte Folge von \n" + \
            "Zahlen an, die sortiert werden sollen.\n\n" + \
            "Bsp.: -17.3 0.4 99 18 -40003 1.1144 +19.3\n"

INFO_ALGORITHMS = "\nBitte geben Sie eine durch genau ein Leerzeichen separierte Folge von\n" + \
                  "den angegebenen Indizes an, welche(n) Algorithen(mus) Sie verwenden wollen.\n\n" + \
                  "0 -> Bubblesort\n" + \
                  "1 -> Insertionsort\n" + \
                  "2 -> Quicksort\n" + \
                  "3 -> Visualisierung von Bubblesort für zehn zufällige Zahlen\n\n" + \
                  "Bsp.: 0 2 3\n"


# (semi) constants
CLEAR = "cls" if os.name =="nt" else "clear"



def info_on_recursive_function_call(function, arguments):
    """Presents infos for output on calls of quick_sort."""
    print("\n{0:-^79}".format(" " + function.__name__.upper() + " "))
    print("Eingabe:")
    print("{}\n".format(*arguments))
    begin = time.time()
    result = function(*arguments)
    end = time.time()
    delta = end - begin
    print("Ausgabe:")
    print("{}\n".format(result))
    print("Laufzeit: {0:.5f} Sekunden\n".format(delta))
    print("Ausgabe von np.sort:")
    result_np = np.sort(arguments[0])
    print("{}\n".format(result))
    print("Abgleich in Ordnung? {}\n".format(np.array_equal(result, result_np)))

def info_on_function_call(function):
    """Works as a decorator for bubble_sort and insertion_sort."""
    
    def wrapper(*args, **kwargs):
        """Presents infos for output on calls of bubble_sort and insertion_sort."""
        print("\n{0:-^79}".format(" " + function.__name__.upper() + " "))
        print("Eingabe:")
        print("{}\n".format(*args))
        begin = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        delta = end - begin
        print("Ausgabe:")
        print("{}\n".format(result))
        print("Laufzeit: {0:.5f} Sekunden\n".format(delta))
        print("Ausgabe von np.sort:")
        result_np = np.sort(*args)
        print("{}\n".format(result))
        print("Abgleich in Ordnung? {}\n".format(np.array_equal(result, result_np)))
    return wrapper


@info_on_function_call
def bubble_sort(array):
    """Implements the bubblesort algorithm."""
    
    # trivial case
    if len(array) <= 1:
        return array

    array = np.copy(array)
    num = len(array) - 1
    
    for k in range(num):
        for i in range(num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


def bubble_sort_with_display(array):
    """Implements the bubblesort algorithm and displays sorting steps."""
    
    # initial state
    display(array)

    # trivial case
    if len(array) <= 1:
        return array

    array = np.copy(array)
    num = len(array) - 1
    for k in range(num):
        for i in range(num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            display(array)
    return array


@info_on_function_call
def insertion_sort(array):
    """Implements the insertionsort algorithm."""
    
    # trivial case
    if len(array) <= 1:
        return array

    num = len(array)
    
    for k in range(1, num):
        value = array[k]
        i = k
        while i > 0 and array[i - 1] > value:
            array[i] = array[i - 1]
            i -= 1
        array[i] = value
    return array


def quick_sort(array, left_index, right_index):
    """Implements the quicksort algorithm."""
    
    # trivial case
    if len(array) < 2 or right_index - left_index < 1:
        return array
    
    # use divide to determine a pivot element and pre-sort the array
    # with respect to the chosen pivot element
    [array, partition_index] = divide(array, left_index, right_index)
    
    # recursively call quick_sort on the left hand side of the pivot element
    if partition_index > left_index:
        array = quick_sort(array, left_index, partition_index - 1)
    
    # recursively call quick_sort on the right hand side of the pivot element
    if partition_index < right_index:
        array = quick_sort(array, partition_index + 1, right_index)
    
    return array


def divide(array, left_index, right_index):
    """Chooses a pivot element and pre_sorts the array wrt the pivot element.

       Elements to the left of the pivot element will be less or equal to the latter.
       Elements to right of it will be equal or bigger.
    """

    # choose the pivot element from the "middle" of the array
    pivot_index = int(left_index + (right_index - left_index)/2)
    pivot_value = array[pivot_index]

    # initialize the running indices 
    left, right = left_index, right_index
    
    while left < right:
        #
        if left == pivot_index:
            swap_index = right
            #
            for k  in range(right, pivot_index, - 1):
                if array[k] >= pivot_value:
                    array[k], array[swap_index] = array[swap_index], array[k]
                    swap_index -= 1
            array[pivot_index], array[swap_index] = array[swap_index], array[pivot_index]
            right = pivot_index
            pivot_index = swap_index
        #
        elif right == pivot_index:
            swap_index = left
            #
            for k  in range(left, pivot_index):
                if array[k] <= pivot_value:
                    array[k], array[swap_index] = array[swap_index], array[k]
                    swap_index += 1
            array[pivot_index], array[swap_index] = array[swap_index], array[pivot_index]
            left = pivot_index
            pivot_index = swap_index
        #
        else:
            #
            for i  in range(left, pivot_index + 1):
                if array[i] > pivot_value:
                    break
            left = i
            #
            for k  in range(right, pivot_index - 1, - 1):
                if array[k] < pivot_value:
                    break
            right = k
            #
            if left != pivot_index and right != pivot_index:
                array[left], array[right] = array[right], array[left]
            
    return [array, pivot_index]
            

def generate_random_numbers(num):
    """Generates an array of num random numbers."""
    
    # set seed so we all get the same "random" numbers
    np.random.seed(0)
    return np.random.choice(range(1, 20), num, replace=True)


def display(numbers, title = "Illustration of the Sorting Steps"):
    """Displays numbers as vertical boxes of height equal to number."""
    fig = plt.figure(0)
    plt.ion()
    plt.clf()
    plt.bar(range(len(numbers)), numbers)
    plt.title(title)
    plt.pause(0.001)


def get_input():
    """Lets the user choose between random and custom mode"""
    
    is_correct_input = False
    
    while not is_correct_input:   
        os.system(CLEAR)
        print(INFO_LIST)
        
        try:
            user_input = input("Ihre Wahl:\n>> ")
            parsed_input = []
        
            for literal in user_input.split(" "):
                parsed_input.append(float(literal))
            return np.array(parsed_input)
        
        except ValueError:
            print("\nValueError!")
            print("Bitte geben Sie Zahlen ein ...\n")
            print("Neuer Versuch ...\n")
            input()
            continue
        
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt!")
            print("Abbruch...\n")
            sys.exit()


def choose_mode():
    """ """
    is_correct_input = False
    
    while not is_correct_input:
        os.system(CLEAR)
        print(INFO_CHOICE)
        
        try:
            user_input = input("Ihre Wahl:\n>> ")

            if user_input == "0":
                return 0
            elif user_input == "1":
                return 1
            else:
                print("\nEingabe nicht gemäß Vorgabe!")
                print("Neuer Versuch ...\n")
                input()
                continue
                
        except KeyboardInterrupt:
                print("\nKeyboardInterrupt!")
                print("Abbruch...\n")
                sys.exit()


ALGORITHMS = {0:bubble_sort, 1:insertion_sort, 2:quick_sort, 3:bubble_sort_with_display}


def choose_algorithms():
    """ """
    is_correct_input = False
    
    while not is_correct_input:
        
        os.system(CLEAR)
        print(INFO_ALGORITHMS)
        
        try:
            user_input = input("Ihre Wahl:\n>> ")
            parsed_input = set(user_input.split(" "))

            if parsed_input.issubset(set([i for i in "0123"])) == True:
                return sorted([int(index) for index in list(parsed_input)])
            else:
                print("\nEingaben nicht gemäß Vorgabe!")
                print("Neuer Versuch ...\n")
                input()
                continue
                
        except KeyboardInterrupt:
                print("\nKeyboardInterrupt!")
                print("Abbruch...\n")
                sys.exit()


def main():
    """Controls the main flow of interaction with the user."""
    
    # user is asked to choose the mode 
    choice_mode = choose_mode()
    # random input mode
    if choice_mode == 0:
        array = generate_random_numbers(200)
    # user input mode
    else:
        array = get_input()
    # user is asked to choose the set of algorithms to be applied
    choice_algorithms = choose_algorithms()
    # dictionary providing the arguments for the respective algorithms (see ALGORITHMS)
    arguments = {0:[array.copy()], 1:[array.copy()],
                 2:[array.copy(), 0, len(array.copy()) - 1], 3:[generate_random_numbers(10)]}
    
    for index in choice_algorithms:
        # special case for quicksort, since decorator doesn't work as desired with recursive
        # function calls
        if index == 2:
            info_on_recursive_function_call(ALGORITHMS[index], arguments[index])
        else:
            ALGORITHMS[index](*arguments[index])
    

if __name__ == "__main__":
    main()