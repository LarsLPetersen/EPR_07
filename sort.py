
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
#import random

# (semi) constants
CLEAR = "cls" if os.name =="nt" else "clear"



def bubble_sort(array):
    """ """
    # display(array)

    if len(array) <= 1:
        return array

    array = np.copy(array)
    num = len(array) - 1
    for k in range(num):
        for i in range(num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            # display(array)
    return array


def insertion_sort(array):
    """ """
    # display(array)

    if len(array) <= 1:
        return array

    num = len(array)
    
    for k in range(1, num):
        value = array[k]
        i = k
        while i > 0 and array[i - 1] > value:
            array[i] = array[i - 1]
            i -= 1
            # display(array)
        array[i] = value

    return array


def quick_sort(array, left_index, right_index):
    """ """
    
    # display(array)
    if len(array) < 2 or right_index - left_index < 1:
        return array
    
    [array, partition_index] = divide(array, left_index, right_index)
    # print("divide({}, {}, {})".format(array, left_index, right_index))
    # print("divide(...) = [{}, {}]".format(array, partition_index))
    
    # if partition_index
    if partition_index > left_index:
        array = quick_sort(array, left_index, partition_index - 1)
    # print("quick_sort({}, {}, {})".format(array, left_index, partition_index -1))
    # print("quick_sort(...) = {}".format(array))
    
    if partition_index < right_index:
        array = quick_sort(array, partition_index + 1, right_index)
    # print("quick_sort({}, {}, {})".format(array, partition_index + 1, right_index))
    # print("quick_sort(...) = {}".format(array))

    #display(array)
    return array

        # pivot_index = right_index
        # pivot = array[pivot_index]
        # left, right = left_index, right_index - 1
        # while left < right:
        #     while array[left] <= pivot:
        #         left += 1
        #     while array[right] >= pivot:
        #         right -= 1
        #     if left < right:
        #         array[left], array[right] = array[right], array[left]
        # if array[left] > pivot:
        #     array[left], array[pivot_index] = array[pivot_index], array[left] 
        
        # return array


def divide(array, left_index, right_index):
    """ """
    # display(array)
    pivot_index = int(left_index + (right_index - left_index)/2)
    # pivot_index = randint(left_index, right_index)
    # print("Pivot Index: {}".format(pivot_index))
    pivot_value = array[pivot_index]
    # print("Pivot Value: {}".format(pivot_value))
    left, right = left_index, right_index
    # print("Left: {}, Right: {}".format(left, right))
    while left < right:
        if left == pivot_index:
            # print("left == pivot_index")
            swap_index = right
            for k  in range(right, pivot_index, - 1):
                if array[k] >= pivot_value:
                    array[k], array[swap_index] = array[swap_index], array[k]
                    swap_index -= 1
            array[pivot_index], array[swap_index] = array[swap_index], array[pivot_index]
            # display(array)
            right = pivot_index
            pivot_index = swap_index
        

        elif right == pivot_index:
            # print("right == pivot_index")
            swap_index = left
            for k  in range(left, pivot_index):
                # display(array)
                if array[k] <= pivot_value:
                    array[k], array[swap_index] = array[swap_index], array[k]
                    swap_index += 1
            array[pivot_index], array[swap_index] = array[swap_index], array[pivot_index]
            # display(array)
            left = pivot_index
            pivot_index = swap_index
        
        else:
            # print("right != pivot_index und left != pivot_index")
            # left = pivot_index
            for i  in range(left, pivot_index + 1):
                if array[i] > pivot_value:
                    # left = i
                    break
            left = i
            # right = pivot_index
            for k  in range(right, pivot_index - 1, - 1):
                if array[k] < pivot_value:
                    # right = k
                    break
            right = k
            if left != pivot_index and right != pivot_index:
                array[left], array[right] = array[right], array[left]
                # display(array)
    
    return [array, pivot_index]
            
# def divide(array, left_index, right_index):
#     """ """
#     pivot_index = int((right_index - left_index)/2)
#     pivot_value = array[pivot_index]
    
#     swap_index = left_index
#     for i in range(left_index, pivot_index):
#         if array[i] <= pivot_value:
#             swap_index += 1
    
#     for i in range(left_index, right_index + 1):
#         if array[i] <= pivot_value:
#                 swap_index += 1
#     left, right = left_index, right_index
    
#     while left < right:
#         for i  in range(left_index, pivot_index + 1):
#             if array[i] > pivot_value:
#                 break
#         left = i
#         #while array[left] <= pivot_value:
#         #    left = min(left + 1, right_index)
#         for k  in range(right_index, pivot_index - 1, - 1):
#             if array[k] < pivot_value:
#                 break
#         right = k
#         print('right', right)
#         #while array[right] >= pivot_value:
#         #    right -= 1
        
#         array[left], array[right] = array[right], array[left]
#     return left

def generate_random_numbers(num):
    """Generates an array of num random numbers."""
    
    # set seed so we all get the same "random" numbers
    np.random.seed(0)
    return np.random.choice(range(1, 20), num, replace=True)



def display(numbers, title = "Illustration of "):
    """Displays numbers as vertical boxes of height equal to number."""
    fig = plt.figure(0)
    plt.ion()
    plt.clf()
    plt.bar(range(len(numbers)), numbers)
    plt.title(title)
    plt.pause(0.001)



def dummy(numbers, disp=False):
    """
    only a dummy-function
    """
    for i in range(10):
        if disp:
            display(numbers, "Dummy")
        # shuffle the numbers in a meaningless way
        shuffle(numbers)
    return numbers


# numbers = generate_random_numbers(10)
# save_time = time.time() # save current time
# sorted_numbers_dm = dummy(numbers.copy(), disp=True)
# print("Dummy took: ", time.time() - save_time)

# if np.array_equal(sorted_numbers_dm, np.sort(numbers)):
#     print("OK")
# else:
#     print("NOT OK")

INFO = "BlaBla"


def choose():
    """Lets the user choose between random and custom mode"""
    
    
    is_correct_input = False
    
    while not is_correct_input:
        
        os.system(CLEAR)
        print(INFO)
        
        try:
            user_input = input("Ihre Liste:\n>> ")

            if user_input == "0":
                return 0
            elif user_input == "1":
                return 1
            else:
                print("\nEingabe nicht gemäß Vorgabe!")
                print("Neuer Versuch ...\n")
                input()
                #os.system(CLEAR)
                continue
                
        except KeyboardInterrupt:
                print("\nKeyboardInterrupt!")
                print("Abbruch...\n")
                sys.exit()


def main():
    """ """
    array = generate_random_numbers(5)
    print(array)

    insertion_sort_start = time.time()
    insertion_sort(array)
    insertion_sort_end = time.time()
    print(insertion_sort_end - insertion_sort_start)
    print(array)

    # array = generate_random_numbers(500)
    # bubble_sort_start = time.time()
    # bubble_sort(array)
    # bubble_sort_end = time.time()
    # print(bubble_sort_end - bubble_sort_start)
    
    # array = generate_random_numbers(500)
    # quick_sort_start = time.time()
    # quick_sort(array, 0, len(array) - 1)
    # quick_sort_end = time.time()
    # print(quick_sort_end - quick_sort_start)
    
    #print(array)
    #print(array1)
    #print(type(array))
    #print(array)
    #np.array([1])
    #choice = choose()
    #print(bubble_sort(array))
    #print(insertion_sort(array))
    # print(quick_sort(array, 1, 2))
    #print("quick_sort({}, {}, {})".format(array, 0, len(array) - 1))
    #print(np.sort(array) == quick_sort(array, 0, len(array) - 1))

if __name__ == "__main__":
    main()