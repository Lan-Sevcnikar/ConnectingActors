import json
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('adj') if isfile(join('adj', f))]
atm = {}
mta = {}

for f in onlyfiles:
    with open('adj/'+f) as ip:
        actor = f[0:7]
        movies = json.load(ip)
        atm[actor] = movies
        for movie in movies:
            if movie in mta:
                mta[movie].append(actor)
            else:
                mta[movie] = [actor]

with open('ADJ_MTA.json','w') as op:
    json.dump(mta,op)
with open('ADJ_ATM.json','w') as op:
    json.dump(atm,op)



