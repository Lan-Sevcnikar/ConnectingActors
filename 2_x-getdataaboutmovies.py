import requests
import re
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
    def __init__(self,sz, n):
        threading.Thread.__init__(self)
        self.sz = sz
        self.dct = {}
        self.n = n

    def run(self):
        while True:
            if (queue.empty()):
                dumpData(self.dct,'md/m'+str(self.n)+'.json')
                return
            # Get the work from the queue and expand the tuple
            (directory, link) = queue.get()
            try:
                movie_data = download_link(directory, link)
                if(movie_data != {}):
                    self.dct[movie_data[0]] = movie_data[1:]
                print(1-queue.qsize()/(self.sz))
            finally:
                queue.task_done()

def getSoup(site):
    requests_session = requests.Session()
    page = requests_session.get(site, headers = headersss)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup


def getData(s,c):
    movie = s.find('a', {'title':'See more release dates'})
    #print(c, "code of movie")
    if(movie):
        #print("----")
        #print(movie.getText().strip())
        #print("----")
        res = re.search("[0-9]{4}",movie.getText().strip())
        #print(res)
        if(res):
            temp = re.search("TV Series",movie.getText().strip())
            if(temp):
                return [c, -1, -1]
            #print(c, "there is a year of reliese")
            res = res.group(0)
            support = s.find('span', {'itemprop':'ratingCount'})
            if(support):
                support = support.contents[0]
                return [c, int(res),int(support.replace(",",""))]
    return [c, -1, -1]


def dumpData(data,s):
    with open(s,'w') as op:
        json.dump(data, op)

def download_link(directory, code):
    soup = getSoup("https://www.imdb.com/title/tt" + code)
    return getData(soup,code)
    
#https://stackoverflow.com/questions/52757859/python-beautifulsoup-returning-incorrect-html-code


def init_main():
    codes_actors = []
    pt = json.load(open('joined_data_1_2/CM.json','r'))
    print(len(pt))
    pt = list(dict.fromkeys(pt))
    print(len(pt))
    return pt

def main():
    codes_actors = init_main()
    for i in range(len(codes_actors)):
    # while(True):
    #     inp = input() 
    #     download_link(str(1),inp)
        queue.put((str(i),codes_actors[i]))
    for x in range(8):
        worker = DownloadWorker(queue.qsize(),x)
        worker.start()    


if __name__ == "__main__":
    main()
