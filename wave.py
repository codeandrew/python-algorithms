"""
The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal rhythm achieved in a packed stadium when successive groups of spectators briefly stand, yell, and raise their arms. Immediately upon stretching to full height, the spectator returns to the usual seated position.

Task
 	In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.
Rules
 	1.  The input string will always be lower case but maybe empty.

2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
Example
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

"""


def wave(str):
    return [ (str[:key] + str[key:].capitalize()) for key, value in enumerate(str)  if 'a' <= value <= 'z']
