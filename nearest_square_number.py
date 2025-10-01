''' Find Nearest square number
https://www.codewars.com/kata/5a805d8cafa10f8b930005ba
Description:
Your task is to find the nearest square number of a positive integer n. In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

For example, if n = 111, then the nearest square number equals 121, since 111 is closer to 121, the square of 11, than 100, the square of 10.

If n is already a perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

Good luck :)

+ + + BRAINSTORM + + +
take the n and find the square root
round the number to the closest integer 
take that integer number and calculate the square
return the last calculation

'''


def nearest_sq(n):
    return round(n ** 0.5) ** 2


print(nearest_sq(1) == 1)
print(nearest_sq(2) == 1)
print(nearest_sq(10) == 9)
print(nearest_sq(111) == 121)
print(nearest_sq(9999) == 10000)
