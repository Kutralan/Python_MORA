numbers=list(map(int,input().split()))
target=int(input())


for i in range(len(numbers)-1): 
    if numbers[i] + numbers[i+1]==target:
        answer=(numbers[i] , numbers[i+1])
        print(answer)
        exit()
else:
    print("None")    