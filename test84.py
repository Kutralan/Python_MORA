fo = open("input.txt", "r")

list2 = []

for line in fo:
    list1 = list(map(eval, line.strip().split(",")))
    list2 = list2 + list1

fo.close()

print(list2)