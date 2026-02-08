user=[]
pw=[]
while True:
         k=input("enter your username: ")
         counter=0
         for i in list(user):
                if i==k:
                       count=1
                else:
                       count=0
                counter=count+counter
         if counter==0:
                user.append(k)
         else:
                print("user name error")
               
         p=input("enter your password: ")
         counter2=0
         for j in list(pw):
                if j==p:
                    count2=1
                else:
                    count2=0
                counter2=count2+counter2   
         if counter2==0:
                pw.append(p)           
         else:
                print("pass word error")

                  
              
        
    
    

    
    
     






