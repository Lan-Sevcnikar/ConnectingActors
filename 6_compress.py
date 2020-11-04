import json
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('adj') if isfile(join('adj', f))]
ta = []
_ta = {}
tm = []
_tm = {}
m = {}

TA = json.load(open("joined_data_1_2/TA.json"))
TM = json.load(open("joined_data_1_2/TM.json"))

i = 0
for (key,value) in TA.items():
    ta.append(value[1])
    _ta[key] = i
    i = i + 1

i = 0
for (key,value) in TM.items():
    tm.append(value)
    _tm[key] = i
    i = i + 1

M = json.load(open("ADJ_ATM.json"))
for (key,value) in M.items():
    temp = []
    for e in value:
        temp.append(str(_tm[e]))
    m[_ta[key]] = temp

json.dump(ta,open("c_ta.json",'w'))
json.dump(tm,open("c_tm.json",'w'))
json.dump( m,open("c_mm.json",'w'))