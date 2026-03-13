matrix = []

while True:
    try:
        row = list(map(int, input().split())) 
    except ValueError and -1 in  row :
        print("Error")
        exit() 
    
    if -1 in row:
         break
    matrix.append(row)
    for i in range(1,len(matrix)):
        if len(matrix[0])!=len(matrix[i]) and -1 in row :
                print("Invalid Matrix")
                exit()

        

for j in range(len(matrix[0])):
    for i in range (len(matrix)):
        print(matrix[i][j],end=" ") 
    print()     