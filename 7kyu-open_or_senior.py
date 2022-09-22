"""
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Output
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

"""

# MY SOLUTION
def open_or_senior(data):
    new_data = []
    for i in data:
        age, handicap = i
        if age > 54 and handicap > 7:
            new_data.append("Senior")
        else:
            new_data.append("Open")
    
    return new_data
  
  
# CLEVER 
def openOrSenior(members):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in members]

# MORE READABLE 
def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]

  
