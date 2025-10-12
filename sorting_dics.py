''' Sorting Dictionaries
https://www.codewars.com/kata/53da6a7e112bd15cbc000012
Description:
Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary?

Create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 2 items).

The list must be sorted by the value and be sorted largest to smallest.

Examples
sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]

'''


def sort_dict(given_dic):
    lst_result = []
    values = list(given_dic.values())
    values.sort(reverse=True)  # mutating
    keys = list(given_dic.keys())

    for v in values:
        for k in keys:
            if given_dic[k] == v:
                lst_result.append((k, v))

    return lst_result


print(sort_dict({3: 1, 2: 2, 1: 3}) == [(1, 3), (2, 2), (3, 1)])
print(sort_dict({1: 2, 2: 4, 3: 6}) == [(3, 6), (2, 4), (1, 2)])
print(sort_dict({1: 3, 2: 2, 3: 1}) == [(1, 3), (2, 2), (3, 1)])
print(sort_dict({3: 1, 2: 2, 1: 3}) == [(1, 3), (2, 2), (3, 1)])
print(sort_dict({1: 2, 2: 4, 3: 6}) == [(3, 6), (2, 4), (1, 2)])
print(sort_dict({1: 5, 3: 10, 2: 2, 6: 3, 8: 8})
      == [(3, 10), (8, 8), (1, 5), (6, 3), (2, 2)])
print(sort_dict({'a': 6, 'b': 2, 'c': 4}) == [('a', 6), ('c', 4), ('b', 2)])
