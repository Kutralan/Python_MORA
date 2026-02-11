if __name__ == '__main__':
    k=int(input())
    SL=[]
    NL=[]
    if 2 <= k <= 5 :

        for _ in range(k):
            name = input()
            NL.append(name)
            score = float(input())
            SL.append(score)  
    else:
        print("Error")

SL.sort()
j=min(SL)
count=0
for i in range (len(SL)):
    if i==j:
        count+=1
second_high=SL[count]
