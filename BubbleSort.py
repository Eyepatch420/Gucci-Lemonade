
#
#
#
# Bubble Sort

from __future__ import print_function


"""
param (collection): some mutable ordered collection 
return: Orderded ascending
"""

def bubble_sort(collection):

    length = len(collection)
    for i in range(length-1):
        print(i)
        swapped = False
        print(swapped)
        for j in range(length-1-i):
            print(range(length-1-i))
            if collection[j] > collection[j-1]:
                swapped = True
                print(i, j)
                print(collection[j-1])
                print(collection[j])
                print(swapped)
                collection[j], collection[j+1] = collection[j+1], collection[j]
                print(collection[j], collection[j+1] , collection[j])
                print(collection)
        if not swapped: break # Stop iteration if collection is sorted
        print(collection)
    return collection
    print(collection)

if __name__ == '__main__':
    try:
        raw_input 
    except NameError:
        raw_input = input
    user_input = raw_input('Enter numbers seperated by a comma: ').strip()
    print(user_input)
    unsorted = [int(item)for item in user_input.split(',')]
    print(unsorted)
    print(bubble_sort(unsorted), sep=',')