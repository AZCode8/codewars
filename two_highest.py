''' Return Two Highest Values in List
In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.

Examples:

[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []


sort the list for highst value
take the first value and compare with the next one
if the value. index 1 is biggert than value index 2, keep value index 1 
if value 1 is equal value 2 keep keep both and move to value 3

'''


def two_highest(arg1):
    if not arg1:
        return []

    arg1 = list(set(arg1))
    arg1.sort(reverse=True)

    if len(arg1) == 1:
        return arg1
    else:
        return [arg1[0], arg1[1]]


print(two_highest([4, 10, 10, 9]) == [10, 9])  # True
print(two_highest([15, 20, 20, 17]) == [20, 17])  # True
print(two_highest([1, 1, 1, 1, 1]) == [1])  # True
print(two_highest([15, 15]))
