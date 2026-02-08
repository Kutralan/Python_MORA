a=input()
b=""
a=a.strip()
a=a.lower()
for i in a:
    b=i+b
print (b)

if a==b:
    print ('palindrome')
