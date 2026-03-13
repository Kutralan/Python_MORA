matrix = []
error = False

while True:
    try:
        row = list(map(int, input().split()))
    except ValueError:
        error = True
        continue

    if -1 in row:
        break

    matrix.append(row)

if error:
    print("Error")
    exit()

for i in range(1, len(matrix)):
    if len(matrix[i]) != len(matrix[0]):
        print("Invalid Matrix")
        exit()

for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()
