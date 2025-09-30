''' Uno Match Play -- 
Description: 
Inspired by the popular Uno card game

Task
Write a function that takes in two arguments: (1) a player's current hand and (2) the current face-up card on the table. The function will return True if the player can make a play, or False if the player has to draw from the deck.

A player can make a play if they have a card:
that is the same color as the face-up card, OR that is the same number as the face-up card.
Cards Format
Colors are always lowercase: `"red", "yellow", "blue", "green".
Numbers are digits from 0 to 9.
Each card is formatted as "color number", e.g., "blue 5"
Notes
Return False if the player is not holding any cards (an empty list).
There are no special cards or wildcards in this deck.

Examples:

["yellow 3", "yellow 7", "blue 8", "red 9", "red 2"], "red 1" ➞ True  # "red 9" or "red 2"
["yellow 3", "yellow 7"], "blue 7"                   ➞ True  # "yellow 7"
["yellow 3", "yellow 5", "red 8"], "red 2"           ➞ True  # "red 8"
["yellow 3", "yellow 5", "red 8"], "blue 5"          ➞ True  # "yellow 5"
["yellow 3", "blue 5", "red 8", "red 9"], "green 4"  ➞ False
["yellow 3", "red 8"], "green 2"                     ➞ False


'''


def can_play(hand, face_up):
    if face_up == '' or hand == []:
        return False
    for card in hand:
        if card.startswith(face_up[:-2]) or card.endswith(face_up[-1:]):
            return True
        else:
            continue
    else:
        return False


print(can_play(["yellow 3", "yellow 7", "blue 8",
      "red 9", "red 2"], "red 1") == True)  # "red 9" or "red 2"
print(can_play(["yellow 3", "yellow 7", "blue 8",
      "red 9", "red 2"], "red 1") == True)  # "red 9" or "red 2"
print(can_play(["yellow 3", "yellow 7"], "blue 7") == True)  # "yellow 7"
print(can_play(["yellow 3", "yellow 5",
      "red 8"], "red 2") == True)  # "red 8"
print(can_play(["yellow 3", "yellow 5", "red 8"],
      "blue 5") == True)  # "yellow 5"
print(can_play(["yellow 3", "blue 5",
      "red 8", "red 9"], "green 4") == False)  # return False
print(can_play(["yellow 3", "red 8"], "") == False)  # Return False
print(can_play(['yellow 3', 'blue 5', 'red 8', 'red 9'], 'green 4') == False)
print((can_play([], 'green 2') == False))
