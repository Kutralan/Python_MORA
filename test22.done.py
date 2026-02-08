a=int(input("enter your electricity consumption in kwh " ) )
if a==0:
    bill=0
elif a<=30:
    bill= a*10 + 150
elif a<=60:
    bill= (a-30)*25 + 30*10 +300
elif a<=90:
    bill= (a-60)*35 + 60*32 + 400
elif a<= 120:
    bill= (a-90)*50 + 60*32 + 30*35 + 1000        
elif a<= 180:
    bill= (a-120)*50 + 60*32 + 30*35 + 30*50 + 1500
elif a> 180:
    bill= (a-180)*75 + 60*32 + 30*35 + 30*50 + 60*50 + 2000
print("your current bill is ",bill)
