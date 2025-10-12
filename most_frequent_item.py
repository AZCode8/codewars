''' Find Count of Most Frequent Item in an Array
Description:
omplete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0
Example
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 
The most frequent number in the array is -1 and it occurs 5 times.

From <https://www.codewars.com/kata/56582133c932d8239900002e> 

+++ BRAINSTROM +++

Funtion count_most_frecuent(array)
sort the list, from lower to higher
take the first item and count how many time the item is in the list.

take the next value in 
array.count(item) for item in array 

'''
# APPROACH #1
#
# def count_most_frecuent(array):
#     unique_num = []
#     highest_num = 0

#     for num in array:
#         if num not in unique_num:
#             unique_num.append(num)

#     for num in unique_num:
#         if highest_num <= array.count(num):
#             highest_num = array.count(num)

#     return (highest_num)

# APPROACH #2
#


# def count_most_frecuent(collection):

#     if collection != []:
#         my_dict = {i: collection.count(i) for i in collection}
#         print(my_dict)
#         highest_num = max(my_dict.values())
#     else:
#         highest_num = 0

#     return highest_num

# APPROACH  # 3 Cleaner code


def count_most_frecuent(collection):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0


print(count_most_frecuent(
    [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]) == 5)  # True
print(count_most_frecuent(
    [-1, -1, -1, -1, -1, -1, -1, 9, 3]) == 7)  # True
print(count_most_frecuent([]) == 0)
