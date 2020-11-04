import requests
from multiprocessing import Pool
import asyncio
import os
from varname import nameof
from bs4 import BeautifulSoup
from queue import Queue
import threading 
import datetime
import time
import pprint
import cProfile
import lxml
import json
import cchardet

queue = Queue()
headersss = {"Accept-Language": "en-US, en;q=0.5"}

class DownloadWorker(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if (queue.empty()):
                return 
            # Get the work from the queue and expand the tuple
            (directory, link) = queue.get()
            try:
                download_link(directory, link)
            finally:
                queue.task_done()


def getSoup(site):
    requests_session = requests.Session()
    page = requests_session.get(site, headers = headersss)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup


def getData(ta, ca, s):
    ass = s.findAll('h3',{"class":"lister-item-header"})
    for a in ass:
        number = a.find('span').get_text().strip()
        name = a.find('a').get_text().strip()
        code = a.find('a')['href'][8:].strip()

        ca.append(code)
        ta[code] = (number,name)
    return (ta,ca)


def dumpData(data,s):
    with open(s,'w') as op:
        json.dump(data, op)

def download_link(directory, link):
    print(link)
    soup = getSoup(link)
    codes_actors = []
    translator_actor = {}
    (translator_actor,codes_actors) = getData(translator_actor,codes_actors,soup)
    dumpData(codes_actors,'actors/CA_'+directory+'.json')
    dumpData(translator_actor,'actors/TA_'+directory+'.json')


def main():
    websites = [(i,"https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page="+str(i)) for i in range(1,11)]
    

    
    for site in websites:
        queue.put((str(site[0]),site[1]))   
    for x in range(8):
        worker = DownloadWorker()
        worker.start() 
        
        



if __name__ == "__main__":
    import time
    total_start = time.time()
    main()
    total_end = time.time()
    print(total_end-total_start)





