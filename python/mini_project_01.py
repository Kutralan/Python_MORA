comment="good"  # uses for last step 
name=input("Enter your name: ")  
Mat=int(input("Enter your Maths marks: "))
Sci=int(input("Enter your Science marks: "))
Eng=int(input("Enter your English marks: "))
Average= round(((Mat+Sci+Eng)/3),2)
'''calculating the average and 
Rounding the decimal number to two decimal places'''
if Average >= 75:
    Grade="A"
elif Average >=65:
    Grade="B"
elif Average >=55:
    Grade="C"
else:
    Grade="F"  
    '''grading system'''
print(f"Average={Average} \n Grade={Grade}") # displaying the average and grade in 2 lines
if Mat>=35 and Sci>=35 and Eng>=35:  # checking that "is the student passed or not using "and" logic 
    passed="yes"
else:
    passed="no"
if passed=="yes":  
    for i in range (1,4):
        print(f"You are eligible for Science stream {name}!!!")
else:    # already assigned  the comment as "good" so that while loop can run for 1st run
    while comment!="yes":
        print('Do you increase your marks next time?') 
        comment=input()  