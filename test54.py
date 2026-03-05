k=int(input("Input: "))
num=input()
q=num.split(" ")
p=[]
for i in q:
    p.append(i)

s=len(p)
p.sort()
min=""
for i in p:
    min=min+str(i)
print(min) 

max=min[::-1]
print(max)

