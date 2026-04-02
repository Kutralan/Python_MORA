b = input()
t=list(b)
answer = []

n = input()
p = list(n)

q = len(p)
r = len(t)

for i in range(r - q + 1):
    f = ""
    for j in range(q):
        f = f + t [i+j] 
    
    if f == n:
        answer.append(i)

print(answer) 