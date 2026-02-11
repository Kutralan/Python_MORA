a="xyz" + "abc"
print(a)
d=5>4
print(d) 
e=3+4j
print(type(e))

c=0x3bfe9 #hexadecimal
''' -0o3702    octal '''

print(type(c)) 


# -321.089e-12    means -321.089 x 10^( -12)  
''' we can use E or e as well''' 

print(id(c))
a=10
b=10 

print(a is b) 
print(id(a))
print(id(b))
_car=90
car=90
Car=90
# 9car=90   is wrong    
''' the person you write a program should be aware with variable names  because it should me the suitable one '''

'''   data whose value can change is mutable  otherwise it is immutable '''
'''
numbers strigs tuples bytes frozenset   are immutable 
lists dictionaries sets user-defined classes  are mutable


'''
 
b=97
c=b
c

print(id(b))
print(id(c))

b =98

print(id(b))
print(id(c))
j="ddkfnknf"
print(id(j))
print(id(j[2]))
print(j[2])
# lists are mutable

# if both refer to the same value the id will be equal
k=[2,3,"mo"]
k[2]= 5

c=car
d=car
print(c is d)



int()
float()
complex()
str()
chr() , ord()
hex() , oct() , bin()
