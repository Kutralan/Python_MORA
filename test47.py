i=int(input())
for j in range(2,i):
    if not(i%j): # i%j==0
        print("not prime")
        break
else: 
    print("prime")