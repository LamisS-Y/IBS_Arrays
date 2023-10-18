# - Create a variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements of `numbers`
# - Print the elements of the reversed `numbers`

numbers = [3, 4, 5, 6, 7]
reversed_numbers = numbers[::-1] # we didn't add the first and last index numbers to include the whole list
print(reversed_numbers)