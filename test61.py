n=1
marks=[]
while n<5:
    studentmarks= list(map(int, input().split()))
    marks.append(studentmarks)
    n=n+1
for i in range(0,4):
    print(f"Total: {sum(marks[i])} Average: {round((sum(marks[i])/3),1)}")
