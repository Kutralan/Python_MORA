matrix = []
error = False
count=0
#getting input matrix
while True:
    try:
        row = list(map(int, input().split()))  
    except ValueError:   #checking whether the matrix only exist with numbers
        error = True
        continue

    if -1 in row:
        break

    matrix.append(row)
    count+=1
if error:
    print("Error")
    exit()
if count>0:
    #checking the inconsistent number of elements
    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            print("Invalid Matrix")
            exit()
    #printing transpose 
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print() 
