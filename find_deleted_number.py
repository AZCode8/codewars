''' Lost number in number sequence
https://www.codewars.com/kata/595aa94353e43a8746000120/python
Description:
An ordered sequence of numbers from 1 to N is given. One number might have deleted from it, then the remaining numbers were mixed. Find the number that was deleted.

Example:

The starting array sequence is [1,2,3,4,5,6,7,8,9]
The mixed array with one deleted number is [3,2,4,6,7,8,1,9]
Your function should return the int 5.
If no number was deleted from the starting array, your function should return the int 0.

Note: N may be 1 or less (in the latter case, the first array will be []).

+ + + BRAINSTROM + + + 
The funcion will received two arrays.
comparison array and mixed array
take one element of mixed array and look if that element exist in the comparison array.
if the number is not there, missing number array.

let's code!

'''


def find_deleted_number(arr, mixed_arr):

    for element in arr:
        if element not in mixed_arr:
            return element
        else:
            continue
    return 0


print(find_deleted_number([1, 2, 3, 4, 5, 6, 7, 8, 9], [
    3, 2, 4, 6, 7, 8, 1, 9]) == 5)
print(find_deleted_number([1, 2, 3, 4, 5], [3, 4, 1, 5]) == 2)
print(find_deleted_number([1, 2, 3, 4, 5, 6, 7, 8, 9], [
    1, 9, 7, 4, 6, 2, 3, 8]) == 5)
print(find_deleted_number([1, 2, 3, 4, 5, 6, 7, 8, 9], [
    5, 7, 6, 9, 4, 8, 1, 2, 3]) == 0)
