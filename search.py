#shuffle cards
#import itertools and random

import itertools,random
#1,13 numbers of card
deck=list(itertools.product(range(1,14) ,["spade","heart","diamond","club"]))

#shuffle the card
random.shuffle(deck)
#draw five card
print("you got: ")
for i in range(5):


    print(deck[i][0] ,"of" ,deck[i][1])
