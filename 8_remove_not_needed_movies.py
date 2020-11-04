import json
from os import listdir
from os.path import isfile, join

TM = json.load(open("joined_data_1_2/TM.json"))
RADJ = json.load(open("rADJ.json"))

used_movies = set([])

for a1 in RADJ:
    for a2 in RADJ[a1]:
        temp = RADJ[a1][a2]
        if(temp != -1):
            used_movies.add(temp)

newTM = {}
for movie in used_movies:
    newTM[movie] = TM[movie]
        
json.dump(newTM,open('newTM.json','w'))