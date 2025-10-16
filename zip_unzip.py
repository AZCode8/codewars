'''
Zip list with different lenght with from itertools import zip_longest.

'''

from itertools import zip_longest


def user_contacts(contact, data):
    contact_info = {}
    contact_info = zip_longest(contact, data, fillvalue=None)

    return (dict(contact_info))


print(user_contacts(["Grae Drake", "Alex Nussbacher",
      # True
                     "Darrell Silver", "Bethany Kok"], [98110, 94101, 11201]) == {'Grae Drake': 98110, 'Alex Nussbacher': 94101, 'Darrell Silver': 11201, 'Bethany Kok': None})


# from itertools import zip_longest
# numbers = [1, 2, 3]
# letters = ["a", "b", "c"]
# longest = range(5)
# zipped = zip_longest(numbers, letters, longest, fillvalue="?")
# print(list(zipped))

# #[(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]
