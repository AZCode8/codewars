'''Alphabetize a list by the nth character
Write a function that accepts two parameters, i) a string (containing a list of words) and ii) an integer (n). The function should alphabetize the list based on the nth letter of each word.

The letters should be compared case-insensitive. If both letters are the same, order them normally (lexicographically), again, case-insensitive.

Example:
    sort_it('bid, zag', 2) #=> 'zag, bid'

The length of all words provided in the list will be >= n. The format will be "x, x, x". In Haskell you'll get a list of Strings instead.

'''


def sort_it(words, n):
    lst = words.split(', ')  # split stirng in a list
    n = int(n)

    for i in range(len(lst)-1):  # loop in items in list
        for j in range(len(lst) - 1 - i):  # loop in characters in the item
            if lst[j][n-1] > lst[j+1][n-1]:  # ascii value comparison
                # assing the item in correct decending order
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return ', '.join(lst)  # convert list in string with comma and a space.


print(sort_it('bill, bell, ball, bull, a ll', 2) ==
      'a ll, ball, bell, bill, bull')  # 'Sort by the second letter'

print(sort_it('a aa, aa b, xbx, aaa, aa a', 2)
      == 'a aa, aa b, aaa, aa a, xbx')  # True

print(sort_it('words, wordz, wordy, wording', 5) ==
      'wording, words, wordy, wordz')  # "Sort by the fifth letter")
# "Sort by the second letter")
print(sort_it('he, hi, ha, ho', 2) == 'ha, he, hi, ho')
print(sort_it('zephyr, yellow, wax, a, ba, cat', 1) ==
      'a, ba, cat, wax, yellow, zephyr')  # "Sort by the first letter")
print(sort_it('hello, how, are, you, doing, today', 3) ==
      'today, are, doing, hello, you, how')  # "Sort by the third letter")
print(sort_it('August Samuel Wahlen, Ernst von Eisenach', 10)
      == 'Ernst von Eisenach, August Samuel Wahlen')  # True
print(sort_it('Paul von Oberstein, Siegfried Kircheis, Reinhard von Lohengramm, Emil von Secla', 5)
      == 'Paul von Oberstein, Emil von Secla, Siegfried Kircheis, Reinhard von Lohengramm')  # True
