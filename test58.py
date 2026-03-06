n=int(input("Input number: "))
count=0
if n>2:
    for i in range (2,n+1):
        k=i//2
        total=0
        for j in range(1,k+1):
            if i%j==0:
                total=total+j
        if total>i:
            count=count+1
    print(f'Number of abundant numbers from 1 to {n} is {count}')            
elif n<2:
    print('Invalid Input') 

    

    