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

headersss = {"Accept-Language": "en-US, en;q=0.5"}
queue = Queue()

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


def getData(tm, cm, s):
    movies = s.find('div', {'id':'filmography'}).contents[3]
    their_movies = []
    for movie in movies:
        if(movie.find('b')!=-1):
            code = movie.find('b').find('a')['href'][9:-1]
            name = movie.find('b').get_text()

            cm.append(code)
            tm[code] = name
            their_movies.append(code)
    return (tm,cm,their_movies)


def dumpData(data,s):
    with open(s,'w') as op:
        json.dump(data, op)

def download_link(directory, code):
    soup = getSoup("https://www.imdb.com/name/nm" + code)
    codes_movies = []
    translator_movies = {}
    (translator_movies,codes_movies,their_movies) = getData(translator_movies,codes_movies,soup)
    dumpData(codes_movies,'movies/CM_'+directory+'.json')
    dumpData(translator_movies,'movies/TM_'+directory+'.json')
    dumpData(their_movies,'adj/'+str(code)+'.json')
    print('Done for actor',code)

#https://stackoverflow.com/questions/52757859/python-beautifulsoup-returning-incorrect-html-code


def init_main():
    codes_actors = []
    for i in range(1,11):
        pt = json.load(open('actors/CA_'+str(i)+'.json','r'))
        for e in pt:
            codes_actors.append(e)
    return codes_actors

def main():
    codes_actors = init_main()
    for i in range(len(codes_actors)):
        queue.put((str(i),codes_actors[i]))
    for x in range(8):
        worker = DownloadWorker()
        worker.start()    


if __name__ == "__main__":
    main()
