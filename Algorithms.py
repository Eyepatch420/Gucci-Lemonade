
"""
This is a python implementation of the bogo sort algorithm.
DOCtest

python3 -m doctest -v bogosort.py

param collection: some mutable ordered collection with heterogenous comparable items
inside.
return: the same collection ordered by ascending.
Examples:
bogosort([0, 5, 3, 2, 2])
[0, 2, 2, 3, 5]
"""

from __future__ import print_function
import random

def bogosort(collection):



    def isSorted(collection):
        if len(collection) < 2:
            return True
        for i in range(len(collection)-1):
            if collection[i] > collection[i+1]:
                return False
        return True

    while not isSorted(collection):
        random.shuffle(collection)
    return collection

if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input

user_input = raw_input('Enter numbers seperated by a comma: \n').strip()
unsorted = [int(item)for item in user_input.split(',')]
print(bogosort(unsorted))
