'''
Convert to Binary
Description:
Task Overview
Given a non-negative integer b, write a function which returns an integer d such that the binary representation of b is the same as the decimal representation of d.

Examples:

n = 1 should return 1
n = 5 should return 101
n = 11 should return 1011

funcion receive an n integer
objetive use the funtion While to solve this exercise

while the n is different to cero
collect as a string the modulo reminder of n divided by two.
asing n the floor division by to of the previos n value
repeat while loop until the floor divition is cero.

revers the string [::-1]
return the reversed integer number

'''


def to_binary(n):
    collector = ''
    while n > 0:
        # concatenating each reminder form modulos operation
        collector += str(n % 2)
        n = n//2

    return int(collector[::-1])  # reversing string


# def to_binary(n):
#     collector = ''
#     return ''.join([collector += str(n % 2), n//2, while n > 0::-1])


# return int(collector[::-1])


print(to_binary(6) == 110)  # True
print(to_binary(1) == 1)  # True
print(to_binary(2) == 10)  # True
print(to_binary(3) == 11)  # True
print(to_binary(5) == 101)  # True
