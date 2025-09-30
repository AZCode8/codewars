''' Case-sensitive!
https://www.codewars.com/kata/5a805631ba1bb55b0c0000b8/train/python
Description:
Your task is very simple. Given an input string s, case_sensitive(s), check whether all letters are lowercase or not. Return True/False and a list of all the entries that are not lowercase in order of their appearance in s.

For example, case_sensitive('codewars') returns [True, []], but case_sensitive('codeWaRs') returns [False, ['W', 'R']].

Goodluck :)

 + + + + BRAINSTORM + + + + 

In a lopop for each character in the string determinate if is upper, 
yes is uppercase character, append in a list
is not uppercase character, move to the next
until the last character and out the loop 
if the list is empty return True and the empty list
if the list is has at least one character, return False and the list with the characters.

'''


def case_sensitive(s):
    upper_letter = []
    for chr in s:
        if chr.isupper():
            upper_letter.append(chr)

    if upper_letter == []:
        return list([True, upper_letter])
    elif upper_letter != []:
        return list([False, upper_letter])


print(case_sensitive('asd') == [True, []])
print(case_sensitive('codeWaRs') == [False, ['W', 'R']])
print(case_sensitive('cellS') == [False, ['S']])
print(case_sensitive('z') == [True, []])
print(case_sensitive('') == [True, []])
