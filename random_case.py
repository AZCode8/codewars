

''' RaNDoM CAsE -- ramdom_case.py
https://www.codewars.com/kata/57073869924f34185100036d

Description:
Write a function that will randomly upper and lower characters in a string - randomCase() (random_case() for Python).

A few examples:

randomCase("Lorem ipsum dolor sit amet, consectetur adipiscing elit") == "lOReM ipSum DOloR SiT AmeT, cOnsEcTEtuR aDiPiSciNG eLIt"

randomCase("Donec eleifend cursus lobortis") == "DONeC ElEifEnD CuRsuS LoBoRTIs"
Notes:

This function will work within the basic ASCII character set to make this kata easier - so no need to make the function multibyte safe.

The letters MUST be selected randomly - filters are set to make sure there is no cheating!

++++ BRAINSTORM ++++
funtion recieive a string.
take the first character 
using module random.choice() and apply a choise either upper or lower case form the character basquet in ascii
 "".join the character to a new string

'''
import random


def random_case(x):

    return ''.join([chr.upper() if random.randint(0, 1) == 0 else chr.lower() for chr in x])


print(random_case("La Dolce Vita"))
