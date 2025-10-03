''' Mew Cipher
mew_cipher_decipher.py
Given a code in the form of an array of Strings, return a single String representing the meaning of the code found through mewing it.
The array will be of at least length 1 and every constituent String will be of equal length n to each other. Every String consists of only lowercase letters and spaces.
Each character in the output string is the average of the corresponding characters in the input strings. This means that the 1st character of the output is the average of the 1st characters of all input strings, the 2nd of the output is the average of the 2nd characters of all input strings, and so on. When the average is not a whole number, round down.
For each character at index n of the input string, μ = σ/L, where μ represents the alphabetical index of the output String's nth character, σ represents the sum of all Strings' nth characters, and L represents the length of the input array of Strings.
Spaces are given a value of 0. Letters are given a value equal to their alphabetical index. a = 1, b = 2, c = 3, and so on.
Example
String s1 = "u lk zxuq hfk as fouh";
String s2 = "y l  zpuv  xe at sicd";
String s3 = "welvayfuqbfpeaauaqcrc";

String sμ = "walk your dog at nine";
index 0: 'u' = 21, 'y' = 25, 'w' = '23', μ = 23 = 'w'
index 1: ' ' = 0,  ' ' = 0,  'e' = 5,    μ = 1.667 = 'a'

From <https://www.codewars.com/kata/671bd5419ea261fbb8d0a0ca/python>

+ + + + +  BRAINSTROM + + + + +

Variables
Input: string 
Output: string
Intermediate: integers counting loops

Funtion receive an array, the items are strings
loop through items and string count, get both counts

loop count string character for count items times.
ecahs loop take the character in the string and look for the index value in the aphabet "string.ascii_lowercase" remember import string for this objet
calculate index average = sum of index values of the position in each item and divide by item count
with the average as index get the alphabet characer and concatenate in a string. 
if the average is cero concatenate a white space   

code!!! + + + + + +

'''
import string


def decipher(code):
    item_counter = len(code)
    st_counter = len(code[0])
    letters = string.ascii_lowercase
    value = 0
    message = ''

    for st_idx in range(0, st_counter):
        for it_idx in range(0, item_counter):
            if code[it_idx][st_idx] in letters:
                value += letters.index(code[it_idx][st_idx]) + 1
        average = int(value/item_counter)
        value = 0
        if average == 0:
            message += ' '
        else:
            message += letters[average - 1]
    print(message)
    return message


print(decipher(["u lk zxuq hfk as fouh", "y l  zpuv  xe at sicd",
                "welvayfuqbfpeaauaqcrc"]) == "walk your dog at nine")  # True
