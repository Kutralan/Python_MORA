
# Get dimensions
dimension = input("Enter the dimension: ")

# Handle invalid dimensions 
try:
    n, m = [int(value) for value in dimension.split(",")]
except ValueError:
    print("Error")
    exit()

def matrix():
    global matrixA, matrixB

    matrixA = []
    error = False
    print("Enter the matrix A: ") 

    # Input matrix A row by row
    while len(matrixA) < n:
        try:
            row = list(map(int, input().split()))  
        except ValueError:
            # If non-integer entered, mark error but continue input
            error = True
            matrixA.append([])   # count this as a row 
            continue

        matrixA.append(row)

    # After full input, check if any invalid data was entered
    if error:
        print("Error")
        exit()

    # Check if all rows in A have same number of elements 
    for i in range(len(matrixA)):
        if len(matrixA[i]) != m:
            print("Invalid Matrix")
            exit()



    matrixB = []
    error = False 
    print("Enter the matrix B: ")

    # Input matrix B row by row 
    while len(matrixB) < n:
        try:
            row = list(map(int, input().split()))  
        except ValueError:
            # Handle non-integer input
            error = True
            matrixB.append([])   # count this as a row
            continue

        matrixB.append(row)

    # Check for invalid input
    if error:
        print("Error")
        exit()

    # Check consistency of row sizes in B
    for i in range(len(matrixB)):
        if len(matrixB[i]) != m: 
            print("Invalid Matrix")
            exit()



def Transpose():
    global matrixB, matrixTranspose

    matrixTranspose = []

    # Convert columns of B into rows (transpose)
    for j in range(len(matrixB[0])):
        row = []
        for i in range(len(matrixB)):
            row.append(matrixB[i][j])  # Swap row and column
        matrixTranspose.append(row)


def multiply():
    global matrixA, matrixTranspose, result

    # Create result matrix filled with zeros
    result = [[0] * len(matrixTranspose[0]) for _ in range(len(matrixA))]

    # Matrix multiplication logic
    for i in range(len(matrixA)):                 # rows of A
        for j in range(len(matrixTranspose[0])):  # columns of Transpose(B)
            for k in range(len(matrixTranspose)): # common dimension
                result[i][j] += matrixA[i][k] * matrixTranspose[k][j]


def display():
    global result

    # Print final result matrix
    print("Matrix A X Transpose(B) :")
    for row in result:
        for val in row:
            print(val, end=" ")
        print()


# Function calls
matrix()        
Transpose()     
multiply()      
display()
