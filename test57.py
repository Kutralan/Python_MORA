num=1
while num>0:
    num=int(input())
    if num==1:
        print("non-prime")
    
    else:
        c1=0
        for i in range (1,round(num**0.5+1)):
            if num%i==0:
                c1=c1+1
            else:
                continue
        if c1==1:
            print("prime")
        elif c1 > 1:
            print("non-prime") 

