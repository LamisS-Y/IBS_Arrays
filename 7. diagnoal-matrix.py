 # - Create a two dimensional list dynamically with the following content.
 #   Note that a two dimensional list is often called matrix if every
 #   internal list has the same length.
 #   Use a loop!
 # 
 #   1 0 0 0
 #   0 1 0 0
 #   0 0 1 0
 #   0 0 0 1
 # 
 #   Its length should depend on a variable
 #  
 # - Print this two dimensional list to the output

matrix_size = int(input("Please input the size of the matrix: "))
matrix = [] # to store the two-dimensional list
for i in range (matrix_size): # this is to define the rows
    row = []
    for j in range (matrix_size): # to define the colomns
        if i == j: # when the row number = the colomn number
            row.append(1) # add 1 to the place
        else:
            row.append(0) # add 0 to the place
    matrix.append(row) # we are telling the matrix that its rows are base on the above if and else functions
for row in matrix: # create a loop that shows everyline in the loop above
    print(" ".join(map(str, row))) #map(str,row) turns every element in the "row" to string, ensure all the elements are easily combined into a single string
                                   # " ".join, to turn the matrix (every single row) into one string. " " is to seperate the elements.   