print("Welcome to the Student Score Report!")

no_of_stu = int(input("Enter the number of students: "))
print()

Stu_name_list = []
Stu_sco_list = []
Stu_gra_list = []

# Input
for i in range(no_of_stu):
    print("Student", i+1)
    name = input("Enter student name: ")
    score = float(input("Enter student score (0-100): "))

    Stu_name_list.append(name)
    Stu_sco_list.append(score)
    print()

# Grading
for score in Stu_sco_list:
    if score >= 75:
        grade = "A"
    elif score >= 65:
        grade = "B"
    elif score >= 55:
        grade = "C"
    elif score >= 40:
        grade = "S"
    else:
        grade = "F"
    Stu_gra_list.append(grade)

# Write to file
with open("rep.txt", "w") as f:
    for i in range(no_of_stu):
        f.write("Name: " + Stu_name_list[i] +
                " Score: " + str(Stu_sco_list[i]) +
                " Grade: " + Stu_gra_list[i] + "\n")

# Read and display
with open("rep.txt") as f:
    print(f.read())