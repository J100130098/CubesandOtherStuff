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