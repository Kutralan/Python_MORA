import numpy as np

def read():
    global input_matrix,number_of_matrix
    filename=input()
    with open(filename) as f:
        lines = f.readlines()
        number_of_matrix=int(lines[0])
        k=1 
        input_matrix=[]
        for i in range(number_of_matrix):
            matrix=[]
            a=int(lines[k])
            for j in range(1,a+1):
                row=list(map(int,lines[j+k].split(",")))
                matrix.append(row)
            input_matrix.append(matrix)
            k=k+(a+1)

def determinant(A):
    return np.linalg.det(A)

def get_minor(A,i,j):
    return np.delete(np.delete(A,i,axis=0),j,axis=1)

def Transpose(A):
    return np.transpose(A)

def cofactor_matrix(A):
    n=len(A)
    cof=np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            minor=get_minor(A,i,j)
            cof[i][j]=((-1)**(i + j))*determinant(minor)
    
    return cof


def inverse(A):
    det= determinant(A)
    if det==0:
        return None
    cof=cofactor_matrix(A)
    adj=Transpose(cof)
    
    inv=adj/det
    
    return inv.tolist()
   
    
    
def display():
    for i in range(number_of_matrix):
        print(f"Inverse of Matrix {i+1}:")
        A = np.array(input_matrix[i])
        inv = inverse(A)
        
        if inv is None:
            print("Matrix is not invertible")
        else:
            for row in inv:
                print("".join(f"{0 if abs(elem) < 1e-9 else elem:7.2f}" for elem in row))
read()
display() 