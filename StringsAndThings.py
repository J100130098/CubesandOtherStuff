# strings are anything that falls within "  "

# Concatenation: put two strings together

firstName = "Fred"
lastName = "Flintstone"

fullName = (firstName +" " + lastName)

print(fullName)

# Repetition operator is the multiplier: *
print("Hip "*2 + "Hooray")
def rowYourBoat():
    print("Row "*3 + "your boat")
    print("gently down the stream")
    print("merrily, "*4)
    print("life is but a dream")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])
print(name[-1])

for i in range(len(name)):
    print(name[i])

# slicing and dicing
# slicing operator: : makes substrings (small parts of larger strings)

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name)+1):
    print(name[0:i])
# searching inside of Strings

print("Biv" in name)
print("V" not in name)

if "y" in name:
    print("the letter y is in name")

    # String Methods to investigate:
    # Method        Use Example         Explanation
    # center        aStr.center(w)
    # ljust         aStr.ljust(w)
    # rjust         aStr.rjust(w)
    # upper         aStr.upper()
    # lower         aStr.lower()
    # index         aStr.index(item)
    # rindex        aStr.rindex(item)
    # find          aStr.find(item)
    # rfind         aStr.rfind(item)
    # replace       aStr.replace(old, new)

    # Be sure to include multiple examples of all of them in use
# character functions
print(ord('B'))
print(chr(97+13))
print(str(53))
# test functions from mapper
from mapper import *

print(letterToIndex('P'))
print(indexToLetter(10))

from crypto import *

print(scramble2Encrypt("Life is insignificant in the grand scheme of the universe"))