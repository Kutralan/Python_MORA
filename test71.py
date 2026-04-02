word = input()
vowels = ["a","e","i","o","u","A","E","I","O","U"]

vowel_count = 0
idea = []

for i in word:
    if i in vowels:
        vowel_count += 1
    else:
        idea.append(vowel_count)
        vowel_count = 0


idea.append(vowel_count)

