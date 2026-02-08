total = 0
while True:
    num = input("Enter a number: ")
    try:
        number = int(num)
    except :
        ValueError 
        print("Please enter a number.")
        continue
    if number == 0:
        break
    total += number
print("The sum =", total)

