t = input()
n = input()

answer = []

for i in range(len(t) - len(n) + 1):
    if t[i:i+len(n)] == n:
        answer.append(i)

print(answer)