def is_leap(year):
    if year%400 == 0:
        leap = True
    else :
        leap = False    
    
    
    

year = int(input())
print(is_leap(year))