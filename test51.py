date=(input("Enter the date(Ex:year month date): "))
year,month,date=date.split(" ")
y=int(year)
m=int(month)
d=int(date)
if m<3:
    m=m+12
    y=y-1

a= 2*m + (6*(m+1))//10
b= y + y//4 - y//100 + y//400
f1=d+a+b+1
f=f1%7
if f==0:
    print("Sunday")
elif f==1:
    print("Monday")  
elif f==2:
    print("Tuesday")
elif f==3:
    print("Wednesday")
elif f==4:
    print("Thursday")
elif f==5:
    print("Friday")
elif f==6:
    print("Saturday")         

