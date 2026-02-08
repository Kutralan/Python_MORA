for i in range (2,99): 
        count=0
        counter=0
        for j in range(2,99):
                
                if i%j==0:
                        count=1
                else:
                        count=0
                counter=counter+count
        if counter==1:
                print(i)
                             