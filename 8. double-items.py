# - Create an array variable named `numbers` with the following content: 
#   `[3, 4, 5, 6, 7]`
# - Double all the values in the array

numbers = [3, 4, 5, 6, 7]
for i in range(len(numbers)): # create loop to be able to access each number alone
    numbers[i] *= 2 # tell it to multiply each number in the array by 2 
print(numbers)      # once a multiplication is done on an element in the array, it is immediatly updated in the array

