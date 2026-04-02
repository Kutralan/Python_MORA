sentence = input().split() 
unique=0
for i in sentence:
    count=0
    for j in sentence:
        if i==j:
            count=count+1
    if count==1:
        unique=unique+1   
print(unique)            

k=0
for i in sentence:
    q=len(i)
    if q>k:
        k=q
print(k)        
