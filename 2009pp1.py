S=input()
k=set()
for i in S:
    try:
        k.add(i)
    except:
        continue    
print(k)

q=list(S)

ideal=0
for i in k:
    count=0
    for j in S:
        if i==j:
            count=count+1
            if (q.index(i))+1==count:
                ideal=ideal+1
if ideal==len(k):
    print("Ideal")        
        

    