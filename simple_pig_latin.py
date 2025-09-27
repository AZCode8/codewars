'''
Simple Pig Latin
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

+++ BRAINSTROM +++
Soluton 1. 
The funtion recieive a string.
In order to be able to work with words individualy, we need to split the sting and keep it in a list.
for the first item in the list:
    Using slicing "[start : end : step]" slice the item. 
    assign to an new variable "new_text" the slice form the second character, and concatenate with the first character adding 'ay' and a white space. I could add the space after the 'ay' but I want to be clear for other people reading the code.

The original problem not mention what to do with punctaction symbols so, I get another approach to solve the problem importing string and using the module string.punctuation, so when there is a punctuation the code don't add 'ay' to the end, only with words.

'''


import string


def change_to_piglatin(text):
    new_text = ''
    list = text.split()

    # *** Solution #1 ***
    # for item in list:
    #     if item[0]:
    #         new_text += item[1:] + item[0] + 'ay' + ' '
    #     else:
    #         new_text += item[1:] + item[0] + 'ay' + ' '

    # *** Solution #2 ***
    for item in list:
        if item in string.punctuation:
            new_text += item
        else:
            new_text += (item[1:] + item[0] + 'ay ')

    # print(new_text)
    return new_text.rstrip()


print(change_to_piglatin('Pig latin is cool') == 'igPay atinlay siay oolcay')
print(change_to_piglatin('This is my string') == 'hisTay siay ymay tringsay')
print(change_to_piglatin('O tempora o mores !')
      == 'Oay emporatay oay oresmay !')
print(change_to_piglatin('Quis custodiet ipsos custodes ?')
      == 'uisQay ustodietcay psosiay ustodescay ?')
