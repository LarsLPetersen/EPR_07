#!/usr/bin/env python
"""
Fle for EPR exercise 10.1.
"""

import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
import time


def generate_random_numbers(num):
    """
    generate num random numbers
    """
    np.random.seed(0) # set seed so we all get the same "random" numbers
    return np.random.choice(range(1, 20), num, replace=True)


def display(numbers, title=""):
    """
    display results, add all the necessary things
    to display your own results
    """
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


numbers = generate_random_numbers(10)
save_time = time.time() # save current time
sorted_numbers_dm = dummy(numbers.copy(), disp=True)
print("Dummy took: ", time.time() - save_time)

if np.array_equal(sorted_numbers_dm, np.sort(numbers)):
    print("OK")
else:
    print("NOT OK")
