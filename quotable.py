'''Thinkful - String Drills: Quotable
https://www.codewars.com/kata/5859c82bd41fc6207900007a/solutions/python
Instructions
Output
This function should take two string parameters: a person's name (name) and a quote of theirs (quote), and return a string attributing the quote to the person in the following format:

'[name] said: "[quote]"'
For example, if name is 'Grae' and 'quote' is 'Practice makes perfect' then your function should return the string

'Grae said: "Practice makes perfect"'
Unfortunately, something is wrong with the instructions in the function body. Your job is to fix it so the function returns correctly formatted quotes.

Click the "Train" button to get started, and be careful with your quotation marks.

'''


def quotable(name, quote):

    return name + " said: " + "\"" + quote + "\""


def quotable(name, quote):
    return '{} said: "{}"'.format(name, quote)


print(quotable('Grae', 'Practice makes perfect')
      == 'Grae said: "Practice makes perfect"')
print(quotable('Dan', 'Get back to work, Grae')
      == 'Dan said: "Get back to work, Grae"')
print(quotable('Alex', 'Python is great fun')
      == 'Alex said: "Python is great fun"')
print(quotable('Bethany', 'Yes, way more fun than R')
      == 'Bethany said: "Yes, way more fun than R"')
print(quotable('Darrell', 'What the heck is this thing?')
      == 'Darrell said: "What the heck is this thing?"')
