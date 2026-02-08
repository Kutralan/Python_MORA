x=input("Your name:-")
y=['kutralan', 'lucshman ', 'sayanudan', 'perushan', 'ragul', 'thuwaarahaa', 'mayurresh', 'lathushan', 'shabareesan ', 'kirshikeshan', 'abikeerthan ', 'thakshanna', 'danushtan', 'renuraj ', 'thanesh', 'rabilakshan', 'kirshigan', 'monikka', 'menujan', 'nikithan']

x=x.lower()
c=y.index(x) #number in order 
a=['Suseenthiran arulraj Harsiyan', 'Megavannan Varun', 'Saravanabavan Tamiran', 'Sivakumar Arun', 'Chandrakumar Darshan ', 'Srinivasan Abilash', 'Tharmabalan Sathuvaasahan', 'Srisujani Sivayokesvarasarma', 'John thevathas joshia', 'Shahaana Idaikkadershinniah', 'Pavisha Thaveswaran', 'Sureshkumaran Ramsaran', 'Vijayananthamoorthy Abishake', 'Rajaram Soorya', 'Purathanie nithiyanantham', ' Manoharan Abivarun', 'jegatheswaran kiriyangaran ', 'Aananthy Sritharan', 'harishana sureshkumar', 'Your Wish']
b=['Sutharsan Kutralan ', 'Bartheepan Lucshman', 'Nitheyakumar Sayanudan', 'Prabakaran Perushan', 'Thavarasa Ragul', 'Thuwaarahaa Sivakumar ', 'Sivaganeshan Mayurresh', 'Suresh Lathushan ', 'Rasenthiram Shabareesan', 'Vijeyakumar kirshikeshan', 'Thiruchelvam Abikeerthan ', 'Thakshanna Theivendran', 'Nesaraj Danushtan', 'Nilatharan Renuraj ', 'Thamilselvam Thanesh', 'Singarajah  Rabilakshan ', 'Sivakumar kirshigan', 'Monikka Narendranath', 'Anton Menujan Jerrid', 'Kalaignanasundram Nikithan']


for i in range(20):
    name24=b[i]
    d=i+c
    if (d<20):
        name23=a[d]
        print(f"{name24}:-{name23}")
    else:
        name23=a[(d-20)]
        print(f"{name24}:-{name23}")
