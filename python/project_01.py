
PINK = "\033[95m"        #Color codes
CYAN = "\033[96m"


print(f"{PINK}\U0001f4d4 Welcome to the Student Score Report!")     #Welcome message 

no_of_stu=int(input(f"{CYAN}Enter the number of students: "))        #requesting for number of students in colored text 
print("\n")
Stu_name_list=[]   #created empty lists for following use
Stu_sco_list=[]    #because ,using the list... we can store the data by appending 
Stu_gra_list=[] 

for i in range(0,no_of_stu):
    print(f"{PINK}Student{CYAN} {i+1} \U0001f468\u200d\U0001f393")   #title for each students (Eg: student 1   student 2 .....)
    name=input(f"{CYAN}Enter student name:{PINK} ")             #requesting for the name in colored text
    score=float(input(f"{CYAN}Enter student score (0-100):{PINK} "))  #requesting for the score in colored text 
    Stu_name_list.append(name)  
    Stu_sco_list.append(score)
    ''' storing those details in the certain list using append'''
    print("\n") 

for i in Stu_sco_list:  # grading each scores which are in Stu_sco_list  using for loop 
    if i >= 75:
        grade="A"
    elif i >= 65:
        grade="B" 
    elif i >= 55:
        grade="C" 
    elif i >= 40:
        grade="S"
    else:
        grade="F"
    Stu_gra_list.append(grade) # storing the grades in Stu_gra_list using append  



for i in range(no_of_stu):   #this for loop will store other student's details in order as the 1st one! using append
    my_dict={
        "Name":Stu_name_list[i],
        "Score":Stu_sco_list[i],
        "Grade":Stu_gra_list[i] 
    }
    with open("rep.txt") as f:
          #to store each student's details in new line
        f.write(f"{'Name:':<6}{my_dict['Name']:<10}{'Score:':<7}{my_dict['Score']:<6}{'Grade:':<7}{my_dict['Grade']}")
        f.close()


with open("rep.txt") as f:   
    print(f.read())
