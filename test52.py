E=int(input("enter your electricity consumption in kwh " ) )
if E==0:
    bill=400
elif E<=30:
    bill= E*30 + 400
elif E<=60:
    bill= (E-30)*37 + 30*30 +550
elif E<=90:
    bill=  E*42 + 650
elif E<= 120:
    bill= (E-90)*50 + 90*42 + 1500       
elif E<= 180:
    bill= (E-90)*50 + 90*42 + 1500
elif E> 180:
    bill= (E-180)*75 + 90*50 + 90*42 + 2000
print("your current bill is ",bill)
