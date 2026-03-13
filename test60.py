games=list(input().split()) #getting all  the games as input with space and adding to a list
pronoun=["I","We"] #list of pronoun 
verb=["Play","Watch"] #list of verb
for i in pronoun: # creating sentences in order of pronoun , verb , games
    for j in verb:
        for k in games:
            print(i,j,k,".")
        