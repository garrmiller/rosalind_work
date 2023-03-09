from math import comb
import random

def flatten(l):
    return [item for sublist in l for item in sublist]
    
k = 15
m = 15
n = 17

prob_dict = {
    "kk" : 1,
    "km" : 1,
    "kn" : 1,
    "mm" : .75,
    "mn" : .5,
    "nn" : 0
    
}

list = [["k"]*k, ["m"]*m, ["n"]*n]

list = flatten(list)

hold = []
for i in range(1000001):

    choice_1 = random.choice(list)
    choice_2 = random.choice(list)
    
    both = [choice_1, choice_2]

    both = flatten(both)
    prob = prob_dict[''.join(sorted(both))]
    
    hold.append(prob)
 


print(sum(hold)/len(hold))