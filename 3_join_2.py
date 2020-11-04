import json

CA = []
CM = []
TA = {}
TM = {}
for i in range(1,11):
    pt = json.load(open('actors/CA_'+str(i)+'.json','r'))
    CA += pt
    pt = json.load(open('actors/TA_'+str(i)+'.json','r'))
    TA.update(pt)

for i in range(1000):
    try:
        pt = json.load(open('movies/CM_'+str(i)+'.json','r'))
        CM += pt
    except:
        print("There was an error with CM",i)

    try:
        pt = json.load(open('movies/TM_'+str(i)+'.json','r'))
        TM.update(pt)
    except:
        print("There was an error with TM",i)

with open('joined_data_1_2/TM.json','w') as op:
    json.dump(TM,op)
with open('joined_data_1_2/TA.json','w') as op:
    json.dump(TA,op)
with open('joined_data_1_2/CA.json','w') as op:
    json.dump(CA,op)
with open('joined_data_1_2/CM.json','w') as op:
    json.dump(CM,op)

print(len(CM))
