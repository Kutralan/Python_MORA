games=list(input().split()) #getting all  the games as input with space and adding to a list
pronoun=["I","We"]
verb=["Play","Watch"]
for i in pronoun:
    for j in verb:
        for k in games:
            print(i,j,k,".")
        