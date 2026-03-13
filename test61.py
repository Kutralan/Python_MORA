n=1
marks=[] 
while n<5:
    studentmarks= list(map(int, input().split())) #getting the input marks of all the students
    marks.append(studentmarks)
    n=n+1
for i in range(0,4):
    #printing total and average(rounded off to one decimal point)
    print(f"Total: {sum(marks[i])} Average: {round((sum(marks[i])/3),1)}")
