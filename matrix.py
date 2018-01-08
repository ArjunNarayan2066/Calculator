#ROW BY COLUMN!!!
#ROW MATRIX
#len(matrix) = # of rows, USE X FOR ROWS
#len(matrix[0]) = # of columns, USE Y FOR COLUMNS
#matrix[-1] = R or C for row or column
#for i in range (len(matrix)-2) to iterate through 
    #matrix[-2] = max length

def getMaxLength(matrix):
    max_length = matrix[-2]
    for x in range (len(matrix)-2): #Iterating through rows
        for y in range (len(matrix[0])): #Iterating through columns
                val = str(matrix[x][y])
                if len(val) > max_length:
                    max_length = len(val)
    return max_length

def printMatrix(matrix):
    #For A Row Matrix
    if matrix[-1] == "R":
        for x in range (len(matrix)-2):
            line = "|"
            for y in range (len(matrix[0])):
                num = str(matrix[x][y])
                if len(num) < matrix[-2]:
                    num = (" " * (matrix[-2] - len(num))) + num
                if y < len(matrix[0]) - 1:
                    num += ", "
                line += num
            print(line + "|")
            
    elif matrix[-1] == "C":
        for y in range (len(matrix[0])):
            line = "|"
            for x in range (len(matrix)-2):
                num = str(matrix[x][y])
                if len(num) < matrix[-2]:
                    num = (" " * (matrix[-2] - len(num))) + num
                if x != len(matrix) - 3:
                    num += ", "
                line += num
            print(line + "|")

def makeMatrix():
    while True:
        row = int(input("Please enter number of rows\n"))
        col = int(input("Please enter nunber of columns\n"))
        max_length = 0

        rows = [0 for i in range (col)]
        matrix = [rows for i in range (row)]

        print("Entering values row by row\n")

        for x in range (len(matrix)): #Iterating through rows
            line = []
            for y in range (len(matrix[0])): #Iterating through columns
                val = (input("Entry: " + str(x+1) + "," + str(y+1) + "\n"))
                if len(val) > max_length:
                    max_length = len(val)
                line.append(float(val))
            matrix[x] = line
        matrix.append(max_length+2)
        matrix.append("R")
            
        printMatrix(matrix)

        if(input("Is this accurate? Y/N \n") != "N"):
            break       
            
    return matrix

def makeColumnMatrix (matrix):
    row = len(matrix)
    col = len(matrix[0])
    column_matrix = []

    for y in range (len(matrix[0])):#Iterate rows of RowMatrix
        column_matrix.append([])
        for x in range (len(matrix)-2):#Iterate columns of RowMatrix
            column_matrix[y].append(matrix[x][y])
    column_matrix.append(matrix[-2])
    column_matrix.append("C")
    return column_matrix

###ERO FUNCTIONS#####
###ALL FUNCTION USING ROW MATRICES###

def multiply_add (row1, row2, val):
    #Adds val*row1 to row2
    temp = row1
    temp = multiply(temp, val)
    print("Adding")
    print(row1)
    print("to")
    print(row2)
    return add_row(temp, row2)
    

def subtract_row (row1, row):
    #Subtracts row1 to row2
    for i in range (len(row1)):
        row2[i] -= row1[i]
    return row2

def add_row (row1, row2):
    #Adds row1 to row2
    for i in range (len(row1)):
        row2[i] += row1[i]
    return row2

def divide (row, val):
    return multiply(row, 1/val)

def multiply (row, val):
    print("Multiplying %d to " %(val))
    print(row)
    for i in range (len(row)):
        row[i] *= val
    return row

def subtract_val (row, val):
    return add_val (row, -1*val)

def add_val(row, val):
    for i in range(len(row)):
        row[i] += val
    return row


def rowSwap(matrix, row1, row2):
    print(matrix[-1])
    if (matrix[-1] != 'R'):
        print ("ERROR: Row swap called on invalid matrix")
        return
    temp = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = temp
    return matrix

###END OF ERO FUNCTIONS###

def zero_column (matrix, column_matrix, val):
    base_row_index = val
    base_column_index = val

    #Find minimum of column    
    min_value = min(column_matrix[val][val:])
    minIndex = column_matrix[val].index(min_value)

    #Move either min to top, if @ top leave @ top, or if min = 0 move to bottom & put next min @ top
    if minIndex == base_row_index and column_matrix[base_column_index][minIndex] == 0:
        #0 at top
        matrix = rowSwap(matrix, minIndex, len(matrix)-3)#Move 0 to bottom
        column_matrix = makeColumnMatrix(matrix)#Update new matrix

        #Re-evaluate Minimum
        min_value = min(column_matrix[val][val:len(matrix)-3])
        minIndex = column_matrix[val].index(min_value)

    if minIndex != base_row_index and column_matrix[base_column_index][minIndex] != 0:
        #Moving min to top
        matrix = rowSwap(matrix, minIndex, base_row_index)
        column_matrix = makeColumnMatrix(matrix)#Update new matrix

    printMatrix(matrix) 

    #Zeroes now at bottom, minimum at top
    #Calculate adjustment & zero each row under the base_row_index
    for y in range(base_row_index+1, len(column_matrix[0])):
        adjust = -1*column_matrix[base_column_index][y]/column_matrix[base_column_index][base_row_index]

        print("%d * row %d  +  row %d" % (adjust, base_row_index, y))
        print("%d = " % (base_row_index))
        print(matrix[base_row_index])
        print("%d = " % (y))
        print(matrix[y])
        print("\n")
        
        temp = []
        for i in range (len(matrix[0])):
            temp.append(matrix[base_row_index][i])
        matrix[y] = multiply_add(temp, matrix[y], adjust)
        matrix[-2] = getMaxLength(matrix)
        print("\n")
        #column_matrix = makeColumnMatrix(matrix)
        printMatrix(matrix)
        print("hi")

    return matrix
        


        
    
def ref(matrix):
    rank = 0
    for y in range (len(column_matrix)):#Iterate through column of column matrix
        matrix = zero_column(matrix, column_matrix, y)
        
        

def run():
    matrix = makeMatrix()
    print(matrix)
    column_matrix = makeColumnMatrix(matrix)
    ref(matrix)
    


run()
            

    
