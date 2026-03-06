message=input("Enter message: ")
base=int(input("Enter base: "))
R=""
for i in message:
        
        k=ord(i)
        r=""
        while k>0:
                 
                 q=str(k%base)
                 r=q+r
                 k=k//base
                        
        R=R+r                 
print(R)                 
                

       

