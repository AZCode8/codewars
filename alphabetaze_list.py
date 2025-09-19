'''Alphabetize a list by the nth character
Write a function that accepts two parameters, i) a string (containing a list of words) and ii) an integer (n). The function should alphabetize the list based on the nth letter of each word.

The letters should be compared case-insensitive. If both letters are the same, order them normally (lexicographically), again, case-insensitive.

Example:
    sort_it('bid, zag', 2) #=> 'zag, bid'

The length of all words provided in the list will be >= n. The format will be "x, x, x". In Haskell you'll get a list of Strings instead.

+++ BRAINSTROM +++
list_resutl 
loop through each item 
sort(slice[n]) [:n]


'''


def sort_it(words, n):
    lst1 = []

    lst = words.split(', ')

    for item in lst:
        lst1.append(item[int(n)-1])

        # lst1.sort()
    print(lst1)


print(sort_it('bill, bell, ball, bull', 2) ==
      'ball, bell, bill, bull')  # 'Sort by the second letter'
# print(sort_it('words, wordz, wordy, wording', 5) == 'wording, words, wordy, wordz') # "Sort by the fifth letter")
# print(sort_it('he, hi, ha, ho', 2) == 'ha, he, hi, ho') # "Sort by the second letter")
# print(sort_it('zephyr, yellow, wax, a, ba, cat', 1) == 'a, ba, cat, wax, yellow, zephyr') # "Sort by the first letter")
# print(sort_it('hello, how, are, you, doing, today', 3) == 'today, are, doing, hello, you, how') # "Sort by the third letter")
