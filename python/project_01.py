
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

my_dict={
    "Name":Stu_name_list[0],   # storing student 1 's details in dictionary 
    "Score":Stu_sco_list[0],
    "Grade":Stu_gra_list[0]

}

with open("report.txt", "w") as f:    # saving student 1's details in a text file 
  f.write(f"{'Name:':<6}{my_dict['Name']:<10}{'Score:':<7}{my_dict['Score']:<6}{'Grade:':<7}{my_dict['Grade']}")
with open("report2.txt", "w")as f:    # saving student 1's details in another text file   
    f.write(f"{CYAN}{'Name:':<6}{PINK}{my_dict['Name']:<10}{CYAN}{'Score:':<7}{PINK}{my_dict['Score']:<6}{CYAN}{'Grade:':<7}{PINK}{my_dict['Grade']}")

    '''reason for saving in 2 text files is

    my aim is to display the text report at the end using colored text and storing the data in the text file neatly
    but if I write on a text file using colored text ,it can't be stored in colored text in the text file !! rather than it will be stored using color codes...
    it was very messful   
    so that I write 2 files
    one is for displaying in the terminal (report2)
    another one is for saving (report)

    
    '''


for i in range(1,no_of_stu):   #this for loop will store other student's details in order as the 1st one! using append
    my_dict={
        "Name":Stu_name_list[i],
        "Score":Stu_sco_list[i],
        "Grade":Stu_gra_list[i] 
    }
    with open("report.txt", "a") as f:
            f.write("\n")   #to store each student's details in new line
            f.write(f"{'Name:':<6}{my_dict['Name']:<10}{'Score:':<7}{my_dict['Score']:<6}{'Grade:':<7}{my_dict['Grade']}")
    with open("report2.txt", "a")as f:
        f.write("\n")
        f.write(f"{CYAN}{'Name:':<6}{PINK}{my_dict['Name']:<10}{CYAN}{'Score:':<7}{PINK}{my_dict['Score']:<6}{CYAN}{'Grade:':<7}{PINK}{my_dict['Grade']}")


print("Student Grade Report \U0001f58b\ufe0f")
print("---------------------------------------------------------")
with open("report2.txt") as f:    #displaying in the terminal using colored text 
    print(f.read())
print("---------------------------------------------------------")    

print('\U0001f4ec Report saved to "report.txt" ')    # stored text file   