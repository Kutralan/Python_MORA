n = int(input())
if  (2 <= n <= 10) :

    arr = map(int, input().split())
    score= list(arr)
    for i in score:
                
        if -100<= i <= 100:
            pass
        else:  
            print("Not valid")
        break
score.sort()
                       
                    
print (score[-2])
    