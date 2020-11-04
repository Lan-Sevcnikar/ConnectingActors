import json

scores = {}
for i in range(8):
    pt = json.load(open('md/m'+str(i)+'.json','r'))
    scores.update(pt)



with open('joined_data_1_2/scores.json','w') as op:
    json.dump(scores,op)

