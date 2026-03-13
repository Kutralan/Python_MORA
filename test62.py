matrix=[]

try:
    number_1=int(input())
except:
    print("Error")
    number_1=-1

while number_1 != -1:
    try:
        row=list(map(int,input().split()))
    except:
        print("Error")
        break

    row.insert(0,number_1)
    matrix.append(row)

    try:
        number_1=int(input())
    except:
        print("Error") 
        number_1=-1

for i in range(1,len(matrix)):
    if len(matrix[0])!=len(matrix[i]):
        print("Invalid Matrix")
        break 