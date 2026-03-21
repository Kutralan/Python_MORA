S = list(map(int, input().split()))
number=int(input())
S.append(number)
S.sort()
k=S.index(number)
print(S)

n=S[k-1]
m=S[k+1]
print([n+1,m-1])