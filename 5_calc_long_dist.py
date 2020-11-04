import json
import queue 



def bfs(actor):
    visited = {}
    q = queue.Queue()

    q.put(actor)
    visited[actor] = 0

    while(not q.empty()):
        ac = q.get()

        for mo in adj_atm[ac]:
            for a in adj_mta[mo]:
                if(a in visited):
                    pass
                else:
                    visited[a] = visited[ac]+1
                    q.put(a)

    m = 0
    ba = 0
    for actor in visited:
        if(m < visited[actor]):
            m = visited[actor]
            ba = actor
    return (m,ba)



adj_mta = json.load(open("ADJ_MTA.json",'r'))
adj_atm = json.load(open("ADJ_ATM.json",'r'))
m = 0
ba = 0
for actor in adj_atm:
    print(actor)
    (ts,tm) = bfs(actor)
    if(ts > m):
        m = ts
        ba = (actor,tm)

print(m,ba)