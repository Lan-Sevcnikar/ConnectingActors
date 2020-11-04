import json
from os import listdir
from os.path import isfile, join

CA = json.load(open("joined_data_1_2/CA.json"))
ADJ_ATM = json.load(open("ADJ_ATM.json"))
scores = json.load(open("joined_data_1_2/scores.json"))

real_ADJ = {}

for a1 in CA:
    real_ADJ[a1] = {}
    for a2 in CA:
        m1 = ADJ_ATM[a1]
        m2 = ADJ_ATM[a2]
        common = list(set(m1).intersection(m2))
        best_movie = -1
        best_score = -1 
        for movie in common:
            if(scores[movie][1] > best_score and scores[movie][1] != 359152 and scores[movie][1] != 300521):
                best_score = scores[movie][1]
                best_movie = movie
        if(best_movie != -1):
            real_ADJ[a1][a2] = best_movie
        
json.dump(real_ADJ,open('rADJ.json','w'))
