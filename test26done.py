for num in range(2,100):
    count=0
    i=2
    while num>i:
        if num%i == 0 :
            count=count+1
        i +=1

    if count == 0:
        print(f"{num} is a Prime number.")
    else:
        print(f"{num} is not a Prime number.") 