# - Create a variable named `firstArrayOfNumbers`
#   with the following content: `[1, 2, 3]`
# - Create a variable named `secondArrayOfNumbers`
#   with the following content: `[4, 5]`
# - Print "secondArrayOfNumbers is longer" if `secondArrayOfNumbers` has more
#   elements than `firstArrayOfNumbers`
# - Otherwise print: "firstArrayOfNumbers is the longer one"

firstArrayOfNumbers = [1,2,3]
secondArrayOfNumbers = [4,5,]
count_firstArrayOfNumbers= len(firstArrayOfNumbers) #len counts the number of elements in a list
count_secondArrayOfNumbers = len(secondArrayOfNumbers)
if count_firstArrayOfNumbers < count_secondArrayOfNumbers:
    print("secondArrayOfNumbers is longer")
else:
    print("firstArrayOfNumbers is the longer one")