'''
In the US state names there is one alphabet letter that doesn't appear, find out which one
'''

import string
states = 'Alabama, Alaska, American Samoa, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, District of Columbia, Florida, Georgia, Guam, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Minor Outlying Islands, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Northern Mariana Islands, Ohio, Oklahoma, Oregon, Pennsylvania, Puerto Rico, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, U.S. Virgin Islands, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming'


def missing_letter(state_list):
    missing = []
    # for letter in state_list.lower():
    #     if letter not in missing:
    #         missing.append(letter)

    # for letter in string.ascii_lowercase:
    #     if letter not in missing:
    #         print(letter)

    for letter in string.ascii_lowercase:
        if letter not in state_list.lower():
            return letter


print(missing_letter(states))
