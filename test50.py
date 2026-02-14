a=int(input("Enter angle 1: "))
b=int(input("Enter angle 2: "))
c=int(input("Enter angle 3: "))

if a>0 and b>0 and c>0:
    if a+b+c==180:
        if a==90 or b==90 or c== 90:
            print("Right angled")
        elif a<90 and b<90 and c<90:
            print("Acute angled")
        else:
            print("Obtuse angled")    

    else:
        print("given angles do not form a triangle") 
else :
    print("given angle do not form a triangle")                  