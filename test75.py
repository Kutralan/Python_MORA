# Function to read matrices from file
def read_matrices(filename):
    with open(filename,'r') as file: 
        num_matrices=int(file.readline().strip()) #read number of matrices
        matrices=[] #list to store matrices
        for _ in range(num_matrices): #loop for each matrix 
            n=int(file.readline().strip()) #read matrix size
            matrix=[list(map(int, file.readline().strip().split(','))) for _ in range(n)] 
            matrices.append(matrix) #add matrix to list
    return matrices 

# Function to compute determinant recursively
def determinant(matrix):
    n=len(matrix) 
    if n == 1:
     return matrix[0][0] 
    if n == 2:
     return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    
    det=0 #initialize determinant
    for c in range(n): #expand along first row
        minor_matrix=minor(matrix,0,c) 
        det += ((-1)**c)*matrix[0][c]*determinant(minor_matrix) #cofactor expansion
    return det

# Function to get minor matrix
def minor(matrix,i,j):
    minor_matrix=[]
    for row in (matrix[:i] + matrix[i+1:]): #remove row i
        minor_matrix.append(row[:j] + row[j+1:]) #remove column j
    return(minor_matrix)

# Function to compute cofactor matrix
def cofactor_matrix(matrix):
    n=len(matrix)
    cofactors=[] 
    for i in range(n):
        row=[]
        for j in range(n):
            minor_det=determinant(minor(matrix,i,j)) #determinant of minor
            row.append(((-1)**(i+j))*minor_det) #apply sign
        cofactors.append(row)
    return cofactors

# Function to transpose matrix
def transpose(matrix):
    matrixTranspose = []
    for j in range(len(matrix[0])): #loop columns
        row = []
        for i in range(len(matrix)): #loop rows
            row.append(matrix[i][j]) #swap indices
        matrixTranspose.append(row)
    return matrixTranspose

# Function to compute inverse
def inverse(matrix):
    det=determinant(matrix) #compute determinant
    if det==0:
        return None #not invertible
    
    cofactors=cofactor_matrix(matrix) #cofactor matrix
    adjoint=transpose(cofactors) #adjoint
    n=len(matrix)
    return [[adjoint[i][j]/det for j in range(n)] for i in range(n)] #divide by determinant

# Function to display inverse matrices
def display_inverse(matrices):
    for idx,matrix in enumerate(matrices,start=1): #loop matrices
        inv=inverse(matrix) #compute inverse
        print(f"Inverse of Matrix {idx}:") #print heading

        if inv is None:
            print("Not invertible") #handle non-invertible
            continue
        
        for row in inv: #print each row
            print("".join(f"{0.0 if abs(round(e,2))==0 else e:7.2f}" for e in row)) #formatted output


matrices=read_matrices(input())
display_inverse(matrices) 