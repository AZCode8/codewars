''' Sort with a sorting array
https://www.codewars.com/kata/59dc8288fc3c49cc3f000039

Sort an array according to the indices in another array.
It is guaranteed that the two arrays have the same size, and that the sorting array has all the required indices.

    sort(['x', 'y', 'z'], [1, 2, 0]) => ['z', 'x', 'y']
    
    sort(['z', 'x', 'y'], [0, 2, 1]) => ['z', 'y', 'x']

'''
from operator import itemgetter


def sort_by_sorting_list(startarray, indexarray):
    # zip the the list in an array of tuples (value, index)
    combinearray = list(zip(startarray, indexarray))

    sortedarray = sorted(combinearray, key=itemgetter(1))

    # unzip the tuples in two lists
    finalarray, indexarray = zip(*sortedarray)
    return (list(finalarray))


print(sort_by_sorting_list(['x', 'y', 'z'], [1, 2, 0]) == ['z', 'x', 'y'])
print(sort_by_sorting_list(['z', 'x', 'y'], [0, 2, 1]) == ['z', 'y', 'x'])
