n=int(input())
i=0 
count=len(str(n))
while True:
    i="1"*count
    
    if n%int(i)==0:
        print(n//int(i))
        break
    count-=1


