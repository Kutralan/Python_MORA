def print_first_n_triangle_numbers(n):
    for i in range(1,n+1):
        z=int(i*(i+1)/2)
        print(z) 

def find_nth_triangle_number(n):
    return int(n*(n+1)/2) 

p=int(input("enter a number n: "))
print_first_n_triangle_numbers(p) 

print(find_nth_triangle_number(p)) 
