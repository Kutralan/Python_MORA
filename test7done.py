user = range(1,6)
user2=range(7,9)


print (set (user))


print (user[0])
print (user[-1])


print(len(user))            


print (list (user) +list (user2))


squares = []
for x in range(0, 9):
    squares.append(x**2)
    print(squares)


count = 0
while count < 10:
    count += 1
    if count == 5:
        break
    print(count)


for k in range(1,10):
    if k==5:
        continue
    print(k) 